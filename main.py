import googleapiclient.discovery
from json import loads
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyD_z5CcnRqDRmf5yXIOev2aXRhxvFvB5Ag'
# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
# Request body
request = youtube.search().list(
    part="snippet",
    type='video',
    q="why scorpions glow in night",
    maxResults=4,
    videoDuration='short'
)
# Request execution
response = request.execute()
x = []
print(response)
for y in response["items"]:
    x.append(f"https://www.youtube.com/embed/{y['id']['videoId']}")
print(x)
