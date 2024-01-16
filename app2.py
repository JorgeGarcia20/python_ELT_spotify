from cnf import CLIENT_ID, CLIENT_SECRET
from requests import post, get
import base64
import json
from datetime import datetime, timedelta


def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def search_for_artist(token, artist_name):
    artist_name = artist_name.replace(" ", "+")

    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)

    query = f"?q={artist_name}&type=artist&offset=0&limit=1"
    query_url = url + query
    
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        return None
    
    return json_result[0]


def get_top_artists(token, offset=20, limit=20):
    url = "https://api.spotify.com/v1/me/top/artists"
    # "https://api.spotify.com/v1/me/top/artists?limit=20&offset=20"
    header = get_auth_header(token)

    query = f"?limit={limit}&offset={offset}"
    # query_url = f"{url}{query}"
    query_url = url + query

    # result = get(query_url, headers=header)
    result = get(url, headers=header)
    # print(result)
    json_result = json.loads(result.content)["items"]
    print(json_result)


def get_recently_played(token, date):
    url = "https://api.spotify.com/v1/me/player/recently-played"
    header = get_auth_header(token)
    ds = int(date.timestamp()) * 1000

    query = f"?before={ds}"
    query_url = f"{url}{query}"

    result = get(query_url, headers=header)
    json_result = json.loads(result.content)
    print(json_result)


if __name__ == '__main__':
    my_token = get_token()
    print(my_token)
    
    # result = search_for_artist(my_token, "led zeppeline")
    # print(result.keys())
    # print(result["name"])
    # print(result["id"])
    # print(result["genres"])

    # print(get_top_artists(my_token))
    # top_artists_result = get_top_artists(my_token)

    # date = datetime.today() - timedelta(days=1)

    # get_recently_played(my_token, date)

