# Flask API Server on AKS

This is a proof of concept (POC) project demonstrating how to use Azure DevOps to build Docker images and deploy a Python Flask REST API server to an Azure Kubernetes Service (AKS) cluster.

# Prerequisites

- Azure subscription and resource group.
- Azure Container Registry (ACR).
- Azure Kubernetes Service (AKS) cluster.
- Azure DevOps account with project, pipeline, and service connection setup.

# Deployment Overview

Once the code is built and deployed by the provided pipelines using Azure DevOps, the following resources will be available in the Azure portal:

- A Docker image named flask-api-server in ACR.
- A workload named flask-api-server with the corresponding pod deployed to the AKS cluster.
- A service named flask-api-server-service with an external IP address.

# Accessing the Flask API Server

- The Flask REST API server can be accessed via the following URL:

- http://external-ip-address-of-flask-api-ingress

