import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

if not all([AIRTABLE_PAT, BASE_ID, TABLE_NAME]):
    raise ValueError("Missing Airtable environment variables")

url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

headers = {
    "Authorization": f"Bearer {AIRTABLE_PAT}",
    "Content-Type": "application/json"
}

def create_test_record():
    data = {
        "records": [
            {
                "fields": {
                    "Name": "Test Entry"
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ Record created successfully")
        print(response.json())
    else:
        print("❌ Failed to create record")
        print(response.status_code, response.text)


if __name__ == "__main__":
    create_test_record()