# main.tf

# Criação da VPC

resource "aws_vpc" "main" {

  cidr_block = var.vpc_cidr_block #10.0.0.0/16

  enable_dns_support = true

  enable_dns_hostnames = true

  tags = merge(var.common_tags, {

    Name = "trilha-devops-vpc"

  })

}

# Criação do S3 Bucket

# Nota: Nomes de bucket S3 são globalmente únicos.

# Usaremos um nome aleatório para evitar conflitos.

resource "random_id" "bucket_id" {

  byte_length = 8

}

resource "aws_s3_bucket" "lab_bucket" {

  # Nome do bucket: prefixo definido na variável + ID aleatório

  bucket = "${var.bucket_prefix}-${random_id.bucket_id.hex}"

  tags = merge(var.common_tags, {

    Name = "trilha-devops-lab-bucket"

  })

}

# Configuração de versionamento para o bucket

resource "aws_s3_bucket_versioning" "lab_bucket_versioning" {

  bucket = aws_s3_bucket.lab_bucket.id # Referencia o bucket criado acima

  versioning_configuration {

    status = "Enabled"

  }

}

# Configuração de bloqueio de acesso público para o bucket (Boas práticas de segurança)

resource "aws_s3_bucket_public_access_block" "lab_bucket_pab" {

  bucket = aws_s3_bucket.lab_bucket.id

  block_public_acls = true

  block_public_policy = true

  ignore_public_acls = true

  restrict_public_buckets = true

}
