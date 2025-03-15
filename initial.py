import os 
import google_auth_oauthlib.flow
import googleapiclient.discovery

SCOPES = [
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube.readonly"
]

def authenticate_yt():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=8080)
    yt = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return yt

def get_captions(yt, video_id):
    request = yt.captions().list(
        part="snippet",
        videoId = video_id
    )
    response = request.execute()

    if "items" in response and response["items"]:
        for caption in response["items"]:
            print(f"Caption ID: {caption['id']} - Language: {caption['snippet']['language']}")
            return caption["id"]
    else:
        print("No captions available")
        return None
    
def download_caption(yt, caption_id):
    request = yt.captions().download(id=caption_id).execute()
    with open("captions.srt","wb") as f:
        f.write(request)
    print("Captions saved as captions.srt")

if __name__ == "__main__":
    yt = authenticate_yt()
    video_id = "WHYMGNbPv2U"
    caption_id = get_captions(yt, video_id)

    if caption_id:
        download_caption(yt, caption_id)