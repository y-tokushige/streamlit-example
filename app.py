import streamlit as st
st.set_page_config(page_title="材料計算",layout = "wide",page_icon="\\\\192.168.30.105\\share\\ITA室\\AsdSystem\\asdico.png") #画面を広く使うための設定
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode, ColumnsAutoSizeMode
import pandas as pd
import jaconv

# `st.columns`のリストを取得
col=st.columns(10)
with col[0]:
    zaisitu = st.selectbox("材質", ["", "タングステン"])
with col[1]:
    senkei = st.text_input("線径(μ）")
with col[2]:
    meshsu = st.text_input("mesh数")
with col[3]:
    haba = st.text_input("巾(mm)")

senkei = jaconv.z2h(senkei,digit=True, ascii=True)#全角⇒半角変換
meshsu = jaconv.z2h(meshsu,digit=True, ascii=True)#全角⇒半角変換
haba = jaconv.z2h(haba,digit=True, ascii=True)#全角⇒半角変換


# データフレーム作成
columns = ["使用コイル数", "ロット番号", "同ロット数", "使用始めのＭ数", "使用終わりのM数", "使用kg数"]
data = [[i, "", "", "", "", ""] for i in range(1, 11)]
df = pd.DataFrame(data, columns=columns)

#Gridオプション変更
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_side_bar()
uniform_width = 30
for col in df.columns:
    gb.configure_column(col, width=uniform_width)

gb.configure_column(f"ロット番号", editable=True, cellEditor='NumericEditor')
gb.configure_column(f"同ロット数", editable=True, cellEditor='NumericEditor')
gb.configure_column(f"使用始めのＭ数", editable=True, cellEditor='NumericEditor')
gb.configure_column(f"使用終わりのM数", editable=True, cellEditor='NumericEditor')
gb.configure_column(f"使用kg数", editable=True, cellEditor='NumericEditor')

gridOptions = gb.build()

col=st.columns(2)
with col[0]:
    grid=AgGrid(df, theme="streamlit", enable_enterprise_modules=True, gridOptions=gridOptions,columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)               
    new_df = pd.DataFrame(grid["data"])
with col[1]:
    st.write(new_df)