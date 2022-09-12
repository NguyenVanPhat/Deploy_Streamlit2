import streamlit as st
import os

click_show = st.button("Xem Video")
if click_show:
    # show video
    video_file = open("./haha.mp4", 'rb')
    # video_bytes = video_file.read()
    st.video(video_file)
