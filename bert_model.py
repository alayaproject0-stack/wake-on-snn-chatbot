from transformers import pipeline

class BertResponder:
    def __init__(self):
        # 実際にはパイプラインを初期化するが、ここではダミー
        # self.pipe = pipeline(
        #     "text-classification",
        #     model="distilbert-base-uncased",
        #     return_all_scores=True
        # )
        # print("BertResponder initialized (using dummy pipeline)")
        pass

    def respond(self, text):
        # ダミー実装: テキストの長さに応じてラベルを返す
        if len(text) > 15:
            label = "哲学"
        elif len(text) > 8:
            label = "技術"
        else:
            label = "日常"
            
        # scores = self.pipe(text)[0]
        # top = max(scores, key=lambda x: x["score"])
        # return f"考えて答えると…この話題は「{top["label"]}」ですね。"
        return f"考えて答えると…この話題は「{label}」ですね。"

# ※ 後で LLMに差し替え可能
