import json
from pathlib import Path


class DataManager:

    def __init__(self, file_path=None):

        if file_path is None:
            self.file_path = Path(__file__).with_name("calendar_data.json")
        else:
            self.file_path = Path(file_path)

        self.data = {
            "users": {
                "ali": "1234"
            },
            "activities": [],
            "meetings": [],
            "notes": []
        }

        self.load_data()


    def load_data(self):

        if self.file_path.exists():

            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)

                for key in self.data:
                    if key in saved_data:
                        self.data[key] = saved_data[key]

            except (json.JSONDecodeError, OSError):
                print("Could not load saved data. Using default data.")

        return self.data


    def save_data(self):

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)


    # -----------------------
    # USERS
    # -----------------------

    def get_users(self):
        return self.data["users"]


    # -----------------------
    # ACTIVITIES
    # -----------------------

    def get_activities(self):
        return self.data["activities"]


    def add_activity(self, activity):
        self.data["activities"].append(activity)
        self.save_data()


    def update_activity(self, index, activity):
        self.data["activities"][index] = activity
        self.save_data()


    def delete_activity(self, index):
        del self.data["activities"][index]
        self.save_data()


    # -----------------------
    # MEETINGS
    # -----------------------

    def get_meetings(self):
        return self.data["meetings"]


    def add_meeting(self, meeting):
        self.data["meetings"].append(meeting)
        self.save_data()


    def update_meeting(self, index, meeting):
        self.data["meetings"][index] = meeting
        self.save_data()


    def delete_meeting(self, index):
        del self.data["meetings"][index]
        self.save_data()


    # -----------------------
    # NOTES
    # -----------------------

    def get_notes(self):
        return self.data["notes"]


    def add_note(self, note):
        self.data["notes"].append(note)
        self.save_data()


    def update_note(self, index, note):
        self.data["notes"][index] = note
        self.save_data()


    def delete_note(self, index):
        del self.data["notes"][index]
        self.save_data()
