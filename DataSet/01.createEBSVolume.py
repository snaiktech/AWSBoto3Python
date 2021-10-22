import boto3
AWS_REGION="us-east-2"

ec2_client=boto3.client("ec2",region_name=AWS_REGION)

new_volume=ec2_client.create_volume(
    AvailabilityZone=f'{AWS_REGION}c',
    Size=10,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'mujahedvolume1'
                }
            ]
        }
    ]
)

print(f"Created volume ID: {new_volume['VolumeId']}")

#vol-024820347f43c53c1