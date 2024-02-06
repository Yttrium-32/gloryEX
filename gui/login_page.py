from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QSizePolicy, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout

from pathlib import Path

LOGO_PATH = Path("../assets/logo_128x128.png")

LOGO_STYLE = """
    padding: 30px;
    margin-bottom: 25px;
"""

WELCOME_SIGN_STYLE = """
  color: #8e44ad;
  font-size: 24px;
"""

BUTTON_STYLE = """
  background-color: #8e44ad;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  margin-right: 5px;
"""

INPUT_FIELD_STYLE = """
    border: 1px solid #8e44ad;
"""

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setMinimumSize(QSize(405, 250))

        welcome_sign = QLabel("Welcome back!")
        welcome_sign.setMaximumHeight(50)
        welcome_sign.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        welcome_sign.setStyleSheet(WELCOME_SIGN_STYLE)

        password_input = QLineEdit()
        password_input.setPlaceholderText("Password")
        password_input.setStyleSheet(INPUT_FIELD_STYLE)

        username_input = QLineEdit()
        username_input.setPlaceholderText("Username")
        username_input.setStyleSheet(INPUT_FIELD_STYLE)

        login_button = QPushButton("Login")
        login_button.setStyleSheet(BUTTON_STYLE)

        register_button = QPushButton("Register")
        register_button.setStyleSheet(BUTTON_STYLE)

        logo_label = QLabel()
        logo_pixmap = QPixmap(LOGO_PATH.resolve())
        logo_label.setPixmap(logo_pixmap)
        logo_label.setStyleSheet(LOGO_STYLE)
        logo_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        login_layout = QGridLayout()
        login_layout.addWidget(username_input, 0, 0, 1, 3)
        login_layout.addWidget(password_input, 1, 0, 1, 3)
        login_layout.addWidget(login_button, 2, 0)
        login_layout.addWidget(register_button, 2, 2)

        login_wlogo_layout = QHBoxLayout()
        login_wlogo_layout.addLayout(login_layout)
        login_wlogo_layout.addWidget(logo_label)

        body_layout = QVBoxLayout()
        body_layout.addWidget(welcome_sign)
        body_layout.addLayout(login_wlogo_layout)

        self.setLayout(body_layout)

if __name__ == "__main__":
    app = QApplication()
    login_page = LoginPage()
    login_page.show()
    app.exec()

