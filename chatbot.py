import json
from wake_controller import WakeController
from snn_model import SNNGate
from bert_model import BertResponder

class WakeChatBot:
    def __init__(self, snn_gate, wake_ctrl):
        self.snn = snn_gate
        self.wake = wake_ctrl
        self.bert = BertResponder()

        with open("responses.json", "r", encoding="utf-8") as f:
            self.light = json.load(f)

    def reply(self, text):
        conf = self.snn.confidence(text)

        if not self.wake.should_wake(conf):
            # 軽量応答の検索
            for k, v in self.light.items():
                if k in text.lower():
                    return f"[SNN] {v}"
            return "[SNN] なるほど"

        return "[BERT] " + self.bert.respond(text)
