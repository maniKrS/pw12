from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)

def youtube_scrape():
    url = 'https://www.youtube.com/feed/trending'
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        get_video = [video.get_text() for video in soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')]
        return get_video

@app.route('/youtube')
def display_trending_videos():
    trending_videos = youtube_scrape()
    return render_template('index.html', videos=trending_videos)

if __name__ == '__main__':
    app.run(debug=True)
