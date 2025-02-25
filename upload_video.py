import os
import google_auth_httplib2
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http


class Upload_Youtue():

    def __init__(self):
        global SCOPES 
        self.SCOPES =  ["https://www.googleapis.com/auth/youtube.upload"]
        global TOKEN_FILE 
        self.TOKEN_FILE = 'token.json'

    def authenticate_youtube(self,title,des):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        if os.path.exists(self.TOKEN_FILE):
            os.remove(self.TOKEN_FILE)

        # Load client secrets file, put the path of your file
        client_secrets_file = 'client_.json'

    
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, self.SCOPES)
        credentials = flow.run_local_server()
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=credentials)

        print(youtube)
        request_body = {
            "snippet": {
                "categoryId": "22",
                "title": title,
                "description": des,
                "tags": ["Bible","Gospel","Christanity","jesus","GoodTimes"]
            },
            "status":{
                "privacyStatus": "public"
            }
        }

        # put the path of the video that you want to upload
        media_file = "result1.mp4"

        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True)
        )

        response = None 

        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Upload {int(status.progress()*100)}%")

            print(f"Video uploaded with ID: {response['id']}")

    # if __name__ == "__main__":
    #     youtube = authenticate_youtube()
    #     upload_video(youtube)

# yt = Upload_Youtue()
# yt.authenticate_youtube()
