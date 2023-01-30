import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from nltk.chat.util import Chat, reflections

class Chatbot(QWidget):
    def __init__(self):
        super().__init__()
        self.chatbot = Chat(pairs, reflections)

        self.label = QLabel("Welcome to the chatbot! How can I help you today?")
        self.input_text = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.get_response)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.setWindowTitle("Chatbot")
        self.show()

    def get_response(self):
        user_input = self.input_text.text()
        response = self.chatbot.respond(user_input)
        self.label.setText(response)
        self.input_text.clear()

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot, nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you for asking!"]
    ],
    [
        r"goodbye",
        ["Goodbye! Come back soon!"]
    ]
]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = Chatbot()
    sys.exit(app.exec_())