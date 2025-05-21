terraform {
  backend "s3" {
    bucket  = "dev-fanaticos4tech-terraform-state"
    key     = "trilha-devops-app/terraform.tfstate"
    region  = "eu-central-1"
    encrypt = true
  }
}
