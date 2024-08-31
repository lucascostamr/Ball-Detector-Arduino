import cv2

class Camera:
    def __init__(self, video_url):
        self.capture = cv2.VideoCapture(video_url)

    def get_frame(self):
        retrieve, frame = self.capture.read()
        if not retrieve:
            return None
        return frame

    def release(self):
        self.capture.release()
