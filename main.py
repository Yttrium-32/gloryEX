from PySide6.QtWidgets import QApplication

from pathlib import Path
import sys

from gui.main_window import MainWindow

app = QApplication(sys.argv)

logo_path = Path("data/assets/logo_32x32.png")

window = MainWindow(app)
window.show()

app.exec()

