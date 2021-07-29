import streamlit as st
from streamlit import caching #キャッシュクリア
from streamlit.script_runner import StopException, RerunException #rerun用
st.set_page_config(page_title="AsdSystem-",layout = "wide") #画面を広く使うための設定
import pandas as pd
import numpy as np
import sqlite3

DB_PATH = "\\\\192.168.30.105\\share\\ITA室\\PowerBI用データ\\STREAMLIT.sqlite3"
#------------------------------------------------------------------------------------
# データベース(読込)
#------------------------------------------------------------------------------------
@st.cache
def sql_read(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(query)
        df = c.fetchall() 
        conn.close()
    except:
        st.error("予期せぬエラーが発生しました。再度実行して下さい")
        conn.close()
   
    return(df)
#====================================================================================
# メイン
#====================================================================================
st.title("来場受付")
st.text_input("テスト")
df = sql_read(f"SELECT * FROM ログイン")
login_df = pd.DataFrame(df)
st.write(login_df) 
