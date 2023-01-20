#====================================================================================
# ライブラリ
#====================================================================================
import streamlit as st
st.set_page_config(page_title="AsdSystem-Excelリフレッシュ") #画面を広く使うための設定
#import win32com.client
#import pythoncom
#import tkinter as Tk
#from tkinter import filedialog
import os

# デスクトップ
DESKTOP_PATH = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop\\"
#====================================================================================
# メイン
#====================================================================================
def main():
    if st.button("ファイル選択"):
        filetype = [("Excel","*.xls*"),("すべて","*")]
        file_path = tkinter.filedialog.askopenfilename(filetypes = filetype,initialdir = DESKTOP_PATH)
    else:
        st.stop()

    pythoncom.CoInitialize() 
    xl = Dispatch('Excel.Application')
    xl.Visible = False
    wb = xl.Workbooks.Open(file_path)
    #if i == 1:
    #    pass
    wb.Close(SaveChanges=False)
    xl.Quit()

    st.success("処理完了")

if __name__ == "__main__":
    main()
