from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget

from pathlib import Path
import requests, json

try:
    from gui.cards import CardWidget
    from gui.config import API_URL, TOKENS_FILE_PATH
except ImportError:
    from cards import CardWidget
    from config import API_URL, TOKENS_FILE_PATH

API_URL = "http://0.0.0.0:8000"

if __name__ == "__main__":
    TOKENS_FILE_PATH = ".." / TOKENS_FILE_PATH

class SkillsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skills Page")
        self.setMinimumSize(400, 300)

        self.grid_layout = QGridLayout()

        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.grid_widget)

        update_button = QPushButton("Update cards")
        update_button.clicked.connect(self.add_widget_contents)

        main_layout = QVBoxLayout()
        main_layout.addWidget(update_button)
        main_layout.addWidget(self.scroll_area)

        self.add_widget_contents()

        self.setLayout(main_layout)

    def get_skills_list(self) -> list[dict] | None:
        if not TOKENS_FILE_PATH.is_file():
            print("Not logged in")
            return None

        with open(str(TOKENS_FILE_PATH.resolve()), "r") as tokens_file:
            credentials = json.load(tokens_file)
            user_id: int = credentials["id"]
            try:
                response = requests.get(API_URL + f"/users/{user_id}/get_skill")
                json_data: list[dict] = json.loads(response.text)
                print(f"{json_data=}")

                json_data = self.clean_json_data(json_data)

                print(f"cleaned_json_data={json_data}")
                return json_data

            except requests.exceptions.ConnectionError:
                print("Api not running")
                return None

    def clean_json_data(self, json_data: list[dict]) -> list[dict]:
        # TODO: Remove hard coded path for images
        if __name__ == "__main__":
            backend_path = "../backend/"
        else:
            backend_path = "backend/"
        for entry in json_data:
            del entry["id"], entry["user_id"]
            if entry["certificate_image_path"] is not None:
                new_image_path = backend_path + entry.pop("certificate_image_path")
                entry["image_path"] = Path(new_image_path).resolve()
            else:
                del entry["certificate_image_path"]

        return json_data

    def clear_grid_layout(self):
        # Remove existing widgets from the layout
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

    def add_widget_contents(self):
        self.skills_list = self.get_skills_list()
        self.clear_grid_layout()

        if self.skills_list == [] or self.skills_list is None:
            no_entries_label = QLabel("No skills found\nor\nAPI not running")
            no_entries_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.grid_layout.addWidget(no_entries_label, 0, 0)

        else:
            # Add two widgets per column
            row, col = 0, 0
            for entry in self.skills_list:
                card_widget = CardWidget(**entry)
                self.grid_layout.addWidget(card_widget, row, col)
                # Increment col for every widget added
                col += 1

                # Reset col after adding two widgets
                if col == 2:
                    # Go to next row after two widgets
                    row += 1
                    col = 0

if __name__ == "__main__":
    app = QApplication()
    skills_page = SkillsPage()
    skills_page.show()
    app.exec()

