from youtube_transcript_api import YouTubeTranscriptApi as ytapi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
"""nltk.download('punkt')
nltk.download('punkt_tab')"""

def get_transcript(video_id):
    try:
        transcript = ytapi.get_transcript(video_id)
        return {"success":True, "data":"\n".join([entry["text"] for entry in transcript])}
    except Exception as e:
        return {"success":False, "data":f"Error: {e}"}
    
def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return "\n".join(str(sentence) for sentence in summary)
    
if __name__=="__main__":
    video_id = "WHYMGNbPv2U"
    result = get_transcript(video_id)
    
    if result["success"]:
        summary = summarize_text(result["data"])
        print("--SUMMARY--:")
        print(summary)
    else:
        print("Error: ",result["data"])