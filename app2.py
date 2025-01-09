import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd

# 初期データフレームを作成
data = {
    "使用コイル数": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "ロット番号": ["", "", "", "", "", "", "", "", "", ""],
    "同ロット数": ["", "", "", "", "", "", "", "", "", ""],
    "使用始めのＭ数": ["", "", "", "", "", "", "", "", "", ""],
    "使用終わりのM数": ["", "", "", "", "", "", "", "", "", ""],
    "使用kg数": ["", "", "", "", "", "", "", "", "", ""]
}

df = pd.DataFrame(data)

# Gridオプションの設定
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True)  # ページネーションの設定
gb.configure_default_column(editable=True)  # 全てのカラムを編集可能に設定
gridOptions = gb.build()

# AgGridでテーブルを表示
grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
    data_return_mode=DataReturnMode.AS_INPUT,
    fit_columns_on_grid_load=True,
    theme='light',  # テーブルのテーマを設定
    enable_enterprise_modules=True,
    height=350,
    reload_data=True
)

# 更新されたデータフレームを取得
updated_df = grid_response['data']

st.write("更新されたデータフレーム")
st.dataframe(updated_df)
