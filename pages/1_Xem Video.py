import streamlit as st
import os
# import sys
# sys.path.insert(1, './')
# from Home import choose_of_user
# from PIL import Image

click_show = st.button("Xem Video")
# if click_show and choose_of_user == "video":
if click_show:
    # show video
    video_file = open("./haha.mp4", 'rb')
    # video_bytes = video_file.read()
    st.video(video_file)
# if click_show and choose_of_user == "image":
#     image = Image.open('./haha.jpg')
#     st.image(image, caption='Image Result')
