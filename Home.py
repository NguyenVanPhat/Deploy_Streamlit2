import streamlit as st
import wget
import os
from os import walk
# os.system("lshw -C video")
# import tensorflow as tf
# print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# from detection_helpers import *
# from tracking_helpers import *
# from bridge_wrapper import *
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
    st.write("Đã tải yolov7x.pt tracker")


# click = st.button("Tiến hành Object Traking")

# if click and (uploaded_file is None):
#     st.caption("Làm ơn tải lên Video")



    # check file exist
    # f = []
    # mypath = "./"
    # for (dirpath, dirnames, filenames) in walk(mypath):
    #     f.extend(filenames)
    # st.write(f)









