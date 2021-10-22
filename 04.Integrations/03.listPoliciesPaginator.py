import boto3
iam=boto3.client("iam")

response=iam.list_policies(
    Scope="Local"
)

paginator=iam.get_paginator("list_policies")

for page in paginator.paginate():
    for p in page["Policies"]:
        print(f"- { p['PolicyName'] }")