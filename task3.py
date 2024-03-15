#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

video_path = 'test.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error")
    exit()


while True:
    ret, frame = cap.read()
    

    if not ret:
        break
    cv2.resize(frame ,(280,280))
    frame_path = f'frame_{frame_count}.jpg'
    cv2.imwrite(frame_path, frame)


cap.release()


# In[ ]:





# In[ ]:




