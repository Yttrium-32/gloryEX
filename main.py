from PySide6.QtWidgets import QApplication
import sys

from gui.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()

