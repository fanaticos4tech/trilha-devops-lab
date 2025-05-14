terraform {
  backend "s3" {
    bucket  = "prod-trilha-devops-fanaticos4tech-terraform-state"
    key     = "terraform.tfstate"
    region  = var.aws_region
    encrypt = true
  }
}
