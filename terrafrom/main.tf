# Declare the provider (in this case, AWS)
provider "aws" {
  region = "US West (N. California) us-west-1" # Specify your desired region
}

# Define the S3 bucket resource
resource "aws_s3_bucket" "assignmentuploadfile" {
  bucket = "assignmentuploadfile" # Specify the name of your S3 bucket
  acl    = "private"         # Specify the access control list (ACL) for the bucket

  tags = {
    Name = "assignmentuploadfile"   # Add tags to the bucket for easier identification
  }
}