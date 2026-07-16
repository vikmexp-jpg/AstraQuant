from dotenv import load_dotenv
import os

import upstox_client
from upstox_client.rest import ApiException


load_dotenv()

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise RuntimeError(
        "UPSTOX_ACCESS_TOKEN not found in .env"
    )

configuration = upstox_client.Configuration()

configuration.access_token = ACCESS_TOKEN

client = upstox_client.UserApi(
    upstox_client.ApiClient(configuration)
)

try:
    response = client.get_profile(api_version="2.0")

    print("=" * 60)
    print("Connected to Upstox successfully")
    print("=" * 60)
    print(response)

except ApiException as error:
    print("Connection failed")
    print(error)