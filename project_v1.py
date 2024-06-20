"""import requests
url = "https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.activities.list?"
response = requests.post(url)
print(response.json())"""

# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'enter key here'
# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
# Request body
request = youtube.search().list(
        part="id,snippet",
        type='video',
        q="Spider-Man",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1
)
# Request execution
response = request.execute()
print(response)