import boto3
import json

dragon_table_data = {
    "dragon_bonus_attack": "../resources/dragon_bonus_attack.json",
    "dragon_current_power": "../resources/dragon_current_power.json",
    "dragon_family": "../resources/dragon_family.json",
    "dragon_stats": "../resources/dragon_stats.json"
}

if __name__ == "__main__":
    dynamodb = boto3.resource("dynamodb")
    print("Inserting data into Dynamo tables...")
    for table_name, file in dragon_table_data.items():
        table = dynamodb.Table(table_name)
        with open(file) as f:
            loaded_data = json.load(f)

            with table.batch_writer() as batch:
                print(f"Inserting items for table '{table_name}'...", end="")
                for item in loaded_data:
                    batch.put_item(Item=item)
                print("Done")
    print("Done")