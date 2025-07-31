provider "aws" {
  profile = "default"
  # It's good practice to be explicit with your region.
  # "uswest" is not a valid AWS region. You likely mean "us-west-1" or "us-west-2".
  # I'll use "us-west-2" as a common example. Please adjust to your actual desired region.
  region = "us-west-2" 
}

resource "aws_s3_bucket" "tf-try1" {
  bucket = "jcck25-terraform-bucket-073120255"
  # You should also typically set object_ownership to BucketOwnerPreferred
  # or BucketOwnerEnforced when using ACLs for clarity and best practice.
  # For new buckets, AWS generally recommends BucketOwnerEnforced to disable ACLs entirely
  # and rely solely on bucket policies, but if you truly need ACLs,
  # BucketOwnerPreferred is the way to go with a separate ACL resource.
  # For this example, let's include it for best practice.
  tags = {
    Name = "MyTerraformBucket"
  }
}

# Add this resource to explicitly set the ACL
resource "aws_s3_bucket_acl" "tf-try1_acl" {
  bucket = aws_s3_bucket.tf-try1.id
  acl    = "private"
  # Ensure bucket ownership controls are set up correctly when using ACLs.
  # This makes sure the bucket owner has full control over objects.
  # Add a dependency to ensure ownership controls are applied before the ACL.
  depends_on = [aws_s3_bucket_ownership_controls.tf-try1_ownership] 
}

# It's highly recommended to explicitly define bucket ownership controls,
# especially if you're managing ACLs.
resource "aws_s3_bucket_ownership_controls" "tf-try1_ownership" {
  bucket = aws_s3_bucket.tf-try1.id
  rule {
    object_ownership = "BucketOwnerPreferred" # Or "BucketOwnerEnforced" if you want to disable ACLs
  }
}

# Additionally, consider configuring Public Access Block settings for security
# New S3 buckets have all public access blocks enabled by default.
# If you explicitly want "private" and no public access, ensure these are true.
# resource "aws_s3_bucket_public_access_block" "tf-try1_public_access_block" {
#   bucket = aws_s3_bucket.tf-try1.id
#   block_public_acls   = true
#   block_public_policy = true
#   ignore_public_acls  = true
#   restrict_public_buckets = true
# }

/*

You're encountering a common issue in Terraform when trying to set an S3 bucket's Access Control List (ACL) directly within the aws_s3_bucket resource block.

The problem is that the acl argument within the aws_s3_bucket resource is deprecated. AWS is moving towards a model where bucket ACLs are disabled by default for new buckets, and permissions are primarily managed through S3 Bucket Policies and AWS Identity and Access Management (IAM) policies.

While private is still a valid canned ACL value, Terraform now requires you to manage ACLs using a separate resource: aws_s3_bucket_acl.












*/



