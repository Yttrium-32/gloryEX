from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget

from os import PathLike
from pathlib import Path

CARD_TITLE_STYLE = """
    background-color: #8e44ad;
    border-radius: 10px;
    color: #fff;
    font-size: 18pt;
    font-weight: bold;
"""

CARD_BODY_STYLE = """
    padding: 15px;
    border-radius: 10px;
    background-color: #9b59b6;
    color: #333;
"""

class CardWidget(QWidget):
    def __init__(self, title: str, description: str, image_path: PathLike | None = None):
        super().__init__()
        self.setWindowTitle("Text Card with Image")
        self.setWindowIcon(QIcon("../assets/logo_32x32.png"))
        self.setMinimumSize(QSize(300, 0))
        self.setMaximumSize(QSize(500, 500))

        card_title = QLabel(title)
        card_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        card_title.setAlignment(Qt.AlignCenter)
        card_title.setMaximumHeight(60)
        card_title.setStyleSheet(CARD_TITLE_STYLE)

        card_body = QLabel(description)
        card_body.setAlignment(Qt.AlignCenter)
        card_body.setWordWrap(True)
        card_body.setStyleSheet(CARD_BODY_STYLE)

        card_body_layout = QHBoxLayout()
        card_body_layout.addWidget(card_body)

        if image_path is not None:
            image_label = QLabel()
            image_label.setPixmap(QPixmap(image_path))
            image_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            card_body_layout.addWidget(image_label)

        card_layout = QVBoxLayout()

        card_layout.addWidget(card_title)
        card_layout.addLayout(card_body_layout)

        self.setLayout(card_layout)

if __name__ == "__main__":
    app = QApplication()

    body = "This is a long a complex body used for testing in a card body."
    image_path = Path("../assets/logo_128x128.png")

    card_widget = CardWidget("Test Title", body)
    card_widget.show()

    image_card_widget = CardWidget("Test Title", body, image_path.resolve())
    image_card_widget.show()

    app.exec()
