import streamlit as st
st.set_page_config(page_title="材料計算",layout = "wide",page_icon="\\\\192.168.30.105\\share\\ITA室\\AsdSystem\\asdico.png") #画面を広く使うための設定
#from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode, ColumnsAutoSizeMode
import pandas as pd
import jaconv
import numpy as np

# `st.columns`のリストを取得

col=st.columns(5)
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


columns = ["ロット番号", "使用コイル数","同ロット数", "使用始めのM数", "使用終わりのM数"]
data = [["", "", "", "", ""] for _ in range(10)]
df = pd.DataFrame(data, columns=columns, index=range(1, 11))

try:
    col=st.columns(2)
    with col[0]:
        eddf = st.data_editor(df)

        eddf = eddf.replace("", np.nan) # 空白をnanへ返還
        eddf = eddf.dropna(how='all', subset=["ロット番号", "使用コイル数"]).reset_index(drop=True) # nan行を削除
        eddf = eddf.applymap(lambda x: jaconv.z2h(x, kana=False, ascii=True, digit=True))# 全角を半角に変換

        eddf["材質"] = zaisitu
        eddf["線径"] = float(senkei)
        eddf["メッシュ数"] = int(meshsu)
        eddf["巾"] = int(haba)

        eddf["使用始めのM数"] = pd.to_numeric(eddf["使用始めのM数"], errors='coerce').fillna(0).astype(int)
        eddf["使用終わりのM数"] = pd.to_numeric(eddf["使用終わりのM数"], errors='coerce').fillna(0).astype(int)
        eddf["使用コイル数"] = pd.to_numeric(eddf["使用コイル数"], errors='coerce').fillna(0).astype(int)
        eddf["同ロット数"] = pd.to_numeric(eddf["同ロット数"], errors='coerce').fillna(0).astype(int)

        #try:
        eddf["計算結果"] = np.where(
            eddf["材質"] == "タングステン",
            (((100/2.54*eddf["メッシュ数"]*((eddf["巾"]/1000)+0.2)*((eddf["線径"]/1000)*(eddf["線径"]/1000))*6.225)*(eddf["使用終わりのM数"]-eddf["使用始めのM数"])/eddf["使用コイル数"]*eddf["同ロット数"]/1000))*2.92,  # 計算式1
            (((100/2.54*eddf["メッシュ数"]*((eddf["巾"]/1000)+0.2)*((eddf["線径"]/1000)*(eddf["線径"]/1000))*6.225)*(eddf["使用終わりのM数"]-eddf["使用始めのM数"])/eddf["使用コイル数"]*eddf["同ロット数"]/1000))  # 計算式2
        )

    with col[1]:
        df2=eddf[["ロット番号","計算結果"]]
        df2.index = range(1, len(df2) + 1)
        grouped_df = df2.groupby("ロット番号").sum()
        grouped_df = grouped_df.round(2)
        st.write(grouped_df)



    #st.write(df2)
except:
    pass













#container = st.container(border=True)
#col=container.columns(10)
#with col[0]:
#    siyocoil = [st.text_input("使用コイル数" if i == 0 else "", key=f"input_{i}") for i in range(10)]

text="""
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

"""