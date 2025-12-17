from chatbot import WakeChatBot
from wake_controller import WakeController
from snn_model import SNNGate, DummyModel, DummyVectorizer
import torch

# 既存モデルを読み込み (ダミー実装)
# 実際にはtorch.load("trained_snn.pt")などを行う
snn_model = DummyModel()
vectorizer = DummyVectorizer()

# デバイスはCPUに設定 (cudaはサンドボックス環境では使用不可のため)
gate = SNNGate(snn_model, vectorizer, "cpu") 
wake = WakeController(thr=0.434)  # wake_q=0.30由来

bot = WakeChatBot(gate, wake)

print("Wake-on-SNN Chatbot 起動 (exitで終了)")
while True:
    try:
        text = input("You> ")
        if text == "exit":
            break
        print("Bot>", bot.reply(text))
    except EOFError:
        print("\nExiting chat loop.")
        break
