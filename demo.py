
# coding: utf-8

# In[ ]:


import cv2


# In[ ]:


from face import *


# In[ ]:


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1)
    face = face_detect(img)
    try:
        for i in face['faces']:
            rec = i['face_rectangle']
            info = face_analyze(i['face_token'])
            search_result1 = face_search(i['face_token'], 'songliang')
            search_result2 = face_search(i['face_token'], 'xuye')
            search_result3 = face_search(i['face_token'], 'wyy')
            f = zip(info['faces'][0]['attributes']['emotion'].values(), info['faces'][0]['attributes']['emotion'].keys())
            if search_result1['results'][0]['confidence'] > 80:
                cv2.putText(img, 'songliang', (rec['left'], rec['top'] + 30), 1, 1, (255, 255, 0))
            if search_result2['results'][0]['confidence'] > 80:
                cv2.putText(img, 'xuye', (rec['left'], rec['top'] + 30), 1, 1, (255, 255, 0))
            if search_result3['results'][0]['confidence'] > 80:
                cv2.putText(img, 'wyy', (rec['left'], rec['top'] + 30), 1, 1, (255, 255, 0))
            cv2.putText(img, 'age:{0}, sex:{1}, emotion:{2}'.format(info['faces'][0]['attributes']['age']['value'], info['faces'][0]['attributes']['gender']['value'], sorted(f, reverse=True)[0][1]), (rec['left'], rec['top']), 1, 1, (255, 0, 0))
            cv2.rectangle(img, (rec['left'], rec['top']), (rec['left'] + rec['width'], rec['top'] + rec['height']), (255, 0, 0), 1)
    except Exception as e:
        print(e)
    #print(face)
    cv2.imshow('', img)
    if cv2.waitKey(50) == 27:
        break
cap.release()

