import boto3
import os

bucket_name = "mgil-dragon-website"
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
content_types = {
    "html": "text/html",
    "js": "application/javascript",
    "png": "image/png",
    "css": "text/css"
}

def upload_file(path="./resources"):
    print(f"Folder: {path}")
    for resource in os.listdir(path):

        full_path = os.path.join(path, resource)
        
        if os.path.isdir(full_path):
            upload_file(full_path)
            continue
        
        with open(full_path, 'rb') as data:
            print(f"\t-{full_path}")
            parts = resource.split(".")
            ext = parts[len(parts) - 1]
            bucket.put_object(Key=resource, Body=data, ContentType=content_types.get(ext))

if __name__ == "__main__":
    print("Uploading file...")
    upload_file()
    print("Done")