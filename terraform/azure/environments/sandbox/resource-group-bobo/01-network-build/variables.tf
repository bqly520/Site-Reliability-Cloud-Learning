variable "rg_name" {
  type = string
  default = "resource-group-bobo"
}

variable "location" {
  type = string
  default = "West US 2"
}

variable "vnet_name" {
  type = string
  default = "vnet-bobo"
}

variable "subnet_name" {
  type = string
  default = "subnet-bobo"
}

variable "address_space" {
  type = string
  default = "10.1.1.1/28"
}