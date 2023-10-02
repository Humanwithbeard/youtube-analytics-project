from src.channel import Channel


class Video(Channel):
    def __init__(self, channel_id, video_id=None):
        super().__init__(channel_id)
        self.video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None

        if video_id:
            try:
                self.youtube = self.get_service().videos().list(
                    part='snippet,statistics', id=self.video_id
                ).execute()
                self.video_data = self.youtube.get("items")[0]
                self.title = self.video_data.get('snippet').get('title')
                self.url = f'https://www.youtube.com/watch?v={self.video_id}'
                self.view_count = int(self.video_data.get('statistics').get('viewCount'))
                self.like_count = int(self.video_data.get('statistics').get('likeCount'))
            except IndexError as e:
                print(e)
            except Exception as e:
                self.title = None
                self.url = None
                self.view_count = None
                self.like_count = None
                print(f"An error occurred: {e}")

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, channel_id, video_id, playlist_id):
        super().__init__(channel_id, video_id)
        self.playlist_id = playlist_id
