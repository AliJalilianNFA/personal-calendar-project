from data_manager import DataManager
from login import LoginSystem
from activity_manager import ActivityManager
from notes_manager import NotesManager


def show_menu():

    print("\n================================")
    print("     PERSONAL CALENDAR")
    print("================================")

    print("\n--- Activities ---")
    print("1. Add Activity")
    print("2. Display Activities by Date")
    print("3. Update Activity")
    print("4. Cancel Activity")

    print("\n--- Meetings ---")
    print("5. Add Meeting")
    print("6. Search Upcoming Meetings")
    print("7. Check Schedule Conflicts")

    print("\n--- Notes ---")
    print("8. Create Note")
    print("9. Display Notes")
    print("10. Search Notes")
    print("11. Update Note")
    print("12. Delete Note")

    print("\n--- Schedule Summary ---")
    print("13. Daily Summary")
    print("14. Weekly Summary")

    print("\n0. Exit")


def main():

    # Create shared data manager
    data_manager = DataManager()

    # Create objects from each module
    login_system = LoginSystem(data_manager)
    activity_manager = ActivityManager(data_manager)
    notes_manager = NotesManager(data_manager)

    # --------------------------
    # LOGIN
    # --------------------------

    if not login_system.login():
        print("Access denied.")
        return

    # --------------------------
    # MAIN MENU
    # --------------------------

    while True:

        show_menu()

        choice = input("\nEnter your choice: ").strip()

        # ==========================
        # ACTIVITIES
        # ==========================

        if choice == "1":

            print("\n--- Add Activity ---")

            title = input("Title: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            start_time = input("Start time (HH:MM): ").strip()
            end_time = input("End time (HH:MM): ").strip()
            category = input("Category: ").strip()

            activity_manager.add_activity(
                title,
                date,
                start_time,
                end_time,
                category
            )

        elif choice == "2":

            date = input(
                "Enter date (YYYY-MM-DD): "
            ).strip()

            activity_manager.display_activities(
                date
            )

        elif choice == "3":

            print("\n--- Update Activity ---")

            title = input(
                "Current activity title: "
            ).strip()

            date = input(
                "Current date (YYYY-MM-DD): "
            ).strip()

            print(
                "Press Enter to keep the current value."
            )

            new_title = input(
                "New title: "
            ).strip() or None

            new_date = input(
                "New date (YYYY-MM-DD): "
            ).strip() or None

            new_start = input(
                "New start time (HH:MM): "
            ).strip() or None

            new_end = input(
                "New end time (HH:MM): "
            ).strip() or None

            new_category = input(
                "New category: "
            ).strip() or None

            activity_manager.update_activity(
                title,
                date,
                new_title,
                new_date,
                new_start,
                new_end,
                new_category
            )

        elif choice == "4":

            title = input(
                "Activity title to cancel: "
            ).strip()

            date = input(
                "Activity date (YYYY-MM-DD): "
            ).strip()

            activity_manager.cancel_activity(
                title,
                date
            )

        # ==========================
        # MEETINGS
        # ==========================

        elif choice == "5":

            print("\n--- Add Meeting ---")

            title = input(
                "Meeting title: "
            ).strip()

            date = input(
                "Date (YYYY-MM-DD): "
            ).strip()

            start_time = input(
                "Start time (HH:MM): "
            ).strip()

            end_time = input(
                "End time (HH:MM): "
            ).strip()

            location = input(
                "Location: "
            ).strip()

            activity_manager.add_meeting(
                title,
                date,
                start_time,
                end_time,
                location
            )

        elif choice == "6":

            date = input(
                "Show meetings from date "
                "(YYYY-MM-DD): "
            ).strip()

            activity_manager.search_upcoming_meetings(
                date
            )

        elif choice == "7":

            date = input(
                "Check conflicts for date "
                "(YYYY-MM-DD): "
            ).strip()

            activity_manager.find_conflicts(
                date
            )

        # ==========================
        # NOTES
        # ==========================

        elif choice == "8":

            notes_manager.create_note()

        elif choice == "9":

            notes_manager.display_notes()

        elif choice == "10":

            notes_manager.search_notes()

        elif choice == "11":

            notes_manager.update_note()

        elif choice == "12":

            notes_manager.delete_note()

        # ==========================
        # SUMMARY
        # ==========================

        elif choice == "13":

            notes_manager.daily_summary()

        elif choice == "14":

            notes_manager.weekly_summary()

        # ==========================
        # EXIT
        # ==========================

        elif choice == "0":

            print(
                "\nThank you for using "
                "Personal Calendar."
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select a valid option."
            )


if __name__ == "__main__":
    main()
