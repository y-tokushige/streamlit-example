import streamlit as st
from streamlit import caching #キャッシュクリア
from streamlit.script_runner import StopException, RerunException #rerun用
st.set_page_config(page_title="AsdSystem-",layout = "wide") #画面を広く使うための設定
import pandas as pd
import numpy as np
import sqlite3
#====================================================================================
# 定数 （共通）
#====================================================================================
# データベースファイルのパス
DB_PATH = "\\\\192.168.30.105\\share\\ITA室\\PowerBI用データ\\前工程test.sqlite"

# デスクトップのパス
DESKTOP_PATH = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop\\"

#====================================================================================
# メイン
#====================================================================================
st.title("来場受付")
st.text_input("テスト")
file_up = st.file_uploader("ダイス入力表")
if file_up:
    daice_in = pd.read_excel(file_up, sheet_name=0)
    st.write(daice_in) 
