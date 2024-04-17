# Python & GCP Exercise: Deploying an Nginx Web Server

## Helpful links:

- https://cloud.google.com/python/docs/reference/compute/latest
- https://cloud.google.com/docs/get-started

## Objective

Utilize Python and the Google Cloud Client Libraries to create a virtual machine instance on Google Cloud Platform (GCP) that runs the Nginx web server, ensuring it's accessible over the internet. **Opt for the smallest possible instance type to remain within the GCP free tier**.

## Prerequisites

- Basic understanding of Python programming and Google Cloud Platform services, particularly Google Compute Engine (GCE).
- Python environment set up with access to GCP client libraries (google-cloud-compute).
- Access to a GCP account and permissions to create and manage GCE instances.
- A GCP project set up for this exercise and a service account with the necessary permissions (e.g., Compute Admin) created within it.

## Tasks

### Task 1: Environment Setup

- **Create a Python Virtual Environment**: In your project directory, set up a Python virtual environment to manage dependencies.

```
python -m venv env-name
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Google Cloud Client Libraries:

```
pip install google-cloud-compute
```

### Task 2: Prepare Your Python Script

Create a Python script named `deploy_web_server.py`. This script will perform the following actions:

- **Authentication**: Use your service account key file to authenticate API requests.
- **Define the Smallest Instance Type**: Set the instance type to `f1-micro` to stay within the free tier.
- **Create a Compute Engine Instance**: Program your script to launch a GCE instance in your specified project and zone. Ensure the instance uses a Debian or Ubuntu image and installs Nginx upon startup.
- **Output Instance Details**: Print the external IP address of the instance to the console once it's up and running.

### Task 3: Write the Python Script

- Import the necessary modules and set up authentication using the service account key file.
- Define a function to create the Compute Engine instance with the Nginx web server.
- Use the `google-cloud-compute` library to interact with the Compute Engine API.
- Ensure the startup script for the instance installs Nginx.

### Task 4: Execute Your Script and Verify the Deployment

Run Your Script:

- Access the Web Server: Use the external IP address printed by your script to navigate to the Nginx welcome page in a web browser.

### Task 5: Clean Up Resources

After you've completed the exercise, ensure to clean up your resources to avoid incurring charges:

- Modify your script or create a new one to delete the created instance and any other resources that were allocated.

## Deliverables

- **Python Script**: Submit your `deploy_web_server.py` script that automates the deployment process.
- **Execution Proof**: A screenshot showing the Nginx welcome page accessible via the external IP of the deployed instance.

## Evaluation Criteria

- **Functionality**: The script successfully creates a GCE instance and deploys Nginx, accessible externally.
- **Code Quality**: The script is well-organized, commented, and follows Python best practices.
- **Resource Efficiency**: The solution stays within the GCP free tier by using the smallest instance type and properly cleaning up resources after completion.

**Should you encounter any issues or errors, please record the details of these occurrences, along with descriptions of how you addressed them, if applicable.**
