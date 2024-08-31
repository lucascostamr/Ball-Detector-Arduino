from services.SerialCommunicator import SerialCommunicator
from services.Camera import Camera
from services.BallDetector import BallDetector
from config import env


def main():
    serial_communicator = SerialCommunicator(serial_device=env.SERIAL_DEVICE, baudrate=env.BAUD_RATE, timeout=env.TIMEOUT)
    camera = Camera(video_url=env.VIDEO_URL)
    ball_detector = BallDetector(lower_color=env.LOWER_COLOR, upper_color=env.UPPER_COLOR)

    while True:
        frame = camera.get_frame()
        if frame is None:
            break

        result = ball_detector.detect_ball(frame)
        if result:
            x, y, radius = result
            if radius > 10:
                frame_width = frame.shape[1]

                if x < frame_width // 3:
                    serial_communicator.send_data('L')
                    print('L')
                elif x > 2 * frame_width // 3:
                    serial_communicator.send_data('R')
                    print('R')
                else:
                    serial_communicator.send_data('S')
                    print('S')

    camera.release()
    serial_communicator.close()

if __name__ == "__main__":
    main()