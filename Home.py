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
import tempfile
import cv2
from os.path import exists
from PIL import Image

st.set_page_config(
    page_title="Web_App_Of_Phat",
    page_icon="💽",
)
st.markdown("<h1 style='text-align: center; color: red;'>🎥 Web App of Phat 📀</h1>", unsafe_allow_html=True)
st.header('')
st.header('')
path = ""

if not exists("./yolov7x.pt"):
    wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")


# os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")

# "@st.cache" sẽ kiểm tra xem nếu "text" truyền vào ko thay đổi thì hàm sẽ trả ra cùng 1 kết quả so với lần..
# chạy trước, Do đó nó sẽ ko chạy nữa mà lấy luôn kết quả của lần chạy trước (nghĩa là chỉ chạy 1 lần duy nhất)
# điều này giúp Model ko phải load đi load lại tránh tràn RAM hoặc disk của máy chủ (streamlit cloud)
# @st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
@st.cache
def load_model(text):
    detector_temp = Detector()
    detector_temp.load_model(text)
    return detector_temp


# click = st.button("Tiến hành Object Traking")

# if click and (uploaded_file is None):
#     st.caption("Làm ơn tải lên Video")
detector = load_model("./yolov7x.pt")
uploaded_file = st.file_uploader("Tải video lên", type=["mp4", "jpg", "png", "jpeg"])
# global choose_of_user
if uploaded_file is not None and uploaded_file.type == "video/mp4":
    name_file = uploaded_file.name
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    # vf = cv2.VideoCapture(tfile.name)
    # st.write(type(vf))

    # st.write("Input: ", tfile.name)
    # st.write("Ouput: ", "./result/haha.mp4")

    tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)
    tracker.track_video(video=str(tfile.name), output="./haha.mp4", show_live=False, skip_frames=0, count_objects=True,
                        verbose=15)
    # check file exist
    # f = []
    # mypath = "./"
    # for (dirpath, dirnames, filenames) in walk(mypath):
    #     f.extend(filenames)
    # st.write(f)

    st.subheader("Đã xử lý xong video !")
    st.write('Vào tab "Xem Video" để xem video kết quả')
    # choose_of_user = "video"
    # detector = 0
    # tracker = 0
    # os.remove("./traced_model.pt")

if uploaded_file is not None and (uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/png" or uploaded_file.type == "image/jpeg"):
    name_file = uploaded_file.name
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    result = detector.detect(str(tfile.name), plot_bb=True)

    if len(result.shape) == 3:  # If it is image, convert it to proper image. detector will give "BGR" image
        result = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        # cv2.imwrite("./haha.jpg", result)
        # choose_of_user = "image"
        # image = Image.open('./haha.jpg')
        st.image(result, caption='Image Result')

