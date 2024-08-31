from os import environ

VIDEO_URL = environ.get("VIDEO_URL")
BAUD_RATE = 9600
SERIAL_DEVICE = environ.get("SERIAL_DEVICE")
TIMEOUT = 0.1

LOWER_COLOR = [0, 120, 70]
UPPER_COLOR = [10, 255, 255]