import boto3


dynamodb=boto3.resource("dynamodb")

table =dynamodb.create_table(
    TableName="MujahedEmployees",
    KeySchema=[
        {
            "AttributeName":"Name",
            "KeyType":"HASH"
        },
        {
            "AttributeName":"Email",
            "KeyType":"RANGE"
        }],
    AttributeDefinitions=[
        {
            "AttributeName":"Name",
            "AttributeType":"S"
        },
        {
            "AttributeName":"Email",
            "AttributeType":"S"
        }
    ],
    ProvisionedThroughput={
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
            }
)

print(table)