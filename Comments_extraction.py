import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Your API key here
api_key = "###"

youtube = build("youtube", "v3", developerKey=api_key)

from googleapiclient.errors import HttpError

def get_video_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        try:
            response = youtube.commentThreads().list(
                part="id,snippet",
                videoId=video_id,
                maxResults=100,
                textFormat="plainText",
                order="relevance",
                pageToken=next_page_token,
            ).execute()

            for item in response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]
                comments.append(
                    {
                        "video_id": video_id,
                        "comment_id": item["id"],
                        "comment_text": comment["textDisplay"],
                        "update_date": comment["updatedAt"],
                        "likes": comment["likeCount"],
                    }
                )

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        except HttpError as e:
            error_reason = e._get_reason().lower()

            if "commentsdisabled" in error_reason:
                print(f"Comments are disabled for video {video_id}")
            else:
                print(f"An error occurred for video {video_id}: {e}")

            break

    return comments


def get_channel_id(query):
    response = youtube.search().list(
        part="id,snippet",
        q=query,
        type="channel",
        maxResults=1
    ).execute()

    return response['items'][0]['id']['channelId']

def get_videos(channel_id):
    videos = []
    next_page_token = None

    while True:
        try:
            response = youtube.search().list(
                part="id",
                channelId=channel_id,
                maxResults=50,
                order="date",
                publishedBefore="2023-04-01T00:00:00Z",
                type="video",
                pageToken=next_page_token
            ).execute()

            videos.extend(response['items'])
            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

        except HttpError as e:
            print(f"An error occurred: {e}")
            break

    return videos

def save_comments_csv(influencer, output_file):
    channel_id = get_channel_id(influencer)
    videos = get_videos(channel_id)

    all_comments = []

    for video in videos:
        video_comments = get_video_comments(video["id"]["videoId"])
        all_comments.extend(video_comments)

    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        fieldnames = ["video_id", "comment_id", "comment_text", "update_date", "likes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for comment in all_comments:
            writer.writerow(comment)

influencers = [
    'Vegetta'
]

for influencer in influencers:
    try:
        output_file = f"{influencer}_comments.csv"
        save_comments_csv(influencer, output_file)
        print(f"Comments for {influencer} successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while processing {influencer}: {e}")
