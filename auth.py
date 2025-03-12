import base64
import json
import os

from dotenv import load_dotenv #type: ignore
from requests import post #type: ignore

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("REFRESH_TOKEN")

def get_token():
  auth_string = client_id + ":" + client_secret
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded",
  }
  data = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
  }
  result = post(url, headers=headers, data=data)
  json_result = json.loads(result.content)
  scope_token = json_result["access_token"]
  return scope_token

def get_auth_header(token):
  return {"Authorization": "Bearer " + token}
