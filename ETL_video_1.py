import csv
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound

# Set up API credentials
API_KEY = 'AIzaSyBcRAIrp45w0a5HZjPutrLoEjh-_D75o70'

# Set up API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Helper functions
def get_channel_id_by_name(channel_name):
    response = youtube.search().list(
        part='snippet',
        q=channel_name,
        type='channel',
        maxResults=1
    ).execute()

    if response['items']:
        return response['items'][0]['snippet']['channelId']
    else:
        return None

def get_channel_videos(channel_id, max_results=50, published_before=None):
    videos = []
    page_token = None
    while True:
        response = youtube.search().list(
            part='id,snippet',
            channelId=channel_id,
            maxResults=max_results,
            type='video',
            order='date',
            publishedBefore=published_before,
            pageToken=page_token
        ).execute()
        videos.extend(response['items'])
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    return videos


def get_video_details(video_id):
    response = youtube.videos().list(
        part='statistics,snippet',
        id=video_id
    ).execute()
    video = response['items'][0]
    languages = ['en', 'es']

    try:
        srt = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        transcript_text = ' '.join([entry['text'] for entry in srt])
    except (NoTranscriptFound, TranscriptsDisabled):
        transcript_text = 'Subtitle not available'

    return {
        'video_id': video_id,
        'title': video['snippet']['title'],
        'description': video['snippet']['description'],
        'publish_date': video['snippet']['publishedAt'],
        'likes': video['statistics'].get('likeCount', 'Not available'),
        'views': video['statistics'].get('viewCount', 'Not available'),
        'comments': video['statistics'].get('commentCount', 'Not available'),
        'transcript': transcript_text
    }

def etl(channel_name, output_csv, published_before='2023-04-01T00:00:00Z'):
    channel_id = get_channel_id_by_name(channel_name)

    if channel_id:
        # Extract
        videos = get_channel_videos(channel_id, published_before=published_before)
        video_details = [get_video_details(video['id']['videoId']) for video in videos]

        # Transform
        # The data is already in a suitable format

        # Load
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['video_id', 'title', 'description', 'publish_date', 'likes', 'views', 'comments', 'transcript']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for video in video_details:
                writer.writerow(video)
        print('Data successfully extracted and saved to {}'.format(output_csv))
    else:
        print(f'Channel not found for the name: {channel_name}')

# Main script
if __name__ == '__main__':
    influencers = [
        'Mostopapi',
        'Orslok',
        'Vegetta'
    ]

for influencer in influencers:
    try:
        output_file = f'{influencer}_videos.csv'
        etl(influencer, output_file)
        print(f'Data for {influencer} successfully extracted and saved to {output_file}')
    except HttpError as e:
        print(f'An error occurred while processing {influencer}: {e}')

