provider "aws" {
  region = "us-east-2"
}

resource "aws_launch_configuration" "example" {
  image_id = "ami-0a63f96e85105c6d3"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.instance.id]

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World" > index.html
              nohup busybox httpd -f -p ${var.server_port} &
              EOF
  # Required when using a launch configuration with an auto scaling group.
  # https://www.terraform.io/docs/providers/aws/r/launch_configuration.html
  lifecycle {
    create_before_destroy = true
  }
}

# auto-scaling group (ASG)
resource "aws_autoscaling_group" "asg_example" {
  launch_configuration = aws_launch_configuration.example.name
  vpc_zone_identifier = data.aws_subnet_ids.default.ids

  max_size = 4
  min_size = 2

  tag {
    key = "Name"
    propagate_at_launch = true
    value = "terraform-asg-example"
  }
}

# security group
resource "aws_security_group" "instance" {
  name = "terraform-example-instace"

  ingress {
    from_port = var.server_port
    to_port = var.server_port
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "server_port" {
  description = "http port 8080"
  type = number
  default = 8080
}

output "public_ip" {
  value = aws_instance.example.public_ip
  description = "The public IP address of the web server"
}

output "arn_id" {
  value = aws_instance.example.arn
}

# data source
data "aws_vpc" "default" {
  default = true
}

data "aws_vpc" "default1" {
  vpc_id = data.aws_vpc.default.id
}