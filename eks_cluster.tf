# Configure AWS provider (assuming you have a separate provider.tf file)
# ...

resource "aws_eks_cluster" "cluster" {
  name          = "file-uploader-eks"
  role_arn      = aws_iam_role.cluster_role.arn
  vpc_config    = aws_vpc_config.cluster_vpc.config
  kubernetes_version = "~> 1.23"
  # Node group configuration
  node_group {
    name           = "default-node-group"
    instance_type = "t3.medium"
    desired_capacity = 2
  }
}

# Resources for IAM role and VPC configuration (separate files not shown)
