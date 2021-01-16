provider "kubernetes" {
  config_context_cluster   = "minikube"
}

resource "kubernetes_namespace" "minikube-namespace" {
  metadata {
        name = "bobo-terraform-namespace"
  }
}

provider "helm" {
  kubernetes {
        config_context_cluster   = "minikube"
       
  }
}

resource "helm_release" "local" {
  name          = "buildachart"
  chart         = "./buildachart"
}