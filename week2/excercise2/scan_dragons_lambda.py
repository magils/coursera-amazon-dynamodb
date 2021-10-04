import boto3

def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("dragons")
    result = table.scan()
    return result.get("Items")

    