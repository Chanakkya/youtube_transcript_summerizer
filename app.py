from flask import Flask, render_template, request
from summarizer2 import yt_summarizer
from yt_scrapper import scrap_similar_shorts
from json import dumps

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def summarize_n_recommend():
    # print(request.json, type(request.json))
    video_url = request.json['link']
    summary = yt_summarizer(video_url)
    title, shorts = scrap_similar_shorts(video_url)

    return dumps({
        "title": title,
        "summary": summary,
        "shorts": shorts
        })

if __name__ == '__main__':
    app.run(debug=True)
