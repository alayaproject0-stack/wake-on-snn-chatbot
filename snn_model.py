import torch
import numpy as np # vectorizerのダミーとして使用

# ダミーのSNNモデルとベクトライザーのクラス
class DummyModel:
    def to(self, device): return self
    def eval(self): return self
    def __call__(self, x):
        # ダミーのlogitsとspikesを返す
        return torch.tensor([[0.5, 0.5]]), None

class DummyVectorizer:
    def transform(self, text_list):
        # ダミーの疎行列を返す
        return np.array([[0.1, 0.2]])

class SNNGate:
    def __init__(self, snn_model, vectorizer, device):
        # 実際にはモデルとベクトライザーをロードするが、ここではダミー
        self.model = snn_model
        self.vec = vectorizer
        self.device = device
        # print(f"SNNGate initialized on device: {self.device}")

    @torch.no_grad()
    def confidence(self, text):
        # ダミー実装: テキストの長さに応じてconfidenceを返す
        # 長いほど（複雑な質問ほど）confidenceが低くなる（Wake!しやすい）と仮定
        length_score = len(text.split()) / 10.0
        # 0.1から0.8の範囲で、長さが長いほど値が小さくなるように調整
        confidence_score = max(0.1, 0.8 - length_score)
        
        # ユーザーの指定ではprob.max().item()なので、0.0から1.0の値を返す
        return confidence_score
