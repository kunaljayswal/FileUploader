resource "aws_s3_bucket" "uploads" {
  bucket = var.assignmentuploadfile
  acl    = "private"

  # Versioning configuration (optional)
  versioning {
    enabled = true
  }
}

variable "assignmentuploadfile" {
  type = string
  default = "file-upload-bucket"
}