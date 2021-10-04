import boto3

tables_definition = [
    {
        "TableName":"dragon_stats_table_one",
        "KeySchema":[
            {"AttributeName": "dragon_name_str", "KeyType": "HASH"}
        ],
        "AttributeDefinitions":[
            {"AttributeName": "dragon_name_str", "AttributeType": "S"}
        ],
        "ProvisionedThroughput":{
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    },
    {
        "TableName":"dragon_stats_table_trow",
        "KeySchema":[
            {"AttributeName": "dragon_name_str", "KeyType": "HASH"}
        ],
        "AttributeDefinitions":[
            {"AttributeName": "dragon_name_str", "AttributeType": "S"}
        ],
        "ProvisionedThroughput":{
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    },
    {
        "TableName":"dragon_bonus_attack_table",
        "KeySchema":[
            {"AttributeName": "breath_attack", "KeyType": "HASH"},
            {"AttributeName": "range", "KeyType":"RANGE"}
         ],
         "AttributeDefinitions":[
             {"AttributeName": "breath_attack", "AttributeType": "S"},
             {"AttributeName": "range", "AttributeType": "N"}
         ],
         "ProvisionedThroughput":{
             "ReadCapacityUnits": 5,
             "WriteCapacityUnits": 5
         }
    },
    {
        "TableName":"dragon_family",
        "KeySchema":[
            {"AttributeName": "family", "KeyType": "HASH"}
        ],
        "AttributeDefinitions":[
            {"AttributeName": "family", "AttributeType": "S"}
        ],
        "ProvisionedThroughput":{
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    }
]

dynamodb = boto3.resource("dynamodb")

def create_tables():
    print("Creating tables...")
    for t in tables_definition:
        res = dynamodb.create_table(**t)
        print(f"{t['TableName']} -> {res.table_status}")
    print("Done")
    
if __name__ == "__main__":
    create_tables()