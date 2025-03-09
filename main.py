import json
import os

from requests import get
from shutil import rmtree

from auth import get_auth_header, get_token

def get_user_id(token):
  url = "https://api.spotify.com/v1/me"
  headers = get_auth_header(token)

  result = get(url, headers=headers)
  json_result = json.loads(result.content)
  user_id:str = json_result["id"]

  return user_id

def get_user_playlists(token:str):
  url = "https://api.spotify.com/v1/me/playlists?limit=50"
  headers = get_auth_header(token)

  result = get(url, headers=headers)
  json_result = json.loads(result.content)
  return json_result

def check_playlist_owner(playlists, user_id:str):
  users_playlists = {}
  playlist_items = playlists["items"]
  for playlist in playlist_items:
    playlist_owner = playlist["owner"]
    owner_id = f"{playlist_owner['id']}"
    if owner_id == user_id:
      playlist_url = playlist["external_urls"]
      playlist_url = playlist_url["spotify"]
      users_playlists[f"{playlist['name']}"] = playlist_url
    else:
      pass
  return users_playlists



if __name__ == "__main__":
  token = get_token()
  user_id = get_user_id(token)

  playlists = get_user_playlists(token)
  users_playlists = check_playlist_owner(playlists, user_id)

  for idx, playlist in enumerate(users_playlists):
    norm_name = f"{playlist}"
    os.makedirs(f"dump_sorter/all/{norm_name}", exist_ok = True)
    with open(f"dump_sorter/all/{norm_name}/Playlist Url", "w") as f:
      f.write(users_playlists.get(playlist))
      f.close()

  os.system("nvim dump_sorter/all")
  rmtree("dump_sorter/all")

  selected_playlists = os.listdir("dump_sorter")
