import time
from datetime import datetime   
from flask import Flask, jsonify
from flask_cors import CORS
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.storage.blob import BlobServiceClient
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)
CORS(app)

# Config values, will be moved to config file
key_vault_name='BillTestKeyVault'
key_valut_uri = f"https://{key_vault_name}.vault.azure.net"
subscription_id_key = "subscriptionId"  # for retrieving subscription_id from Key Vault
resource_group_name_key = "resourceGroupName"   # for retrieving resource_group_name from Key Vault
account_url = "https://billteststorage238.blob.core.windows.net/"

# Azure specific
credential=DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_valut_uri, credential=credential)
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
container_client = blob_service_client.get_container_client("ssms-server")

def __azure_values():
    subscription_id = secret_client.get_secret(subscription_id_key).value
    computer_client = ComputeManagementClient(credential=credential, subscription_id=subscription_id)
    resource_group_name = secret_client.get_secret(resource_group_name_key).value
    
    return computer_client, resource_group_name

# Will be moved to a customized Logging class
def __log(message):
    blob_client = container_client.get_blob_client(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}: ' +
                                                   'Information')
    blob_client.upload_blob(message)

@app.route('/')
def default():
    return jsonify(message="Flask REST API server on AKS Ingress works")

@app.route('/test', methods=['GET'])
def test():
    __log('test accessing Azure Key Vault')
    _, resource_group = __azure_values()
    
    if resource_group is not None and len(resource_group) > 0:
        return jsonify(message="Secret access test success")
    else:
        return jsonify(message="Secret access test fail")
      
if __name__ == '__main__':
    app.run()
