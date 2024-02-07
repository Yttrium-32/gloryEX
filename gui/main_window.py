#!/bin/python
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow
from PySide6.QtWidgets import QStackedWidget, QToolBar, QWidget

try:
    from gui.login_page import LoginPage
    from gui.skills_page import SkillsPage
except ImportError:
    from login_page import LoginPage
    from skills_page import SkillsPage

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

        login_widget = LoginPage()
        skills_widget = SkillsPage()

        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(login_widget)
        stacked_widget.addWidget(skills_widget)

        main_layout = QHBoxLayout()
        main_layout.addWidget(stacked_widget)
        main_layout.setAlignment(Qt.AlignCenter)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication()

    main_window = MainWindow(app)
    main_window.show()

    app.exec()

