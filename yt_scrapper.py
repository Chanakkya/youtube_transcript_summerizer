import googleapiclient.discovery
from json import loads
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyD_z5CcnRqDRmf5yXIOev2aXRhxvFvB5Ag'

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

def scrap_similar_shorts(video_url):

    video_id = video_url.split("v=")[-1]
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    video_title = response["items"][0]["snippet"]["title"]

    request = youtube.search().list(
        part="snippet",
        type='video',
        q=video_title,
        maxResults=4,
        videoDuration='short'
    )
    response = request.execute()
    shorts = []
    for y in response["items"]:
        shorts.append(y['id']['videoId'])

    return video_title, shorts

# print(scrap_similar_shorts("https://www.youtube.com/watch?v=f-Nr2z5X7Rs"))
