from flask import Flask, render_template
from project_v1 import DEVELOPER_KEY, Project

app = Flask(__name__)


@app.route('/')
def home():
    # Fetch data from YouTube API
    youtube_data = Project.fetch_youtube_data()

    # Save response to the database and retrieve data
    db_data = Project.save_to_database(youtube_data)

    # Render the template with data
    return render_template(
        'index.html', data=youtube_data, query_result=db_data.to_dict(
            orient='records'))


app.run(debug=True, host="0.0.0.0")
