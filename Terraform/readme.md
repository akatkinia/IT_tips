# AWS

## EC2

### Environment variables

  Environment variables for terraform (if I don't want to keep my settings in a file in prompt text format):
export AWS_ACCESS_KEY_ID=""  
export AWS_SECRET_ACCESS_KEY=""  
export AWS_DEFAULT_REGION=""  
  
  It is the same if I write description of a provider (AWS) setup in the tf file. For example:  
```
provider "aws" {  
  access_key = "" # your AWS access key  
  secret_key = "" # your AWS secret key  
  region     = "eu-central-1"  
}
```

And in this case we can describe our provider simply short like this:
<code>provider "aws" {}</code>

### Examples of tf configuration

* To make a resource of Ubuntu vm instance ("aws_instance") in t3.micro configuration (the simpliest and cheaper one) and add some tags:  
```
resource "aws_instance" "<ANY NAME (for example 'My_ubuntu'>" {
  ami           = "ami-090f10efc254eaf55"  # Ubuntu AMI
  instance_type = "t3.micro"  
  
  tags = {
    TAG1 = "VALUE1"
	TAG2 = "VALUE2"
  }
}
```

/* # begin comment
* To make an instance of vm and attach it with security group resource:
```
resource "aws_instance" "<ANY NAME (for example 'My_ubuntu'>" {
  ami                    = "ami-090f10efc254eaf55"  # Ubuntu AMI
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.my_webserver.id]  # this variable is a dependecy to security group
  user_data              = <<EOF
#!/bin/bash
yum -y update
yum -y install httpd
myip = 'curl http://169.254.169.254/latest/meta-data/local-ipv4'
echo "<h2>WebServer with IP: $myip</h2><br>Build by Terraform!" > /var/www/html/index.html
sudo service httpd start
chkconfig httpd on  
EOF # BUT also instead of writing the script into the main tf file we can index it from an external file by using "file" function. For example: user_data = file("user_data.sh")
}
*/ # end of comment

resouse "aws_security_group" "my_webserver" {
  name        = "WebServer Security Group"
  description = "My first SecurityGroup"
  
  ingress {
    from_port   = 80
	to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]	
  }

  ingress {
    from_port   = 443
	to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]	
  }
  
  # Outcomming traffic - any port, any ip
  engress {
    from_port   = 0
	to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]	  
  }
```



### Some notes

Web-resource with description of region codes: https://awsregion.info  
Types of EC2 instances:  
* t3.micro

Types of EC2 resources:
* aws_instance # virtual machine
* aws_security_group # something like firewall settings for our resources (we should to attach our security group to our instance by using "vpc_security_group_ids" key with list values that can be id of our security group or it may be playceholder like "aws_security_group.my_webserver.id"). Settings are include ingress and egress (from_port; to_port; protocol; cidr_blocks; prefix_list_ids) options