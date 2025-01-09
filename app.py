import panel as pn

# パネルの拡張機能を有効化
pn.extension()

# テキスト入力ウィジェットを作成
text_input = pn.widgets.TextInput(name='テキスト入力', placeholder='ここに入力してください...')

# 入力内容を表示する関数を定義
def update_text(event):
    text_output.value = text_input.value

# テキスト入力の値が変更されたときに関数を呼び出す
text_input.param.watch(update_text, 'value')

# テキスト表示用のパネルを作成
text_output = pn.pane.Markdown("入力された内容がここに表示されます")

# レイアウトを作成
layout = pn.Column(
    "## シンプルなPanelサンプル",
    text_input,
    text_output
)

# アプリケーションとしてサーブ
layout.servable()
