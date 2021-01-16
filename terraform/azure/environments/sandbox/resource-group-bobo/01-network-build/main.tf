provider "azurerm" {
  # whilst the `version` attribute is optional, we recommend pinning to a given version of the Provider
  version = "=2.0.0"
  features {}
}

module networks {
  source = "../../../../modules/networks"
  rg_name = ""
  location = ""
  vnet_name = ""
  subnet_name = ""
  address_space = ""
}