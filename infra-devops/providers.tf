# providers.tf

terraform {

  required_providers {

    aws = {

      source = "hashicorp/aws"

      version = "~> 5.0" # Use uma versão recente do provider AWS

    }

  }

  required_version = ">= 1.0" # Exige versão mínima do Terraform

}

provider "aws" {

  region = var.aws_region

}
