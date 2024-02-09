from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from pathlib import Path
import requests, json

API_URL = "http://0.0.0.0:8000"

if __name__ == "__main__":
    TOKENS_FILE_PATH = Path("../token.json")
else:
    TOKENS_FILE_PATH = Path("token.json")

class SkillsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skills Page")
        skills_list = SkillsPage.get_skills_list()

        no_entries_label = QLabel("No skills found")
        no_entries_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        if skills_list == []:
            mainV_layout = QVBoxLayout()
            mainH_layout = QHBoxLayout()
            mainH_layout.addWidget(no_entries_label)
            mainV_layout.addLayout(mainH_layout)
            self.setLayout(mainV_layout)

    def get_skills_list() -> list[dict] | None:
        if TOKENS_FILE_PATH.is_file():
            with open(str(TOKENS_FILE_PATH.resolve()), "r") as tokens_file:
                credentials = json.load(tokens_file)
                user_id: int = credentials["id"]
                try:
                    response = requests.get(API_URL + f"/users/{user_id}/get_skill")
                    json_data: list[dict] = json.loads(response.text)
                    print(f"{json_data=}")

                    for entry in json_data:
                        del entry["id"], entry["user_id"]
                        if entry["certificate_image_path"] is not None:
                            entry["image_path"] = "backend/" + entry.pop("certificate_image_path")
                        else:
                            del entry["certificate_image_path"]

                    print(f"cleaned_json_data={json_data}")
                    return json_data
                except requests.exceptions.ConnectionError:
                    print("Api not running")
                    return None
        else:
            print("Not logged in")
            return None

if __name__ == "__main__":
    app = QApplication()
    skills_page = SkillsPage()
    skills_page.show()
    app.exec()

