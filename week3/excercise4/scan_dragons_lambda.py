import boto3
from boto3.dynamodb.conditions import Key

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("dragons")
    dragon_name = event["dragon_name_str"]
    response = table.scan(FilterExpression=Key("dragon_name").eq(dragon_name))
    return response.get("Items")