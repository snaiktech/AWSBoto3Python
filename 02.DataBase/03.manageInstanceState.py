import boto3

client=boto3.client("rds")

response = client.stop_db_instance(
    DBInstanceIdentifier='mujahed-db-instance-01',
    DBSnapshotIdentifier='stop-snapshot001'
)


response = client.start_db_instance(
    DBInstanceIdentifier='mujahed-db-instance-01'
)

response = client.modify_db_instance(
    DBInstanceIdentifier='mujahed-db-instance-01',
    MasterUserPassword="NEW PASSWORD"
)


response = client.create_db_instance_read_replica(
    DBInstanceIdentifier='mujahed-db-instance-01',
    PublicyAccessible=True,
    DBInstanceClass="db.t2.micro",
    SourceDBInstanceIdentifier="mujahed-db-instance-01-read-replica",
    StorageType="gp2",
    Tags=[
        {
            "Key":"ReadreplicaNumber",
            "Value":"readreplica001"
        }
    ]
)