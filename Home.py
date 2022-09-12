import streamlit as st
import wget
import os
from os import walk
# os.system("lshw -C video")
# import tensorflow as tf
# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
from detection_helpers import *
from tracking_helpers import *
from bridge_wrapper import *
# from PIL import Image
import tempfile
# import cv2
from os.path import exists

st.set_page_config(
    page_title="Web_App_Of_Phat",
    page_icon="💽",
)
st.markdown("<h1 style='text-align: center; color: red;'>🎥 Web App of Phat 📀</h1>", unsafe_allow_html=True)
st.header('')
st.header('')
path = ""

# os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
if not exists("./yolov7x.pt"):
    wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
    detector = Detector()
    detector.load_model('./yolov7x.pt')
    # tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)
    st.write("Đã khởi tạo tracker")

uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
# click = st.button("Tiến hành Object Traking")

# if click and (uploaded_file is None):
#     st.caption("Làm ơn tải lên Video")

if uploaded_file is not None:
    name_file = uploaded_file.name
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    # vf = cv2.VideoCapture(tfile.name)
    # st.write(type(vf))

    # st.write("Input: ", tfile.name)
    # st.write("Ouput: ", "./result/haha.mp4")
    tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)
    tracker.track_video(video=str(tfile.name), output="./haha.mp4", show_live=False, skip_frames=0, count_objects=True, verbose=15)

    # check file exist
    # f = []
    # mypath = "./"
    # for (dirpath, dirnames, filenames) in walk(mypath):
    #     f.extend(filenames)
    # st.write(f)

    st.subheader("Đã xử lý xong video !")
    st.write('Vào tab "Xem Video" nếu Video có thời lượng dưới 4s')
    st.write('Vào tab "Tải Video" nếu Video có thời lượng trên 4s')







