from PySide6.QtWidgets import QApplication, QWidget

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
        SkillsPage.get_skills_list()

    def get_skills_list():
        if TOKENS_FILE_PATH.is_file():
            with open(str(TOKENS_FILE_PATH.resolve()), "r") as tokens_file:
                credentials = json.load(tokens_file)
                user_id: int = credentials["id"]
                try:
                    response = requests.get(API_URL + f"/users/{user_id}/get_skill")
                    json_data = json.loads(response.text)
                    print(f"{json_data=}")
                except requests.exceptions.ConnectionError:
                    print("Api not running")
        else:
            print("Not found")
            return None

if __name__ == "__main__":
    app = QApplication()
    skills_page = SkillsPage()
    skills_page.show()
    app.exec()
