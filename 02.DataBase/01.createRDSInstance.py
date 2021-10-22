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

# mysql -h mujahed-db-instance-01.cnfs3veczxfo.ap-south-1.rds.amazonaws.com -u admin01 -p