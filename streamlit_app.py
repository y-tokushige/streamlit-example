import streamlit as st
from streamlit import caching #キャッシュクリア
from streamlit.script_runner import StopException, RerunException #rerun用
st.set_page_config(page_title="AsdSystem-材料検査",layout = "wide") #画面を広く使うための設定
import pandas as pd
import numpy as np
import sqlite3

st.text_input("テスト")
