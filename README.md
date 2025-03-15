**Initial Plan:**
	The project aims to build a web app that summarizes (educational) YouTube videos by extracting captions and generating concise summaries.
	The first version (MVP) will focus on fetching captions from the video and implement NLP-based summarization.
	Then create a simple web interface for users to input a video link and get summarized notes.
	If official captions are not available, alternative solutions like speech-to-text models will be explored later.

_Extracting transcripts from youtube:_
	There are 2 options available:
 		1. Use youtube-transcript-api
   		2. Use YouTube Data API
	 
_Going with Option 2:_
	For more control and to keep things official we'll start by exploring OAuth 2.0 authentication to download captions officially
  	( We are required to have OAuth Credentials,  basic initial authentication in the code with the credentials and manage youtube api with required permissions )
   
    This will extract captions from the videos only if the captions are posted by owner
	If a video does not have captions, we will use Automatic Captions (if available):
   			YouTube sometimes auto-generates captions even if the creator didn’t upload them.
			The API response will indicate if auto-captions exist.
    If it is not available: we'll let Users Know.
	
	By default, Google restricts OAuth authentication to only developer-approved testers until you submit your app for verification.
