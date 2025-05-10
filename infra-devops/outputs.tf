# outputs.tf

output "vpc_id" {

  description = "ID da VPC criada"

  value = aws_vpc.main.id

}

output "s3_bucket_name" {

  description = "Nome do Bucket S3 criado"

  value = aws_s3_bucket.lab_bucket.bucket

}

output "s3_bucket_arn" {

  description = "ARN do Bucket S3 criado"

  value = aws_s3_bucket.lab_bucket.arn

}
