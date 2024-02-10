from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget

from pathlib import Path
import requests, json

try:
    from gui.cards import CardWidget
except ImportError:
    from cards import CardWidget

API_URL = "http://0.0.0.0:8000"

if __name__ == "__main__":
    TOKENS_FILE_PATH = Path("../data/token.json")
else:
    TOKENS_FILE_PATH = Path("data/token.json")

class SkillsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skills Page")
        self.setMinimumSize(400, 300)
        skills_list = SkillsPage.get_skills_list()

        if skills_list == [] or skills_list is None:
            no_entries_label = QLabel("No skills found\nor\nAPI not running")
            no_entries_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            main_layout = QVBoxLayout()
            main_layout.addWidget(no_entries_label)
            main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.setLayout(main_layout)

        else:
            grid_layout = QGridLayout()

            # Add two widgets per column
            row, col = 0, 0
            for entry in skills_list:
                card_widget = CardWidget(**entry)
                grid_layout.addWidget(card_widget, row, col)
                # Increment col for every widget added
                col += 1

                # Reset col after adding two widgets
                if col == 2:
                    # Go to next row after two widgets
                    row += 1
                    col = 0

            grid_widget = QWidget()
            grid_widget.setLayout(grid_layout)
            
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(grid_widget)

            main_layout = QVBoxLayout()
            main_layout.addWidget(scroll_area)

            self.setLayout(main_layout)

    def get_skills_list() -> list[dict] | None:
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

                json_data = SkillsPage.clean_json_data(json_data)

                print(f"cleaned_json_data={json_data}")
                return json_data
            except requests.exceptions.ConnectionError:
                print("Api not running")
                return None

    def clean_json_data(json_data: list[dict]) -> list[dict]:
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
        

if __name__ == "__main__":
    app = QApplication()
    skills_page = SkillsPage()
    skills_page.show()
    app.exec()

