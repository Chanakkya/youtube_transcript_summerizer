from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from functools import lru_cache

@lru_cache
def yt_summarizer(video_link):

    # Splitting of video link
    video_id = video_link.split("v=")[-1]
    trans_json = YouTubeTranscriptApi.get_transcript(video_id)

    trans_list = []
    for segment in trans_json:
        txt = segment['text']
        if not txt or txt.startswith('['):
            continue
        if ":" in txt:
            txt = txt.split(":")[-1].strip()
        trans_list.append(txt)

    trans_para = " ".join(trans_list)

    model = "t5-base"
    summarizer = pipeline("summarization", model=model)

    summarized = summarizer(trans_para, min_length=80)
    return summarized[0]['summary_text']

# print(yt_summarizer("https://www.youtube.com/watch?v=f-Nr2z5X7Rs"))
