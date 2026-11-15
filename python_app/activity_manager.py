"""
Module 2: Daily Activity and Meeting Management
Class: ActivityManager

Data structures (same as agreed with the team):

activity = {
    "title": "Statistics Class",
    "date": "2026-11-15",        # YYYY-MM-DD
    "start_time": "09:00",       # HH:MM (24-hour)
    "end_time": "11:00",
    "category": "Class"
}

meeting = {
    "title": "Project Meeting",
    "date": "2026-11-15",
    "start_time": "14:00",
    "end_time": "15:00",
    "location": "Library"
}
"""

from datetime import datetime


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def to_time(time_str):
    """Convert 'HH:MM' string to a datetime object (raises ValueError if bad)."""
    return datetime.strptime(time_str, "%H:%M")


def to_date(date_str):
    """Convert 'YYYY-MM-DD' string to a datetime object (raises ValueError if bad)."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def valid_inputs(date, start_time, end_time):
    """Check the date/time formats and that start is before end."""
    try:
        to_date(date)
        start = to_time(start_time)
        end = to_time(end_time)
    except ValueError:
        print("Error: use date format YYYY-MM-DD and time format HH:MM (24-hour).")
        return False
    if start >= end:
        print("Error: start time must be before end time.")
        return False
    return True


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------
class ActivityManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    # ----- Activities -------------------------------------------------------
    def add_activity(self, title, date, start_time, end_time, category):
        """Add a new activity. Returns True if added, False otherwise."""
        if not valid_inputs(date, start_time, end_time):
            return False

        activity = {
            "title": title,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "category": category,
        }
        self.data_manager.add_activity(activity)
        print(f"Activity '{title}' added on {date}.")

        # Warn the user if it clashes with something already scheduled
        for other in self.get_activities_by_date(date):
            if other is not activity and self.check_overlap(activity, other):
                print(f"  Warning: overlaps with '{other['title']}' "
                      f"({other['start_time']}-{other['end_time']}).")
        return True

    def get_activities_by_date(self, date):
        """Return a list of activities on a date, sorted by start time."""
        found = [
                a for a in self.data_manager.get_activities()
                if a["date"] == date
                ]
        return sorted(found, key=lambda a: a["start_time"])

    def display_activities(self, date):
        """Print all activities for the selected date."""
        activities = self.get_activities_by_date(date)
        print(f"\n--- Activities on {date} ---")
        if not activities:
            print("No activities scheduled.")
            return
        for i, a in enumerate(activities, start=1):
            print(f"{i}. {a['start_time']} - {a['end_time']} | "
                  f"{a['title']} [{a['category']}]")

    def find_activity(self, title, date):
        """Return the activity dict matching title + date, or None."""
        for a in self.data_manager.get_activities():
            if a["title"].lower() == title.lower() and a["date"] == date:
                return a
        return None

    def update_activity(self, title, date, new_title=None, new_date=None,
                        new_start=None, new_end=None, new_category=None):
        """Update any fields of an existing activity. Only given fields change."""
        activity = self.find_activity(title, date)
        if activity is None:
            print(f"Activity '{title}' on {date} not found.")
            return False

        # Work out the new values first, validate, then apply
        date_final = new_date or activity["date"]
        start_final = new_start or activity["start_time"]
        end_final = new_end or activity["end_time"]
        if not valid_inputs(date_final, start_final, end_final):
            return False

        activity["title"] = new_title or activity["title"]
        activity["date"] = date_final
        activity["start_time"] = start_final
        activity["end_time"] = end_final
        activity["category"] = new_category or activity["category"]
        self.data_manager.save_data()
        print(f"Activity '{title}' updated.")
        return True

    def cancel_activity(self, title, date):
        """Remove an activity from the schedule."""
        activity = self.find_activity(title, date)
        if activity is None:
            print(f"Activity '{title}' on {date} not found.")
            return False
        
        self.data_manager.get_activities().remove(activity)
        self.data_manager.save_data()
        print(f"Activity '{title}' on {date} cancelled.")
        return True

    # ----- Meetings ---------------------------------------------------------
    def add_meeting(self, title, date, start_time, end_time, location):
        """Add a new meeting. Returns True if added, False otherwise."""
        if not valid_inputs(date, start_time, end_time):
            return False

        meeting = {
            "title": title,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "location": location,
        }
        self.data_manager.add_meeting(meeting)
        print(f"Meeting '{title}' added on {date} at {location}.")
        return True

    def search_upcoming_meetings(self, from_date):
        """Print meetings on or after from_date (YYYY-MM-DD), earliest first."""
        try:
            to_date(from_date)
        except ValueError:
            print("Error: use date format YYYY-MM-DD.")
            return []

        upcoming = [
                     m for m in self.data_manager.get_meetings()
                    if m["date"] >= from_date
                    ]
        upcoming.sort(key=lambda m: (m["date"], m["start_time"]))

        print(f"\n--- Upcoming meetings from {from_date} ---")
        if not upcoming:
            print("No upcoming meetings.")
        for m in upcoming:
            print(f"{m['date']} {m['start_time']}-{m['end_time']} | "
                  f"{m['title']} @ {m['location']}")
        return upcoming

    # ----- Conflict checking ------------------------------------------------
    def check_overlap(self, item1, item2):
        """
        Return True if two items (activities or meetings) on the same day overlap.
        Two time ranges overlap when each one starts before the other ends.
        Back-to-back items (11:00 end, 11:00 start) do NOT count as overlap.
        """
        if item1["date"] != item2["date"]:
            return False
        start1, end1 = to_time(item1["start_time"]), to_time(item1["end_time"])
        start2, end2 = to_time(item2["start_time"]), to_time(item2["end_time"])
        return start1 < end2 and start2 < end1

    def find_conflicts(self, date):
        """Print every pair of activities/meetings that overlap on a date."""
        items = (
                self.get_activities_by_date(date)
                +
                [
                m for m in self.data_manager.get_meetings()
                if m["date"] == date
                ]
            )

        print(f"\n--- Conflicts on {date} ---")
        found = False
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if self.check_overlap(items[i], items[j]):
                    print(f"CONFLICT: '{items[i]['title']}' "
                          f"({items[i]['start_time']}-{items[i]['end_time']}) overlaps "
                          f"'{items[j]['title']}' "
                          f"({items[j]['start_time']}-{items[j]['end_time']})")
                    found = True
        if not found:
            print("No conflicts.")
        return found
