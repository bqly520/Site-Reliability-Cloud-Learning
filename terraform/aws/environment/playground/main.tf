terraform {
  backend "remote" {
    organization = "bobo"

    workspaces {
      name = "Bobo-Workspace"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}

resource "aws_instance" "bobo_vm" {
  ami           = var.amis[var.region]
  instance_type = "t2.micro"
  key_name      = "bobo_keyngdom"

  tags = {
    Name = "bobo_vm_only"
    owner = "bobo"
  }

  provisioner "local-exec" {
    command = "echo \"bobo is here\" "
  }
}

resource "aws_instance" "bobo_vm2" {
  ami           = var.amis[var.region]
  instance_type = "t2.micro"
  key_name      = "bobo_keyngdom"

  tags = {
    Name = "bobo_vm2_only"
    owner = "bobo"
  }

  provisioner "local-exec" {
    command = "echo \"bobo2 is here\" "
  }
}

resource "aws_eip" "ip" {
    vpc = true
    instance = aws_instance.bobo_vm.id
}

resource "aws_eip" "ip2" {
    vpc = true
    instance = aws_instance.bobo_vm2.id
}
