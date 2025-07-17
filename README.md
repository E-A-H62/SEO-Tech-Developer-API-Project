# SEO Tech Developer API Project

---

## 🚀 Overview

The **SEO-Tech-Developer-API-Project** is a Python-based web application using the **Flask** web framework. The application fetches data from the **YouTube Data API v3** to retrieve detailed information about YouTube videos, stores this information in a database, and displays it via a web interface.

This project demonstrates:
- Integrating external APIs into web applications.
- Handling and storing API responses in a database.
- Web development with Flask.
- Working with YouTube API to gather and process video data.

---

## ✨ Key Features

- **YouTube API Integration**:  
  Connects to YouTube's API to fetch video details such as titles, descriptions, views, etc.

- **Database Integration**:  
  Saves fetched data from the YouTube API into a local database for easy retrieval and efficient querying.

- **Flask Web Application**:  
  Built using the Flask framework, the app serves the YouTube data on a user-friendly web page.

- **Dynamic Content Rendering**:  
  Displays the data fetched from YouTube and saved in the database dynamically through Flask's templating engine.

- **Data Management**:  
  The data is stored and retrieved using Python’s data manipulation libraries, ensuring fast querying and manipulation.

---

## 🧰 Technologies Used

- **Flask**: A micro web framework for Python, used for building the web application.
- **Python**: The primary programming language used for the project.
- **YouTube Data API v3**: Fetches video-related data from YouTube.

---

**Setup**
* Install the YouTube Python library
  * https://pypi.org/project/python-youtube/
* Install the Google API Python Client library
  `pip install google-api-python-client`
* Get the authentication setup for the YouTube API
  * https://developers.google.com/youtube/v3/guides/implementation/videos

**Running the Code**
* Make sure to use a valid API key when running the code

**Overview of the Code**
* The included code uses the YouTube Data API v3 to request information from YouTube
* It lists information regarding a specific video
  * The requested data is parsed with JSON and put into a separate dataframe
