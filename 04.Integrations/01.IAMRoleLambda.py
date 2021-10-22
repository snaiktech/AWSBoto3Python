import boto3
import json

iam=boto3.client("iam")

# policyLambdaProject={
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "",
#             "Effect": "Allow",
#             "Principal":{
#                 "Service":"lambda.amazonaws.com"
#             },
#             "Action": "sts:assumeRole"
#         }
#     ]
# }

# policyLambdaProject={
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "VisualEditor0",
#             "Effect": "Allow",
#             "Principal":{
#                 "Service":"lambda.amazonaws.com"
#             },
#             "Action": "*"
#         }
#     ]
# }
policyLambdaProject={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}


response=iam.create_role(
    RoleName="rlmujahedv1",
    AssumeRolePolicyDocument=json.dumps(policyLambdaProject)
)
