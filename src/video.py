import json
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.youtube = self.get_service()
        self.video_data = self.fetch_video_data()

    def __str__(self):
        return f"{self.video_data['title']}"

    def get_service(self):
        api_key = 'AIzaSyDOsEBflTxbKq0zbiuwT1Tp53zY33WQmEI'
        return build('youtube', 'v3', developerKey=api_key)

    def fetch_video_data(self):
        request = self.youtube.videos().list(
            part='snippet,statistics',
            id=self.video_id
        )
        response = request.execute()

        if 'items' in response:
            video_info = response['items'][0]
            snippet = video_info['snippet']
            statistics = video_info['statistics']

            video_data = {
                'id': self.video_id,
                'title': snippet['title'],
                'link': f'https://www.youtube.com/watch?v={self.video_id}',
                'viewCount': int(statistics['viewCount']),
                'likeCount': int(statistics['likeCount']),
            }
            return video_data


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        self.playlist_id = playlist_id
        self.video_id = video_id
        super().__init__(video_id)

    def fetch_video_data(self):
        video_data = super().fetch_video_data()
        video_data['playlist_id'] = self.playlist_id
        return video_data




