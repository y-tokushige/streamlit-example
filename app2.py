import panel as pn
import matplotlib.pyplot as plt
import numpy as np
 
# Panel拡張の初期化
pn.extension()
 
# シンプルなサイン波関数を作成
def plot_sine_wave(frequency):
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(frequency * x)
 
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"サイン波 (周波数: {frequency})")
 
    return fig
 
# 周波数をコントロールするスライダーを作成
frequency_slider = pn.widgets.FloatSlider(name='Frequency', start=0.5, end=5.0, step=0.1, value=1.0)
 
# スライダーの値に応じてプロットを動的に更新
interactive_plot = pn.bind(plot_sine_wave, frequency=frequency_slider)
 
# ダッシュボードの表示
dashboard = pn.Column(frequency_slider, interactive_plot)
dashboard.show()