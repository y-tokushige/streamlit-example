#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#====================================================================================
# ライブラリ
#====================================================================================
import streamlit as st #streamlit使用時
st.set_page_config(page_title="出荷チェック") 
from streamlit import caching
import time

import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

def kensa_seiseki():
    # VideoCaptureインスタンス生成
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    try:
        qr_data=""
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # デコード               
                value = decode(frame, symbols=[ZBarSymbol.QRCODE])
                if value:
                    for qrcode in value:
                        # QRコード座標
                        x, y, w, h = qrcode.rect
                        # QRコードデータ
                        dec_inf = qrcode.data.decode('utf-8')

                        qr_data = dec_inf
                        frame = cv2.putText(frame, dec_inf, (x, y-6), font, .3, (255, 0, 0), 1, cv2.LINE_AA)

                        # バウンディングボックス
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

                # 画像表示
                cv2.imshow('pyzbar', frame)

            # ESCキーを押した場合中断する
            k = cv2.waitKey(1)
            if k == 27:
                break
                
            if qr_data != "":
                break
                
        # 映像デバイスを閉じて終了する
        cap.release()
        cv2.destroyAllWindows()
        
        return(qr_data)

    except:
        # 映像デバイスを閉じて終了する
        cap.release()
        cv2.destroyAllWindows()  
# -----------------------------------------------------------
# Init
# -----------------------------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX

# -----------------------------------------------------------
# 画像キャプチャ
# -----------------------------------------------------------
st.title("出荷チェック")
with st.spinner('検査成績表読込...'):
    test = kensa_seiseki()
    ken_seiseki = st.text_input("検査成績表",test)

with st.spinner('ラベル読込...'):
    test2 = kensa_seiseki()
    label = st.text_input("ラベル",test2)

with st.spinner('納品書読込...'):
    test3 = kensa_seiseki()
    nouhin = st.text_input("納品書",test3)

if ken_seiseki == label:
    if label == nouhin:
        st.success("出荷可能")
    else:
        st.error("納品書エラー")
elif ken_seiseki == nouhin:
    st.error("ラベルエラー")
elif label == nouhin:
    st.error("検査成績表エラー")
else:
    st.error("全エラー")


# In[2]:


print(cap_cam.isOpened())


# In[ ]:




