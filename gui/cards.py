from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class CardWidget(QWidget):
    def __init__(self, title: str, content: str) -> None:
        super().__init__()
        self.setWindowTitle("Text Card")
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(500, 500))

        card_title = QLabel(title)
        card_title.setMaximumWidth(300)

        card_body = QLabel(content)
        card_body.setMaximumWidth(500)
        card_body.setWordWrap(True)

        card_layout = QVBoxLayout()
        card_layout.addWidget(card_title)
        card_layout.addWidget(card_body)

        self.setLayout(card_layout)

class CardImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        pass

if __name__ == "__main__":
    app = QApplication()
    body = "This is a long a complex body used for testing in a card body."
    card_widget = CardWidget("Test Title", body)
    card_widget.show()
    app.exec()
