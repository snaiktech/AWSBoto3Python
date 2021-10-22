import boto3

AWS_REGION = "us-east-2"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

volume = ec2_resource.Volume('vol-024820347f43c53c1')

if volume.state == "available":
    volume.delete()
    print(f'Volume successfully deleted')
else:
    print(f"Can't delete volume attached to EC2 instance")