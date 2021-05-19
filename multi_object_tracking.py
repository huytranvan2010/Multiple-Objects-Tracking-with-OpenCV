# Cách dùng
# python opencv_object_tracking.py --tracker CSRT
# python opencv_object_tracking.py --video videos/traffic.mp4 --tracker CSRT

import cv2
import argparse
import imutils
import time

""" Trong bài này trong các lần gọi tracker đều thêm .legacy vào để tránh báo lỗi, bị nhiều lần dù cài opencv-contrib-python """

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="KCF", help="OpenCV object tracker type")  # truyền vào in hoa như bên dưới
args = vars(ap.parse_args())

# tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = args["tracker"]

def createTracker(tracker_type):
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.legacy.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.legacy.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.legacy.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    if tracker_type == 'GOTURN':
        tracker = cv2.legacy.TrackerGOTURN_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.legacy.TrackerMOSSE_create()
    if tracker_type == "CSRT":
        tracker = cv2.legacy.TrackerCSRT_create()
    return tracker

trackers = cv2.legacy.MultiTracker_create()

if not args.get("video", False):
    print("[INFO] starting video stream...")
    video = cv2.VideoCapture(0)     # lấy webcam
    time.sleep(1.)      # warm up
else:
    video = cv2.VideoCapture(args["video"])     # lấy video truyền vào

while True:
    ok, frame = video.read()    # đọc video

    # Nếu ko đọc đọc được frame
    if not ok:
        break
    
    # Nếu đọc đến cuối video
    if frame is None:
        break
    
    # resize lại để có tốc độ tốt hơn
    frame = imutils.resize(frame, width=600)

    # lấy new bounding boxé của các vật thể- update tracker
    # chú ý xem bên dưới mình mới khởi tạo tracker
    (success, boxes) = trackers.update(frame)

    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # hiển thị frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # Nhấn "s" để chọn bounding box theo dõi
    if key == ord("s"):
        # Chọn các bounding box muốn theo dõi (kéo bằng chuột), nhớ nhấn ENTER hoặc SPACE để hoàn thành 1 bounding box
        # sau khi hoàn thành nhiều bouning boxes thì nhấn ESC, ở đây có method selectROIs
        box = cv2.selectROIs("Frame", frame, fromCenter=False, showCrosshair=True)

        # bắt đầu tracking bằng cách cung cấp tọa độ bounding boxes
        """ Đây chính là khởi tạo tracker cho bounding boxes đó """
        for bb in box:
            tracker = createTracker(tracker_type)
            trackers.add(tracker, frame, bb)

    # Nhấn nhấn "q" sẽ thoát ra
    elif key == ord("q"):
        break

# Nếu sử dụng webcam thì dừng lại
if not args.get("video", False):
    video.stop()
# nếu dùng video thì release nó
else:
    video.release()

# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()

        