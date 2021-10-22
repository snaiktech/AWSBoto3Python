import boto3

client = boto3.client('rds')
response = client.delete_db_instance(
    DBInstanceIdentifier='mujahed-db-instance-01',
    SkipFinalSnapshot=True
)
print(response)