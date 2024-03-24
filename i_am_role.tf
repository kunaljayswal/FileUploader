resource "aws_iam_role" "cluster_role" {
  name = "AWSServiceRoleForAmazonEKS"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

  attach_inline_policy = [
    <<EOF
{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "eks:CreateCluster",
            "eks:DescribeCluster",
            "eks:DeleteCluster",
            "eks:ListClusters",
            "eks:UpdateClusterConfig",
            "eks:UpdateClusterVersion",
            "iam:PassRole",
            "iam:CreateServiceLinkedRole",
            "iam:ListAttachedRolePolicies",
            "iam:GetRole"
          ],
          "Resource": "*"
        }
      ]
    }
EOF
  ]
}
