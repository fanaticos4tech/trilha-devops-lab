# variables.tf

variable "aws_region" {

  description = "Região AWS para criar os recursos"

  type = string

  default = "us-east-1" # Você pode mudar para sua região preferida

}

variable "vpc_cidr_block" {

  description = "Bloco CIDR para a VPC"

  type = string

  default = "10.0.0.0/16"

}

variable "bucket_prefix" {

  description = "Prefixo para o nome do bucket S3 (será concatenado com um ID único)"

  type = string

  default = "trilha-devops-lab"

}

variable "common_tags" {

  description = "Tags comuns para aplicar a todos os recursos"

  type = map(string)

  default = {

    Project = "Trilha DevOps Lab"

    Environment = "Development"

    ManagedBy = "Terraform"

  }

}
