import threading
from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, \
    QPushButton
from backend import Chatbot
import sys


class ChatbotWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smarty - Chatbot GPT")
        self.setMinimumSize(680, 400)

        # Add Chat Area Widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 300)
        self.chat_area.setReadOnly(True)

        # Add Chat Input Widget
        self.input_chat = QLineEdit(self)
        self.input_chat.setGeometry(10, 320, 480, 25)
        self.input_chat.returnPressed.connect(self.start_query)

        # Add Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 320, 50, 25)
        self.button.clicked.connect(self.start_query)

        self.show()

    def start_query(self):
        self.chatbot = Chatbot()
        self.query = self.input_chat.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>User: {self.query}")
        self.input_chat.clear()
        print(self.query)

        thread = threading.Thread(target=self.get_bot_response)
        thread.start()

    def get_bot_response(self):
        response = self.chatbot.get_response(self.query)
        print(response)
        self.chat_area.append(f"<p style='color:#333333; "
                              f"background-color:#E9E9E9'>Bot: {response}")


app = QApplication(sys.argv)
main_windows = ChatbotWindow()
sys.exit(app.exec())