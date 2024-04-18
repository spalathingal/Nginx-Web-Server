import os
from google.cloud import compute_v1

# Path to the service account key file
KEY_FILE_PATH = "/keys/service_account_key.json"

# Function to authenticate using service account key file
def authenticate():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/nginx-web-server-d5697f50d28f.json"

# Function to create a Compute Engine instance with Nginx
def create_instance(project_id, zone):
    compute_client = compute_v1.InstancesClient()

    instance_name = "nginx-instance"
    machine_type = f"zones/{zone}/machineTypes/f1-micro"
    image_family = "debian-10"
    startup_script = open("startup-script.sh", "r").read()

    config = {
        "name": instance_name,
        "machine_type": machine_type,
        "disks": [
            {
                "boot": True,
                "auto_delete": True,
                "initialize_params": {
                    "source_image": f"projects/debian-cloud/global/images/family/{image_family}"
                }
            }
        ],
        "network_interfaces": [
            {
                "network": "global/networks/default",
                "access_configs": [
                    {
                        "type_": "ONE_TO_ONE_NAT",
                        "name": "External NAT"
                    }
                ]
            }
        ],
        "metadata": {
            "items": [
                {
                    "key": "startup-script",
                    "value": startup_script
                }
            ]
        }
    }
    
    # Create an InsertInstanceRequest object
    request = compute_v1.InsertInstanceRequest(
    project=project_id,
    zone=zone,
    instance_resource=config
    )   

    operation = compute_client.insert(request=request)
    print(f"Creating instance {instance_name}...")
    print(operation)

    instance = compute_client.get(project=project_id, zone=zone, instance=instance_name)

    # Retrieve the external IP address from the network interface
    info = instance.self_link

    print(f"Instance {instance_name} created.")
    print(f"Link: \n{info}")

if __name__ == "__main__":
    project_id = "nginx-web-server"
    zone = "us-east1-b"

    authenticate()
    create_instance(project_id, zone)
