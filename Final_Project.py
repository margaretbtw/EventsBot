import datetime

events = []

def greet_user():
    print("Hi there! I'm your personal Event Organizer. How can I help you today?")

def display_help():
    """Displays a list of available commands."""
    print("\n--- Available Commands ---")
    print("help - show this list of commands")
    print("add event - add a new event")
    print("show events - view all scheduled events")
    print("weekly events - events for the current week")
    print("search by category - find events by category")
    print("delete event - delete an event")
    print("exit - end the bot's operation")
    print("--------------------------\n")

def add_event():
    while True:
        name = input("Enter the event name: ").strip()
        if name:
            break
        else:
            print("Event name cannot be empty. Please try again.")

    while True:
        date_str = input("Enter the event date (YYYY-MM-DD): ").strip()
        try:
            year, month, day = map(int, date_str.split('-'))
            event_date = datetime.date(year, month, day)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    description = input("Enter a short description for the event: ").strip()

    available_categories = ['Study', 'Meeting', 'Exam', 'Work', 'Personal', 'Other']
    print("\nChoose a category or enter a new one:")
    for i, cat in enumerate(available_categories):
        print(f"{i+1}. {cat}")

    while True:
        category_choice = input("Enter the category number or your own category: ").strip()
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(available_categories):
            category = available_categories[int(category_choice) - 1]
            break
        elif category_choice:
            category = category_choice
            break
        else:
            print("Category choice cannot be empty. Please try again.")


    event = {
        'name': name,
        'date': event_date,
        'description': description,
        'category': category
    }
    events.append(event)
    print(f"Event '{name}' successfully added!")

def show_events(event_list=None):
    if event_list is None:
        event_list = events

    if not event_list:
        print("The event list is empty.")
        return

    print("\n--- Your Events ---")
    for i, event in enumerate(event_list):
        print(f"{i+1}. Name: {event['name']}, Date: {event['date']}, Category: {event['category']}")
        if event['description']:
            print(f"    Description: {event['description']}")
    print("-------------------\n")

def show_weekly_events():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    weekly_events = [
        event for event in events
        if start_of_week <= event['date'] <= end_of_week
    ]

    if not weekly_events:
        print("No events scheduled for this week.")
    else:
        print(f"\n--- Events for the week ({start_of_week} - {end_of_week}) ---")
        show_events(weekly_events)

def search_by_category():
    category = input("Enter the category to search for: ").strip()
    filtered_events = [event for event in events if event['category'].lower() == category.lower()]

    if not filtered_events:
        print(f"No events found for category '{category}'.")
    else:
        print(f"\n--- Events by category '{category}' ---")
        show_events(filtered_events)

def delete_event():
    name_to_delete = input("Enter the name of the event you want to delete: ").strip()
    date_str_to_delete = input("Enter the date of the event (YYYY-MM-DD) you want to delete: ").strip()

    try:
        year, month, day = map(int, date_str_to_delete.split('-'))
        date_to_delete = datetime.date(year, month, day)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    global events
    original_len = len(events)

    events = [
        event for event in events
        if not (event['name'].lower() == name_to_delete.lower() and event['date'] == date_to_delete)
    ]

    if len(events) < original_len:
        print(f"Event '{name_to_delete}' on {date_str_to_delete} successfully deleted.")
    else:
        print(f"Event '{name_to_delete}' on {date_str_to_delete} not found.")

def main():
    greet_user()
    while True:
        command = input("Enter a command ('help' for a list of commands): ").lower().strip()
        if command == "help":
            display_help()
        elif command == "add event":
            add_event()
        elif command == "show events":
            show_events()
        elif command == "weekly events":
            show_weekly_events()
        elif command == "search by category":
            search_by_category()
        elif command == "delete event":
            delete_event()
        elif command == "exit":
            print("Thanks for using the Event Organizer Bot! Goodbye!")
            break
        else:
            print("Unknown command. Please enter 'help' to see the list of commands.")

if __name__ == "__main__":
    main()