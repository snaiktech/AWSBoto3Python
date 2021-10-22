import boto3

client=boto3.client("rds")

response=client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="mujahed-db-instance-01",
    Engine="MySQL",
    MasterUsername="admin01",
    MasterUserPassword="test123pwd0021"
);

print(response)