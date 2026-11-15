from datetime import datetime, timedelta


class NotesManager:

    def __init__(self, data_manager):
        self.data_manager = data_manager


    # -----------------------
    # CREATE NOTE
    # -----------------------

    def create_note(self):

        title = input("Enter note title: ").strip()
        content = input("Enter note content: ").strip()
        date = input("Enter note date (YYYY-MM-DD): ").strip()

        if title == "" or content == "":
            print("Title and content cannot be empty.")
            return

        if not self.valid_date(date):
            print("Invalid date format.")
            return

        note = {
            "title": title,
            "content": content,
            "date": date
        }

        self.data_manager.add_note(note)

        print("Note created successfully.")


    # -----------------------
    # DISPLAY NOTES
    # -----------------------

    def display_notes(self):

        notes = self.data_manager.get_notes()

        if len(notes) == 0:
            print("No notes found.")
            return

        print("\n===== Saved Notes =====")

        for index, note in enumerate(notes, start=1):

            print(
                f"{index}. {note['title']} | {note['date']}"
            )

            print(
                f"   {note['content']}"
            )


    # -----------------------
    # SEARCH NOTES
    # -----------------------

    def search_notes(self):

        keyword = input(
            "Enter title or keyword: "
        ).strip().lower()

        notes = self.data_manager.get_notes()

        found = False

        for note in notes:

            if (
                keyword in note["title"].lower()
                or
                keyword in note["content"].lower()
            ):

                print(
                    f"{note['title']} | "
                    f"{note['date']} | "
                    f"{note['content']}"
                )

                found = True

        if not found:
            print("No matching note found.")


    # -----------------------
    # UPDATE NOTE
    # -----------------------

    def update_note(self):

        notes = self.data_manager.get_notes()

        if len(notes) == 0:
            print("No notes available.")
            return

        self.display_notes()

        try:
            number = int(
                input("Enter note number to update: ")
            )

        except ValueError:
            print("Invalid number.")
            return

        index = number - 1

        if index < 0 or index >= len(notes):
            print("Invalid note number.")
            return

        old_note = notes[index]

        title = input(
            f"New title [{old_note['title']}]: "
        ).strip()

        content = input(
            f"New content [{old_note['content']}]: "
        ).strip()

        date = input(
            f"New date [{old_note['date']}]: "
        ).strip()

        if title == "":
            title = old_note["title"]

        if content == "":
            content = old_note["content"]

        if date == "":
            date = old_note["date"]

        if not self.valid_date(date):
            print("Invalid date format.")
            return

        updated_note = {
            "title": title,
            "content": content,
            "date": date
        }

        self.data_manager.update_note(
            index,
            updated_note
        )

        print("Note updated successfully.")


    # -----------------------
    # DELETE NOTE
    # -----------------------

    def delete_note(self):

        notes = self.data_manager.get_notes()

        if len(notes) == 0:
            print("No notes available.")
            return

        self.display_notes()

        try:
            number = int(
                input("Enter note number to delete: ")
            )

        except ValueError:
            print("Invalid number.")
            return

        index = number - 1

        if index < 0 or index >= len(notes):
            print("Invalid note number.")
            return

        self.data_manager.delete_note(index)

        print("Note deleted successfully.")


    # -----------------------
    # DAILY SUMMARY
    # -----------------------

    def daily_summary(self):

        date = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        if not self.valid_date(date):
            print("Invalid date format.")
            return

        activities = []

        meetings = []

        for activity in self.data_manager.get_activities():

            if activity.get("date") == date:
                activities.append(activity)

        for meeting in self.data_manager.get_meetings():

            if meeting.get("date") == date:
                meetings.append(meeting)

        total_hours = (
            self.calculate_hours(activities)
            +
            self.calculate_hours(meetings)
        )

        print("\n===== Daily Summary =====")
        print(f"Activities: {len(activities)}")
        print(f"Meetings: {len(meetings)}")
        print(
            f"Total scheduled items: "
            f"{len(activities) + len(meetings)}"
        )
        print(
            f"Total scheduled hours: "
            f"{total_hours:.2f}"
        )


    # -----------------------
    # WEEKLY SUMMARY
    # -----------------------

    def weekly_summary(self):

        start_date = input(
            "Enter week start date (YYYY-MM-DD): "
        ).strip()

        if not self.valid_date(start_date):
            print("Invalid date format.")
            return

        start = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        ).date()

        end = start + timedelta(days=6)

        activities = []

        meetings = []

        for activity in self.data_manager.get_activities():

            if self.date_in_range(
                activity.get("date"),
                start,
                end
            ):

                activities.append(activity)

        for meeting in self.data_manager.get_meetings():

            if self.date_in_range(
                meeting.get("date"),
                start,
                end
            ):

                meetings.append(meeting)

        total_hours = (
            self.calculate_hours(activities)
            +
            self.calculate_hours(meetings)
        )

        print("\n===== Weekly Summary =====")
        print(f"Week: {start} to {end}")
        print(f"Activities: {len(activities)}")
        print(f"Meetings: {len(meetings)}")
        print(
            f"Total scheduled items: "
            f"{len(activities) + len(meetings)}"
        )
        print(
            f"Total scheduled hours: "
            f"{total_hours:.2f}"
        )


    # -----------------------
    # CALCULATE HOURS
    # -----------------------

    def calculate_hours(self, items):

        total_hours = 0

        for item in items:

            start_time = item.get("start_time")
            end_time = item.get("end_time")

            if not start_time or not end_time:
                continue

            try:

                start = datetime.strptime(
                    start_time,
                    "%H:%M"
                )

                end = datetime.strptime(
                    end_time,
                    "%H:%M"
                )

                if end > start:

                    duration = (
                        end - start
                    ).total_seconds() / 3600

                    total_hours += duration

            except ValueError:
                continue

        return total_hours


    # -----------------------
    # DATE VALIDATION
    # -----------------------

    def valid_date(self, date):

        try:

            datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            return True

        except ValueError:
            return False


    def date_in_range(
        self,
        date,
        start,
        end
    ):

        try:

            current_date = datetime.strptime(
                date,
                "%Y-%m-%d"
            ).date()

            return start <= current_date <= end

        except:
            return False
