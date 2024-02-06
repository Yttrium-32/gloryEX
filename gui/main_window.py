from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar

from pathlib import Path

LOGO_PATH = Path("assets/logo_32x32.png")

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("GloryEX")
        self.setMinimumSize(QSize(809, 500))
        icon = QIcon(str(LOGO_PATH.resolve()))
        self.setWindowIcon(icon)

        tool_bar = QToolBar()
        tool_bar.setMovable(False)
        tool_bar.setFloatable(False)
        self.addToolBar(Qt.LeftToolBarArea, tool_bar)

        login_page = QAction("Login", self)
        tool_bar.addAction(login_page)

        skills_page = QAction("Skills", self)
        tool_bar.addAction(skills_page)


