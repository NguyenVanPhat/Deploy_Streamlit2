import streamlit as st


with open("./haha.mp4", "rb") as file:
    btn = st.download_button(
        label="Download",
        data=file,
        file_name="result_video.mp4",
        mime="mp4"
    )