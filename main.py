from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QLineEdit, \
    QPushButton
import sys


class ChatbotWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Chatbot GPT")
        self.setMinimumSize(680, 400)

        # Add Chat Area Widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 300)
        self.chat_area.setReadOnly(True)

        # Add Chat Input Widget
        self.input_chat = QLineEdit(self)
        self.input_chat.setGeometry(10, 320, 480, 25)

        # Add Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 320, 50, 25)

        self.show()



class Chatbot:
    pass


app = QApplication(sys.argv)
main_windows = ChatbotWindow()
sys.exit(app.exec())