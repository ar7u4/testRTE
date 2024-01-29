Procedure Notes for Deploy Lambda Functions and Layers Workflow:
Trigger:

This workflow is triggered on each push to the main branch.
Job: deploy-functions-and-layers:

The job runs on an ubuntu-latest environment.
Steps:

Step 1: Checkout Repository

Uses GitHub Actions' actions/checkout@v3 to fetch the repository code.
Step 2: Configure AWS Credentials

Utilizes the aws-actions/configure-aws-credentials@v4 action to set up AWS credentials.
Requires AWS access key, secret access key, and region stored as GitHub secrets.
Step 3: Install jq

Installs the jq tool, a lightweight and flexible command-line JSON processor.
Step 4: Get Changed Files

Uses the tj-actions/changed-files@v42 action to identify the files changed in the push.
Step 5: Deploy Lambda Functions

Checks if there are changes in the Lambda_functions/ directory.
If changes are detected, it iterates over modified folders within Lambda_functions/.
For each Lambda function:
Extracts the function name from the folder structure.
Zips the function code.
Updates the Lambda function code using the ZIP file.
Publishes a new version of the Lambda function.
Updates the "latest" alias to point to the new version.
Step 6: Deploy Lambda Layer

Checks if there are changes in the AWS_Lambda_layer/ directory.
If changes are detected, it identifies the most recently pushed ZIP file.
Publishes a new version of the Lambda layer using the ZIP file.
Outputs the LayerVersionArn of the newly published layer.
Updates all Lambda functions with the new layer version.
