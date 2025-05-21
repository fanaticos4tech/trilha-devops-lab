# ecs.tf
# --- Rede (Assume que a VPC e Subnet da Sessão 1/2 existem) ---
# Precisamos de Subnets e um Security Group para o Fargate
# Se você não fez o desafio da subnet na Sessão 2, crie-as agora.
# Exemplo: Criando duas subnets públicas em AZs diferentes

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.0"
}

provider "aws" {
  region = var.aws_region
}

# Criação da VPC
resource "aws_vpc" "main" {

  cidr_block = var.vpc_cidr_block #10.0.0.0/16

  enable_dns_support = true

  enable_dns_hostnames = true

  tags = merge(var.common_tags, {

    Name = "trilha-devops-vpc"

  })

}

resource "aws_subnet" "public_a" {

  vpc_id            = aws_vpc.main.id

  cidr_block        = "10.0.1.0/24"

  availability_zone = "${var.aws_region}a"

  map_public_ip_on_launch = true # Para acesso direto inicial (não ideal para prod)

  tags = merge(var.common_tags, {

    Name = "trilha-devops-public-subnet-a"

  })

}

resource "aws_subnet" "public_b" {

  vpc_id            = aws_vpc.main.id

  cidr_block        = "10.0.2.0/24"

  availability_zone = "${var.aws_region}b"

  map_public_ip_on_launch = true

  tags = merge(var.common_tags, {

    Name = "trilha-devops-public-subnet-b"

  })

}

# Security Group para permitir tráfego na porta da aplicação (8080)

resource "aws_security_group" "ecs_service_sg" {

  name        = "trilha-devops-ecs-service-sg"

  description = "Allow traffic to ECS service on app port"

  vpc_id      = aws_vpc.main.id

  ingress {

    from_port   = var.app_port

    to_port     = var.app_port

    protocol    = "tcp"

    cidr_blocks = ["0.0.0.0/0"] # Permite acesso de qualquer IP (restringir em prod!)

  }

  egress {

    from_port   = 0

    to_port     = 0

    protocol    = "-1" # Permite todo tráfego de saída

    cidr_blocks = ["0.0.0.0/0"]

  }

  tags = merge(var.common_tags, {

    Name = "trilha-devops-ecs-service-sg"

  })

}

# --- Cluster ECS ---

resource "aws_ecs_cluster" "main" {

  name = var.ecs_cluster_name

  tags = merge(var.common_tags, {

    Name = var.ecs_cluster_name

  })

}

# --- IAM Role para a Task ECS ---

# Permite que a task acesse outros serviços AWS se necessário (ex: S3, Secrets Manager)

# Por enquanto, uma role básica é suficiente.

resource "aws_iam_role" "ecs_task_execution_role" {

  name = "trilha-devops-ecsTaskExecutionRole"

  # Política de confiança que permite ao ECS assumir esta role

  assume_role_policy = jsonencode({

    Version = "2012-10-17",

    Statement = [{

      Action = "sts:AssumeRole",

      Effect = "Allow",

      Principal = {

        Service = "ecs-tasks.amazonaws.com"

      }

    }]

  })

  tags = var.common_tags

}

# Anexa a política gerenciada pela AWS necessária para a execução da task Fargate

# (Permissões para puxar imagem do ECR, enviar logs para CloudWatch, etc.)

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {

  role       = aws_iam_role.ecs_task_execution_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"

}

# --- Task Definition ECS ---

resource "aws_ecs_task_definition" "app_task" {

  family                   = var.ecs_task_family

  network_mode             = "awsvpc" # Necessário para Fargate

  requires_compatibilities = ["FARGATE"]

  cpu                      = var.app_cpu

  memory                   = var.app_memory

  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  # task_role_arn          = aws_iam_role.ecs_task_execution_role.arn # Role para a aplicação (se precisar acessar AWS)

  # Definição do container

  container_definitions = jsonencode([

    {

      name      = "trilha-devops-app-container",

      # Imagem placeholder inicial - será atualizada pelo CI/CD

      image     = "public.ecr.aws/docker/library/python:3.9-slim", 

      cpu       = var.app_cpu,

      memory    = var.app_memory,

      essential = true,

      portMappings = [

        {

          containerPort = var.app_port,

          hostPort      = var.app_port # No modo awsvpc, hostPort = containerPort

        }

      ],

      # Configuração de Logs (envia para CloudWatch)

      logConfiguration = {

        logDriver = "awslogs",

        options = {

          "awslogs-group"         = "/ecs/${var.ecs_task_family}",

          "awslogs-region"        = var.aws_region,

          "awslogs-stream-prefix" = "ecs"

        }

      },

      # Exemplo de como passar variáveis de ambiente

      environment = [

        { name = "NAME", value = "ECS Fargate" },

        { name = "BACKGROUND_COLOR", value = "lightgreen" }

      ]

    }

  ])

  tags = merge(var.common_tags, {

    Name = var.ecs_task_family

  })

}

# --- CloudWatch Log Group (para onde os logs do container serão enviados) ---

resource "aws_cloudwatch_log_group" "ecs_log_group" {

  name              = "/ecs/${var.ecs_task_family}"

  retention_in_days = 7 # Define por quanto tempo manter os logs

  tags = merge(var.common_tags, {

    Name = "${var.ecs_task_family}-log-group"

  })

}

# --- ECS Service ---

resource "aws_ecs_service" "main" {

  name            = var.ecs_service_name

  cluster         = aws_ecs_cluster.main.id

  task_definition = aws_ecs_task_definition.app_task.arn

  desired_count   = 1 # Número desejado de instâncias da task rodando

  launch_type     = "FARGATE"

  # Configuração de rede para Fargate

  network_configuration {

    subnets         = [aws_subnet.public_a.id, aws_subnet.public_b.id] # Roda nas subnets criadas

    security_groups = [aws_security_group.ecs_service_sg.id] # Usa o security group criado

    assign_public_ip = true # Atribui IP público à task (para acesso direto inicial)

  }

  # Garante que o serviço só seja criado/atualizado após a task definition

  depends_on = [aws_ecs_task_definition.app_task]

  # Configuração para rolling updates (padrão)

  deployment_controller {

    type = "ECS"

  }

  tags = merge(var.common_tags, {

    Name = var.ecs_service_name

  })

}
