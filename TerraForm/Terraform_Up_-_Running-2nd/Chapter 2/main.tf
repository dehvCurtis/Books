provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" // Ubuntu AMI
  instance_type = "t2.micro"
}

//resource "aws_launch_configuration" "example" {
//  image_id = "ami-0c55b159cbfafe1f0" // Ubuntu AMI
//  instance_type = "t2.micro"
//  security_groups = [aws_security_group.instance.id]
//  user_data = <<-EOF
//              #!/bin/bash
//              echo "Hello Terraform Word" > index.html
//              nohup busybox httpd -f -p ${var.server_port} &
//              EOF
//  lifecycle {
//    create_before_destroy = true
//  }
//}
//
//resource "aws_autoscaling_group" "example" {
//  launch_configuration = aws_launch_configuration.example.name
//  vpc_zone_identifier  = data.aws_subnet_ids.default.ids
//
//  min_size = 2
//  max_size = 10
//
//  tag {
//    key                 = "Name"
//    value               = "terraform-asg-example"
//    propagate_at_launch = true
//  }
//}
//
//data "aws_subnet_ids" "default" {
//  vpc_id = data.aws_vpc.default.id
//}
//
//resource "aws_security_group" "instance" {
//  name = "terraform-example-instance"
//  ingress {
//    from_port = var.server_port
//    to_port = var.server_port
//    protocol = "tcp"
//    cidr_blocks = ["0.0.0.0/0"]
//  }
//}
//
//variable "server_port" {
//  description = "HTTP Port"
//  type = number
//  default = 8080
//}
//
//output "public_ip" {
//  value       = aws_instance.example.public_ip
//  description = "The public IP of the Instance"
//}