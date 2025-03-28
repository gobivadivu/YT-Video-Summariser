from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import openai
import os
from openai import OpenAI

openai_api_key = "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"
"""client = OpenAI(api_key=openai_api_key)
try:
    models = client.models.list()
    print("Available models: ")
    for model in models:
        print(model.id)
except Exception as e:
    print(f"Error: {e}")"""

def get_transcript(video_id):
    try:
        transcript = ytapi.get_transcript(video_id)
        return {"success":True, "data":"\n".join([entry["text"] for entry in transcript])}
    except Exception as e:
        return {"success":False, "data":f"Error: {e}"}
    
def generate_notes(text):
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"system","content": "Extract key concepts, definitions, and important points from the provided text and organize them into a structured format for students' last-minute revision."},
                {"role": "user", "content": text}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return  f"error :{e}"
    
if __name__=="__main__":
    video_id = "WHYMGNbPv2U"
    result = get_transcript(video_id)
    
    if result["success"]:
        notes = generate_notes(result["data"])
        print("--NOTES--:")
        print(notes)
    else:
        print("Error: ",result["data"])