# Общее  
**terraform.tfstate** - хранит связь между реальными объектами инфраструктуры и экземплярами ресурсов, объявленными в конфигурации. Важно, что в этом файле также хранятся и секретные данные в открытом виде, поэтому важно добавлять его в gitignore. Для коллективной работы используется **remote state**.   
  
Полная конфигурация проекта состоит из **Root Module** и вызываемых им **Child Modules**.
**Root module** - директория, которая сожержит файлы конфигурации Terraform с расширением .tf, и из которой Terraform запускается для создания и управления инфраструктурой. В этой директории могут находиться несколько файлов конфигурации, каждый из которых определяет ресурсы и провайдеры для управления инфраструктурой. Это позволяет удобно организовать код и разделять ресурсы по файлам. Сам Terraform воспринимает все файлы tf этой директории как один единый файл. Вложенные директории в Root Module Terraform игнорируются и не будут использоваться в создании инфраструктуры, если их не явно подключить в качестве дочерних модулей.  
Файлы:  
- *.tf - файлы конфигурации
- terraform.tfvars - автоматически загружаемый файл, в котором можно задавать значения переменных
- *auto.tfvars - то же, что и terraform.tfvars, позволяет именовать файлы с переменными (в том числе секретными). Используется для разделения большого файла с переменными (например, db.auto.tfvars)
- .terraform.lock.hcl - создаётся при инициализации проекта. Фиксирует версии используемых провайдеров и зависимостей проекта
- terraform.tfstate - файл в котором сохраняется текущее состояние инфраструктуры проекта
- каталог .terraform - локальный архив скачанных providers и Child. В нём хранятся секретные данные, поэтому он должен вноситься в gitignore.  
**Child moduel** -  
  
## Mirror registry  
Для работы Terraform в ограниченных сетевых условиях, может потребоваться настройка частного зеркала для Terraform Registry.  
Зеркала могут содержать копию репозитория Hashicorp, а также дополнительные модули и провайдеры, которые используются внутри организации.  
Для использования зеркала необходимо отредактировать файл конфигурации:  
- Для windows: ```%APPDATA%/terraform.rc```
- Для linux: ```~/.terraformrc``` 
Инструкция: https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart#configure-provider  
https://developer.hashicorp.com/terraform/internals/provider-network-mirror-protocol  
  
## Пример кода Terraform:  
```shell
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
    aws = {
      source = "hashicorp/aws"
      version = "-> 2.0"
    }
  }
  required version = ">= 0.13"
}
```  
  
### Блок provider:  
```shell
provider "yandex" {                  # тип provider, лейбел "yandex"
    version   = "~> 0.85"
    token     = "t1.7eueaZ567..."
    cloud_id  = "b2g78mf..."
    folder_id = "b2g6vgh..."
    zone      = "ru-central1-a"
}
```  
Terraform содержит в себе встроенные провайдеры. Они не нуждаются в конфигурации и загрузке.
Важно, что любой сторонний провайдер должен быть предварительно загружен из репозитория.    
  
### Блок resource:  
Создает объекты, поддерживаемые provider - сети, виртуальные машины, базы данных, dns-записи, пароли, файлы и т.п.  
Описываются блоком resouce ```"type" "name" {...}```, содержащим:  
- тип объекта из классификатора provider
- уникальное имя в текущем проекте
- аргументы для создания ресурса
Например:  
```shell
resource "random_passwod" "uniq_name" {
  length = 16
}
```  
Для дальнейшего использования значения, необходимо обратиться к ресурсу в формате:  
```type.name.параметр``` или же в нашем случае: ```random_paaword.uniq_name.result```  
  
### Блок datasource:  
Считывает параметры уже существующих объектов инфраструктуры, поддерживаемых provider.  
Описываются блоком кода data ```"type" "name" {...}```, содержащим:  
- тип объекта из классификатора provider
- уникальное имя в текущем проекте
- фильтр-запрос  
Например:  
```shell
data "local_file" "version" {
  filename = "/proc/version"
}
```  
В примере считывается дата-ресурс "файл". Для дальнейшего использования всех его параметров необходимо обратиться к дата-ресурсу в формате: ```data.type.name```:
```data.local_file.version```  
  
Или отфильтровать конкретный параметр в формате ```data.type.name.параметр```:  
```data.local_file.version.content```  
  
## Базовые команды  
- ```terraform init``` - скачивание зависимостей
- ```terraform validate``` - проверка синтаксиса конфигурации и доступности зависимостей
- ```terraform plan``` - terraform validate + отображение планируемых изменений в инфраструктуре (DRY RUN)
- ```terraform apply``` - terraform plan + внесение изменений в инфраструктуру (если они есть)
- ```terraform destroy``` - уничтожение всех ранее созданных Terraform объектов инфраструктуры
- ```terraform fmt``` - встроенное автоформатирование текста в конфигурации проекта  
    




















---    
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

