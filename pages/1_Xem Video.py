import streamlit as st
import os
# import sys
# sys.path.insert(1, './')
# from Home import choose_of_user
# from PIL import Image
from memory_profiler import profile

# @st.cache(max_entries=5)
@profile
def main_haha():
    @st.cache(max_entries=2)
    def show_video():
        video_file = open("./haha.mp4", 'rb')
        st.video(video_file)
        video_file.close()
        video_file = None

    click_show = st.button("Xem Video")
    # if click_show and choose_of_user == "video":
    if click_show:
        show_video()
        # video_bytes = video_file.read()
    click_show = None
    # if click_show and choose_of_user == "image":
    #     image = Image.open('./haha.jpg')
    #     st.image(image, caption='Image Result')

main_haha()