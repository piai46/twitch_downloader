import keys, requests, shutil

def download_clip(url):
    clip_info = get_info(url)
    video_id = clip_info['data'][0]['id']
    clip_url = clip_info['data'][0]['thumbnail_url']
    url_to_download = clip_url.split('-preview', 1)[0] + '.mp4'
    print('Downloading clip... ', end='')
    try:
        with requests.get(url_to_download, stream=True) as response:
            with open(f'{video_id}.mp4', 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        print('Download success!')
    except Exception as error:
        print(error)
        pass

def get_info(url):
    try:
        clip_id = url.split('/')[-1]
        url = 'https://api.twitch.tv/helix/clips?id=' + clip_id
        headers = {
            'Client-ID':keys.CLIENT_ID,
            'Authorization':f'Bearer {keys.ACCESS_TOKEN}',
            "Accept":"application/vnd.twitchtv.v5+json"
        }
        r = requests.get(url, headers=headers)
        return r.json()
    except Exception as error:
        print(error)
        exit()

def get_new_access_token():
    try:
        url = "https://id.twitch.tv/oauth2/token"
    except Exception as error:
        print(error)
        exit()
    payload = {"client_id": keys.CLIENT_ID, "client_secret": keys.CLIENT_SECRET, "grant_type": "client_credentials"}
    headers = {'Client-ID':keys.CLIENT_ID}
    resp = requests.post(url, params=payload, headers=headers)
    return resp.json()['access_token']

if __name__ == '__main__':
    url = 'https://www.twitch.tv/gafallen/clip/NicePhilanthropicHedgehogFreakinStinkin'
    download_clip(url)