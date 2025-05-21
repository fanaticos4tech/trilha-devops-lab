output "ecr_repository_url" {
  value = aws_ecr_repository.app_ecr_repo.repository_url
}

output "ecs_cluster_name_out" {
  value = aws_ecs_cluster.main.name
}

output "ecs_service_name_out" {
  value = aws_ecs_service.main.name
}
