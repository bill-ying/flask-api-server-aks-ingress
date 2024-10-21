# flask-api-server-aks-ingress

az login
az aks get-credentials --resource-group <resource_group_name> --name <AKS_cluster_name> 
docker build -t <ACR_name>.azurecr.io/flask-api-server-aks-ingress
docker tag flask-api-server-aks-ingress:latest <ACR_name>.azurecr.io/flask-api-server-aks-ingress:latest
sudo docker push <ACR_name>.azurecr.io/flask-api-server-aks-ingress:latest
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml