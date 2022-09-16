import streamlit as st
import os
import gc
# import sys
# sys.path.insert(1, './')
# from Home import choose_of_user
# from PIL import Image
# from memory_profiler import profile

# @st.cache(max_entries=5)
# @profile
def main_haha():
    click_show = st.button("Xem Video")
    # if click_show and choose_of_user == "video":
    if click_show:
        video_file = open("./haha.mp4", 'rb')
        st.video(video_file)
        video_file.close()
        video_file = None
        # video_bytes = video_file.read()
    click_show = None
    try:
        for name in dir():
            # st.write("Name: ", name)
            if not name.startswith('_'):
                del globals()[name]
        gc.collect()
    except:
        pass
    # if click_show and choose_of_user == "image":
    #     image = Image.open('./haha.jpg')
    #     st.image(image, caption='Image Result')

main_haha()
# gc.collect(generation=1)
# gc.collect(generation=2)