import boto3

ROLE_NAME="rl_serverless_mujahed"

iam=boto3.resource("iam")

role=iam.Role(ROLE_NAME)

role.attach_policy(
    PolicyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess"
)

print("Policy Attached...")