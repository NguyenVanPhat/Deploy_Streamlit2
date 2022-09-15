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
# from memory_profiler import profile
# import gc
st.markdown("<h1 style='text-align: center; color: red;'>Web App of Phat</h1>", unsafe_allow_html=True)
st.header('')
st.header('')

# @profile
def main_haha():
    # os.system("python -m memory_profiler Home.py")
    # st.set_page_config(
    #     page_title="Web_App_Of_Phat",
    #     # page_icon="😃",
    # )
    # gc.set_threshold(300, 5, 5)
    # st.write("Số đối tượng không thể truy cập được GC thu thập: ", gc.collect())
    # st.write("Rác không thể thu gom: ", gc.garbage)
    # def get_dir_size(path='.'):
    #     total = 0
    #     with os.scandir(path) as it:
    #         for entry in it:
    #             if entry.is_file():
    #                 total += entry.stat().st_size
    #             elif entry.is_dir():
    #                 total += get_dir_size(entry.path)
    #     return total

    # os.system("wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")

    # "@st.cache" sẽ kiểm tra xem nếu "text" truyền vào ko thay đổi thì hàm sẽ trả ra cùng 1 kết quả so với lần..
    # chạy trước, Do đó nó sẽ ko chạy nữa mà lấy luôn kết quả của lần chạy trước (nghĩa là chỉ chạy 1 lần duy nhất)
    # điều này giúp Model ko phải load đi load lại tránh tràn RAM hoặc disk của máy chủ (streamlit cloud)
    # @st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
    @st.cache
    def load_model(text):
        wget.download("https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt")
        detector_temp = Detector()
        detector_temp.load_model(text)
        os.remove(text)
        os.remove("./traced_model.pt")
        # st.write("Đã load Model")
        return detector_temp

    # @st.cache(max_entries=2)
    # @st.experimental_singleton
    @st.experimental_singleton(suppress_st_warning=True)
    def track_vdieo(text):
        detector = load_model("./yolov7x.pt")
        tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)
        tracker.track_video(video=str(text), output="./haha.mp4", show_live=False, skip_frames=0,
                            count_objects=True,
                            verbose=15)
        detector = None
        tracker = None

    # @st.cache(max_entries=2)
    # @st.experimental_singleton
    @st.experimental_singleton(suppress_st_warning=True)
    def detect_image(txt):
        detector = load_model("./yolov7x.pt")
        result = detector.detect(str(txt), plot_bb=True)
        if len(result.shape) == 3:  # If it is image, convert it to proper image. detector will give "BGR" image
            result = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            st.image(result, caption='Image Result')
        result = None
        tfile = None
        detector = None

    # click = st.button("Tiến hành Object Traking")

    # if click and (uploaded_file is None):
    #     st.caption("Làm ơn tải lên Video")
    st.experimental_singleton.clear()
    uploaded_file = st.file_uploader("Tải video lên", type=["mp4", "jpg", "png", "jpeg"])
    # global choose_of_user
    if uploaded_file is not None and uploaded_file.type == "video/mp4":
        # giải phóng dung lượng bằng cách xoá file Result Video cũ
        if exists("./haha.mp4"):
            os.remove("./haha.mp4")
            # st.write("Đã xoá video cũ")
        # a = get_dir_size()
        # st.write("dung lượng khởi điểm: " + str(round(a * 0.000001)) + " Mb")
        # name_file = uploaded_file.name
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        # vf = cv2.VideoCapture(tfile.name)
        # st.write(type(vf))

        # st.write("Input: ", tfile.name)
        # st.write("Ouput: ", "./result/haha.mp4")
        track_vdieo(tfile.name)


        # Giải phóng dung lượng disk
        os.remove(str(tfile.name))
        # del tfile
        # del tracker
        # del detector
        # gc.collect(generation=2)
        # gc.collect()
        # del name_file
        # del a
        # detector = None
        # tracker = None
        # tfile = None

        # check file exist
        # f = []
        # mypath = "./"
        # for (dirpath, dirnames, filenames) in walk(mypath):
        #     f.extend(filenames)
        # st.write(f)

        st.subheader("Đã xử lý xong video !")
        st.write('Vào tab "Xem Video" để xem video kết quả')
        # st.write("dung lượng kết thúc: " + str(round(get_dir_size() * 0.000001)) + " Mb")
        # gc.collect()
        # choose_of_user = "video"
        # detector = 0
        # tracker = 0
        # os.remove("./traced_model.pt")

    if uploaded_file is not None and (
            uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/png" or uploaded_file.type == "image/jpeg"):

        name_file = uploaded_file.name
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        detect_image(tfile.name)
        st.experimental_singleton.clear()

        # result = detector.detect(str(tfile.name), plot_bb=True)


            # cv2.imwrite("./haha.jpg", result)
            # choose_of_user = "image"
            # image = Image.open('./haha.jpg')

        # del result
        # del tfile
        # del detector
        # result = None
        # tfile = None
        # detector = None
        # gc.collect()

    uploaded_file = None
# gc.enable()

main_haha()
# st.write("Khởi động")