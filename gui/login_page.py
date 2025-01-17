from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QSizePolicy, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout

from uuid import uuid4
import requests, json

try:
    from gui.config import LOGO_PATH, API_URL, TOKENS_FILE_PATH
    from gui.config import LOGO_STYLE, WELCOME_SIGN_STYLE
    from gui.config import INPUT_FIELD_STYLE, BUTTON_STYLE
except ImportError:
    from config import LOGO_PATH, API_URL, TOKENS_FILE_PATH
    from config import LOGO_STYLE, WELCOME_SIGN_STYLE
    from config import INPUT_FIELD_STYLE, BUTTON_STYLE

if __name__ == "__main__":
    LOGO_PATH = ".." / LOGO_PATH
    TOKENS_FILE_PATH = ".." / TOKENS_FILE_PATH

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setMinimumSize(QSize(405, 250))
        self.setMaximumSize(QSize(810, 500))
        icon = QIcon(str(LOGO_PATH.resolve()))
        self.setWindowIcon(icon)

        welcome_sign = QLabel("Welcome back!")
        welcome_sign.setMaximumHeight(50)
        welcome_sign.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        welcome_sign.setStyleSheet(WELCOME_SIGN_STYLE)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(INPUT_FIELD_STYLE)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(INPUT_FIELD_STYLE)

        login_button = QPushButton("Login")
        login_button.setStyleSheet(BUTTON_STYLE)
        login_button.clicked.connect(self.send_login_request)

        register_button = QPushButton("Register")
        register_button.setStyleSheet(BUTTON_STYLE)
        register_button.clicked.connect(self.send_register_request)

        logo_label = QLabel()
        logo_pixmap = QPixmap(LOGO_PATH.resolve())
        logo_label.setPixmap(logo_pixmap)
        logo_label.setStyleSheet(LOGO_STYLE)
        logo_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        login_layout = QGridLayout()
        login_layout.addWidget(self.username_input, 0, 0, 1, 3)
        login_layout.addWidget(self.password_input, 1, 0, 1, 3)
        login_layout.addWidget(login_button, 2, 0)
        login_layout.addWidget(register_button, 2, 2)

        login_wlogo_layout = QHBoxLayout()
        login_wlogo_layout.addLayout(login_layout)
        login_wlogo_layout.addWidget(logo_label)

        body_layout = QVBoxLayout()
        body_layout.addWidget(welcome_sign)
        body_layout.addLayout(login_wlogo_layout)

        self.setLayout(body_layout)

    def send_login_request(self):
        password = self.password_input.text()
        username = self.username_input.text()

        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(API_URL + "/users/verify/", data=json.dumps(payload))
            json_data = json.loads(response.text)
            print(f"{json_data=}")

            if response.status_code == 200:
                with open(TOKENS_FILE_PATH, "w") as token_file:
                    json.dump(json_data, token_file)
        except requests.exceptions.ConnectionError:
            print("Api not running")

    def send_register_request(self):
        password = self.password_input.text()
        username = self.username_input.text()

        payload = {
            "username": username,
            "email": f"mail-{uuid4()}@mail-server.org",
            "password": password
        }

        try:
            response = requests.post(API_URL + "/users/create/", data=json.dumps(payload))
            json_data = json.loads(response.text)
            print(f"{json_data=}")
        except requests.exceptions.ConnectionError:
            print("Api not running")

if __name__ == "__main__":
    app = QApplication()
    login_page = LoginPage()
    login_page.show()
    app.exec()

