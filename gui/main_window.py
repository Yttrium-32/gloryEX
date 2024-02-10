from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow
from PySide6.QtWidgets import QStackedWidget, QToolBar, QWidget

try:
    from gui.login_page import LoginPage
    from gui.skills_page import SkillsPage
    from gui.config import LOGO_PATH
except ImportError:
    from login_page import LoginPage
    from skills_page import SkillsPage
    from config import LOGO_PATH

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

        login_page_action = QAction("Login", self)
        login_page_action.triggered.connect(self.cycle_to_login_page)
        tool_bar.addAction(login_page_action)

        skills_page_action = QAction("Skills", self)
        skills_page_action.triggered.connect(self.cycle_to_skills_page)
        tool_bar.addAction(skills_page_action)

        login_widget = LoginPage()
        skills_widget = SkillsPage()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(login_widget)
        self.stacked_widget.addWidget(skills_widget)
        self.stacked_widget.setCurrentIndex(0)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def cycle_to_skills_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.stacked_widget.update()

    def cycle_to_login_page(self):
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.update()

if __name__ == "__main__":
    app = QApplication()

    main_window = MainWindow(app)
    main_window.show()

    app.exec()

