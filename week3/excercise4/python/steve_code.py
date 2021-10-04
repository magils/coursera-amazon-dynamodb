import sys
import boto3
from boto3.dynamodb.conditions import Key, Attr
from pprint import pprint

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("dragon_stats")

def find_one_dragon(name):
    response = table.query(KeyConditionExpression=Key("dragon_name").eq(name))
    return response["Items"]

def scan_table():
    scan_kwargs = {
        "ProjectionExpression": "dragon_name, #f, protection, damage, description",
        "ExpressionAttributeNames": {"#f": "family"}
    }
    response = table.scan(**scan_kwargs)
    done = False
    start_key = None
    data = []

    while not done:
        if start_key:
            scan_kwargs["ExclusiveStartKey"] = start_key
        response = table.scan(**scan_kwargs)
        data.extend(response.get("Items", []))
        start_key = response.get('LastEvaluatedKey')
        done = start_key is None
    return data

def handler(event, context):
    dragon_name = event.get("dragon_name_str")
    if not dragon_name or dragon_name == "All":
        return scan_table()
    else:
        return find_one_dragon(dragon_name)

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        response = scan_table()
        pprint(response)
        sys.exit(0)

    name = args[1]
    response = find_one_dragon(name)
    pprint(response)