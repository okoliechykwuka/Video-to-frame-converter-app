
import tempfile
from datetime import datetime
import cv2
import os
import streamlit as st
import io


#Title
st.title(" Video to Frame Converter")

# User Directory 
user_input = st.text_input("Enter a folder name : ")

path = "Video-frame"
path1 = user_input.title()

if st.button("summit"):
    try:  
        
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path1):
            os.makedirs(os.path.join(path, path1))
            new = path
            mode = 0o666  
    except OSError as error:  
        print(error) 
    result = path1.title() +  " Successfully created "
    
    st.success(result)

 # Video frame   
f = st.file_uploader("Choose a Video")
if f:
    st.video(io.BytesIO(f.getbuffer()))
    dateObj = datetime.now()
    dateStr = dateObj.strftime("%b %d %Y ")
    today = st.write("Today's date is ", dateStr)
    
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(f.read())
    
    # Opens the Video file
    cap= cv2.VideoCapture(tfile.name)
    stframe = st.empty()
    i=1
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%10 == 0: 
            
            cv2.imwrite(('new_image'+str(i)+'.jpg'),frame)
        i+=1
    cap.release()
    cv2.destroyAllWindows()

    result =  " Video succesfully converted to frame! "
    st.success(result)

    # if result:
    #     st.balloons()
    
# About
st.sidebar.subheader("About App")
st.sidebar.text("App Simply Convert Videos to frame")
st.sidebar.info("Creat a subfolder to save video frame")
st.sidebar.text("App Created by Okolie Chukwuka")



