import panel as pn

# クリック時のイベント規定
def click(event):
    # ボタンのタイプがプライマリーだったら、表示を「押すなよ」にしてボタンタイプをサクセスに。
    if button_e.button_type == "primary":
        button_e.name = "押すなよ"
        button_e.button_type = "success"
    # ボタンのプライマリー以外だったら、表示を「押せよ」にしてボタンタイプをプライマリーに。
    else:
        button_e.name = "押せよ"
        button_e.button_type = "primary"

# ボタンウィジェットの生成
button_e = pn.widgets.Button(name= "押すとイベント実行")
# clickした時のイベントを指定
button_e.on_click(click)

# 描画
button_e
