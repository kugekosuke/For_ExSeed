
import gradio as gr

# ダミーの関数: 予算に応じてヒットしたお店の数を返す
def dummy_function(budget):
    if budget==0:
        return "お店0つ"
    elif budget < 1000:
        return "お店1つ"
    elif budget < 2000:
        return "お店2つ"
    elif budget < 3000:
        return "お店3つ"
    elif budget < 4000:
        return "お店4つ"
    elif budget < 5000:
        return "お店5つ"
    elif budget < 6000:
        return "お店6つ"
    else:
        return "お店7つ以上"

# 入力コンポーネント: スライダー
budget_slider = gr.Slider(minimum=0, maximum=10000,value=5000, step=500, label="予算")

# 出力コンポーネント: テキスト
output_text = gr.Textbox()

# インターフェースを定義
iface = gr.Interface(dummy_function, inputs=budget_slider, outputs=output_text, title="お店検索アプリ")
iface.launch()
