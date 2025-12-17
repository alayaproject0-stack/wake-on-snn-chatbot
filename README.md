# Wake-on-SNN × BERT Hybrid Chatbot

このプロジェクトは、**「Wake-on-SNN × BERT Hybrid チャットボット」**の最小実装（しかし拡張可能）を整理したものです。

人間の脳の構造を模倣し、軽量なスパイクニューラルネットワーク（SNN）を「無意識フィルタ」として使用し、必要に応じて重いBERT/LLMモデルを「意識」として起動することで、省電力かつ効率的な応答を目指します。

## 設計思想

| 構造（人間の脳対応） | 説明 |
| :--- | :--- |
| **SNN: 無意識フィルタ** | 雑談や定型的な入力に対して軽量応答を行います。応答の不確実性が低い場合に機能します。 |
| **BERT / LLM: 意識** | 思考が必要な、または不確実性の高い入力に対してSNNによって`Wake!`（起動）され、深い返答を生成します。 |

## 役割分担

| モジュール | 役割 |
| :--- | :--- |
| `SNNGate` | 入力テキストの「自信度（confidence）」を計算し、「考える必要があるか？」を判定します。 |
| `WakeController` | `confidence`と閾値（`thr`）を比較し、BERTを起動するかどうか（`should_wake`）を制御します。 |
| `BertResponder` | 意味理解・応答生成を担当します。将来的にはLLMに差し替え可能です。 |
| `WakeChatBot` | 会話状態を管理し、SNNとBERTの応答を切り替えます。 |

## フォルダ構成

```
wake_chatbot/
├─ snn_model.py       # SNNの推論ゲート（現在はダミー実装）
├─ bert_model.py      # BERT/LLMによる意識層（現在はダミー実装）
├─ wake_controller.py # SNNのconfidenceからBERT起動を制御
├─ chatbot.py         # メインのチャットボットロジック
├─ responses.json     # 軽量応答データ
└─ run_chat.py        # 起動スクリプト
```

## 実行方法

**注意:** この実装は概念実証のためのダミーモデルを使用しており、実際にSNNやBERTの重みをロードして動作させるには、追加のライブラリ（`torch`, `transformers`など）と学習済みモデルが必要です。

```bash
# 必要なライブラリのインストール (例)
# pip install torch transformers

# 実行
python run_chat.py
```

### 実行時の挙動 (想定)

- `You> こんにちは` -> `Bot> [SNN] こんにちは😊` (軽量応答)
- `You> 人間はなぜ争うの？` -> `Bot> [BERT] 考えて答えると…この話題は「哲学」ですね。` (BERT起動)
