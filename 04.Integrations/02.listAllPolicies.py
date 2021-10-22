import boto3
iam=boto3.resource("iam")
policies=iam.policies.all()
for p in policies:
    print(f" Policy:  {p.policy_name}  ")