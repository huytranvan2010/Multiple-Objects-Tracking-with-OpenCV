# Tracking-multiple-objects-with-OpenCV
Run Command

```python
python opencv_object_tracking.py --video videos/traffic.mp4 --tracker CSRT
```
Bài trước chúng ta đã thực hiện Tracking single object trong OpenCV [link](https://github.com/huytranvan2010/OpenCV-Object-Tracking). Trong bài này chúng ta sẽ thực hiện track multiple objects bằng OpenCV.

**Chú ý**: Do gặp nhiều lỗi trong quá trình cài đặt OpenCV nên trong các câu lệnh gọi tracker chúng ta đều thêm `.legacy` để không còn lỗi.

Các bước thực hiện MultiTracker:
* **Bước 1:** Đọc frame từ video - `multi-object tracker` cần 2 inputs là video frame và bounding boxes của tất cả các objects muốn theo dõi.
* **Bước 2:** Xác định vị trí của object trong frame - dùng `selectROIs()` để chọn được nhiều bounding box. Khi chọn được 1 bounding box thì nhất ENTER hoặc SPACE để hoàn thành việc chọn, tiếp tục cho những bounding box khác. Sau khi kết thúc nhấn ESC để thực hiện tracking.
* **Bước 3:** Tạo Single Object Tracker - `multi-object tracker` thực chất là tập hợp các simple object tracker.
* **Bước 4:** Khởi tạo MuiltiTracker
* **Bước 5:** Update MUltiTracker và hiển thị kết quả 

Các vấn đề của MultiTracker:
* Càng nhiều trackers được tạo ra thì tốc độ xử lý càng chậm
* Mỗi lần theo dõi đối tương lại phải tạo lại tracker riêng (ko sử dụng chung được)
# Tài liệu tham khảo
https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/

https://learnopencv.com/multitracker-multiple-object-tracking-using-opencv-c-python/
