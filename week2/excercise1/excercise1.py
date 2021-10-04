import boto3
from csv import DictReader

dynamodb = boto3.resource("dynamodb")


def create_dynamo_table(table_name):
    
    result = dynamodb.create_table(
        TableName="dragons",
        KeySchema=[
            {"AttributeName":"dragon_name", "KeyType":"HASH"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "dragon_name", "AttributeType": "S"}
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    print("Table status = " + result.table_status)
    
    
def load_data(table_name):
    
    with open("./data.csv") as file:
        csv_reader = DictReader(file)
        table = dynamodb.Table(table_name)
        
        for row in csv_reader:
            table.put_item(Item=dict(row))
            
    print("Items saved")

if __name__ == "__main__":
    table_name = "dragons"
    load_data(table_name)
