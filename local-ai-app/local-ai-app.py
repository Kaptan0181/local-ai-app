import sys
import json
from pathlib import Path

from llama_cpp import Llama
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QScrollArea, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import sounddevice as sd
import vosk


# ================== PATHS ==================
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

LLM_MODEL_NAME = "model.gguf"
VOSK_MODEL_NAME = "vosk"


# ================== LLM ==================
#“This feature will be added in the final version of the application.”


# ================== SPEECH TO TEXT ==================
#“This feature will be added in the final version of the application.”

# ================== UI ==================
class ChatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Local AI Chat")
        self.resize(1000, 720)
        self.setStyleSheet("background-color:#1e1e1e;")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(12, 12, 12, 12)

        self.build_top_bar()
        self.build_chat_area()
        self.build_input_area()
        self.build_footer()

    # ---------- UI PARTS ----------
    def build_top_bar(self):
        layout = QHBoxLayout()

        new_chat_btn = QPushButton("🆕 Yeni Sohbet")
        new_chat_btn.clicked.connect(self.clear_chat)
        new_chat_btn.setStyleSheet("""
            QPushButton {
                background:#0078d7;
                color:white;
                border-radius:18px;
                padding:8px 20px;
                font-weight:bold;
            }
        """)

        layout.addWidget(new_chat_btn)
        layout.addStretch()
        self.main_layout.addLayout(layout)

    def build_chat_area(self):
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("border:none;")

        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignTop)

        self.scroll.setWidget(self.chat_container)
        self.main_layout.addWidget(self.scroll)

    def build_input_area(self):
        layout = QHBoxLayout()

        self.mic_button = QPushButton("🎤")
        self.mic_button.setFixedSize(42, 42)
        self.mic_button.clicked.connect(self.start_mic)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Mesajınızı yazın veya konuşun…")
        self.input_box.returnPressed.connect(self.ask_ai)

        send_btn = QPushButton("Gönder")
        send_btn.clicked.connect(self.ask_ai)

        layout.addWidget(self.mic_button)
        layout.addWidget(self.input_box)
        layout.addWidget(send_btn)

        self.main_layout.addLayout(layout)

    def build_footer(self):
        label = QLabel("Running locally · Conversations stay on your device")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:#888;font-size:11px;")
        self.main_layout.addWidget(label)

    # ---------- CHAT ----------
    def clear_chat(self):
        while self.chat_layout.count():
            item = self.chat_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def add_message(self, text, sender):
        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(600)
        bubble.setFont(QFont("Segoe UI", 11))

        if sender == "user":
            bubble.setStyleSheet("background:#0078d7;color:white;padding:12px;border-radius:16px;")
        else:
            bubble.setStyleSheet("background:#2f2f2f;color:#eee;padding:12px;border-radius:16px;")

        row = QHBoxLayout()
        (row.addStretch(), row.addWidget(bubble)) if sender == "user" else (row.addWidget(bubble), row.addStretch())

        frame = QFrame()
        frame.setLayout(row)
        self.chat_layout.addWidget(frame)

    # ---------- MIC ----------
#“This feature will be added in the final version of the application.”

    # ---------- AI ----------
#“This feature will be added in the final version of the application.”


# ================== RUN ==================
app = QApplication(sys.argv)
window = ChatApp()
window.show()
sys.exit(app.exec_())












