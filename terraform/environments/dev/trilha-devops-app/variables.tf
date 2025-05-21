variable "aws_region" {
  default = "eu-central-1"
}

variable "ecr_repository_name" {
  default = "trilha-devops-app"
}

variable "ecs_cluster_name" {
  default = "trilha-devops-cluster"
}

variable "ecs_service_name" {
  default = "trilha-devops-service"
}

variable "ecs_task_family" {
  default = "trilha-devops-task"
}

variable "app_port" {
  default = 8080
}

variable "app_cpu" {
  default = 256
}

variable "app_memory" {
  default = 512
}

variable "common_tags" {
  type    = map(string)
  default = {
    Project = "TrilhaDevOps"
    Owner   = "Aluno"
  }
}

variable "vpc_cidr_block" {

  description = "Bloco CIDR para a VPC"

  type = string

  default = "10.0.0.0/16"

}