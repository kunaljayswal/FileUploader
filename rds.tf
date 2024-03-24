resource "aws_db_instance" "database" {
  allocated_storage = 20
  engine            = "PostgreSQL"  # Replace with your desired engine (e.g., postgres)
  engine_version    = "10.4"  # Update with your desired version
  instance_class     = "db.t3.micro"
  name              = "file-uploader"
  username          = "dbuser"
  password          = var.db_password  # Reference a sensitive variable
  vpc_security_group_ids = [sg-01c18d4b2a9b56f4a]

  # Additional configuration options (not shown)
}

variable "db_password" {
  type = string
  sensitive = true
}
