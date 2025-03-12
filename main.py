import json
import os

from requests import get
from shutil import rmtree, move

from auth import get_auth_header, get_token

###########################################################

# TODO:

###########################################################


def get_user_id(token):
  url = "https://api.spotify.com/v1/me"
  headers = get_auth_header(token)

  result = get(url, headers=headers)
  json_result = json.loads(result.content)
  user_id = json_result["id"]

  return user_id


def get_user_playlists(token: str):
  url = "https://api.spotify.com/v1/me/playlists?limit=50"
  headers = get_auth_header(token)

  result = get(url, headers=headers)
  json_result = json.loads(result.content)

  return json_result


def check_playlist_owner(playlists, user_id):
  data = "{ }"

  for playlist in playlists["items"]:
    playlist_url = playlist["external_urls"]["spotify"]
    if playlist["owner"]["id"] == user_id:
      temp = data.split()
      new_entry = f' , "{playlist["name"]}": {{ "id": "{playlist["id"]}", "url": "{playlist_url}"}}'

      res = temp[:-1] + [new_entry] + temp[-1:]
      res = " ".join(res)
      data = res

  temp = data.split()
  del temp[1]
  res = " ".join(temp)
  user_playlists = res

  return user_playlists


def make_playlist_folders():
  for idx, playlist in enumerate(owned_playlists):
    norm_name = f"{playlist}"
    playlists_dir = f"dump_sorter/temp/playlists/{norm_name}"
    os.makedirs(playlists_dir, exist_ok = True)
    with open(f"{playlists_dir}/Playlist Url", "w") as f:
      f.write(owned_playlists[playlist]["url"])
      f.close()


def get_dump_playlist():
  input("Select playlist to be sorted... \nPress enter to continue")
  os.system("nvim dump_sorter/temp/playlists && clear")

  temp = os.listdir("dump_sorter/temp")
  temp.remove("playlists")
  dump_playlist = temp[0]
  move(f"dump_sorter/temp/{str(dump_playlist)}", "dump_sorter/dump")
  return dump_playlist


def scrape_dump_playlist(dump_playlist, token): ...


if __name__ == "__main__":
  rmtree("dump_sorter")
  os.system("clear")

  token = get_token()
  user_id = get_user_id(token)

  playlists = get_user_playlists(token)
  owned_playlists = json.loads(check_playlist_owner(playlists, user_id))

  make_playlist_folders()
  dump_playlist = get_dump_playlist()

  input("Select playlists to be sorted into...\nPress enter to continue")
  os.system("nvim dump_sorter/temp/playlists && clear")
  rmtree("dump_sorter/temp/playlists")

  selected_playlists = os.listdir("dump_sorter/temp")

  print(dump_playlist, "Dump")
  for i in range(len(selected_playlists)):
    print("Selection " + str(i + 1), selected_playlists[i])

  rmtree("dump_sorter/temp")

