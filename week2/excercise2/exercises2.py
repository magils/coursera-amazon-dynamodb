from boto3 import resource
from csv import DictReader
import time

dynamo = resource("dynamodb")
table_name = "dragons"

def create_table():
    print("Creating table...")
    try:
        dynamo.create_table(
        TableName=table_name,
        KeySchema=[
            {
                "AttributeName": "dragon_name",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            { 
                "AttributeName": "dragon_name",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    #TODO: Investigate the exception to handle this
    except Exception as e:
        print("Table is already created")
        # raise e


def insert_items():
    print("Inserting items...")
    table = dynamo.Table(table_name)
    
    with open("./data.csv") as file:
        csv_file = DictReader(file)

        for row in csv_file:
            table.put_item(
                Item=dict(row)
            )
    print("Items inserted")


if __name__ == "__main__":
    create_table()
    print("Waiting table creation...")
    time.sleep(5)
    insert_items()