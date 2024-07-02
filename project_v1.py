import requests
import sqlalchemy as db
import pandas as pd
import googleapiclient.discovery
import pprint

# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyDuUFKGfNPkEOJaD3hqIdSvpe7GzMnkfuk'

# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)


class Project:

    def fetch_youtube_data():
        # Request body
        request = youtube.search().list(
                part="id,snippet",
                type='video',
                q="Spider-Man",
                videoDuration='short',
                videoDefinition='high',
                maxResults=1)
        # Request execution
        response = request.execute()
        response2 = {k: v for k, v in response.items() if k != "items"}
        pprint.pp(response2)
        return response2

    def save_to_database(data):
        dataframe = pd.DataFrame.from_dict(data)
        engine = db.create_engine('sqlite:///data_base_name.db')
        dataframe.to_sql(
                'table_name', con=engine, if_exists='replace', index=False)
        with engine.connect() as connection:
            query_result = connection.execute(
                db.text("SELECT * FROM table_name;")).fetchall()
            return pd.DataFrame(query_result)
