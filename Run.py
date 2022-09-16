import os
import wget
import imageio
import streamlit as st
import cv2
import tempfile
from os import walk
from os.path import exists
import shutil
import time
from memory_profiler import profile

# uploaded_file = st.file_uploader("Tải video lên", type=["mp4", "jpg"])
# uploaded_file = st.file_uploader("Tải video lên", type=["jpeg"])
# if uploaded_file is not None:
#     st.write(uploaded_file.type)
#     st.write(type(uploaded_file.type))

# def show_size_disk(path):
#     size = 0
#     for path, dirs, files in os.walk(path):
#         for f in files:
#             fp = os.path.join(path, f)
#             size += os.path.getsize(fp)
#     return size
@profile
def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
# a = round(get_dir_size() * 0.000001)
# st.write("dung lượng: " + str(a) + " Mb")
# os.system("python -m memory_profiler Run.py")


# cap = cv2.VideoCapture("People_Demo.mp4")
# length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# length_100 = round(length*(100/length))
#
# my_bar = st.progress(0)
# for percent_complete in range(length_100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete)


# os.system("streamlit run home.py")
# wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
# phat_test()


# video1 = open("street_input.mp4", "rb")
# st.video(video1)
# uploaded_file = st.file_uploader("Tải video lên", type=["mp4"])
# if uploaded_file is not None:
#     name_file = uploaded_file.name
#     st.write("./result/" + str(name_file))


# get FPS
# st.write(uploaded_file.name)
# tfile = tempfile.NamedTemporaryFile(delete=False)
# tfile.write(uploaded_file.read())
# vf = cv2.VideoCapture(tfile.name)
# fps = vf.get(cv2.CAP_PROP_FPS)
# st.write(int(fps))

# os.remove("./traced_model.pt")

# check file in folder
# f = []
# mypath = "./models"
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
# st.write(f)

