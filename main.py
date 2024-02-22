from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading


# Frontend
class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(40, 40, 480, 320)
        self.chat_area.setReadOnly(True)
        # Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(40, 370, 482, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add button
        self.button = QPushButton('send', self)
        self.button.setGeometry(530, 370, 90, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#EEBCE4'><span style='color:#F94ADB'>User:</span> {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color: #C6EEBC'><span style='color: #287928'>Bot:</span> {response}</p>")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
