import streamlit as st
import sys
sys.path.insert(1, './')
import detection_helpers
from detection_helpers import *
import tracking_helpers
from tracking_helpers import *
import bridge_wrapper
from bridge_wrapper import *
import tempfile

uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
if uploaded_file is not None:
    name_file = uploaded_file.name
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    # vf = cv2.VideoCapture(tfile.name)
    # st.write(type(vf))

    # st.write("Input: ", tfile.name)
    # st.write("Ouput: ", "./result/haha.mp4")
    detector = Detector()
    detector.load_model('./yolov7x.pt')
    tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)
    tracker.track_video(video=str(tfile.name), output="./haha.mp4", show_live=False, skip_frames=0, count_objects=True, verbose=15)
    st.subheader("Đã xử lý xong video !")
    st.write('Vào tab "Xem Video" nếu Video có thời lượng dưới 4s')
    st.write('Vào tab "Tải Video" nếu Video có thời lượng trên 4s')