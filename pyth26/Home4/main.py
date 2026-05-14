# Import the classes
from Date import Date
from Event import Event


# Main function
def main():

    # List to store all events
    events = []

    # Main program loop
    while True:

        # Display menu
        print("\nConvention Center Scheduler")
        print("1) Add an Event")
        print("2) Cancel an Event")
        print("3) View all Events")
        print("4) Quit")

        # Get user choice
        choice = input("Enter your choice: ")

        # =========================
        # Add Event
        # =========================
        if choice == "1":

            # Ask for event information
            name = input("Enter event name: ")

            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            year = int(input("Enter year: "))

            start_hour = int(input("Enter start hour (0-23): "))
            end_hour = int(input("Enter end hour (0-23): "))

            # Make sure start time is before end time
            if start_hour >= end_hour:

                print("Start hour must be less than end hour.")
                continue

            # Create Date object
            event_date = Date(month, day, year)

            # Create Event object
            new_event = Event(name, start_hour, end_hour, event_date)

            # Variable to track overlap
            overlap_found = False

            # Check all existing events
            for event in events:

                # Check if events are on same date
                if event.event_date == new_event.event_date:

                    # Check for time overlap
                    # Overlap happens when:
                    # new start < existing end
                    # AND new end > existing start
                    if (
                        new_event.start_hour < event.end_hour and
                        new_event.end_hour > event.start_hour
                    ):

                        print("\nCannot add event.")
                        print("This event overlaps with:")
                        print(event)

                        overlap_found = True
                        break

            # Add event only if no overlap
            if not overlap_found:

                events.append(new_event)
                print("Event added successfully.")

        # =========================
        # Cancel Event
        # =========================
        elif choice == "2":

            # Ask for event name
            cancel_name = input("Enter the name of the event to cancel: ")

            # Track if event was found
            found = False

            # Loop through all events
            for event in events:

                # Find matching event name
                if event.event_name == cancel_name:

                    # Remove the event
                    events.remove(event)

                    print("Event canceled.")

                    found = True
                    break

            # Event not found
            if not found:
                print("No event with that name was found.")

        # =========================
        # View Events
        # =========================
        elif choice == "3":

            # Check if list is empty
            if len(events) == 0:

                print("No events scheduled.")

            else:

                print("\nAll Scheduled Events:\n")

                # Print every event
                for event in events:

                    print(event)
                    print()

        # =========================
        # Quit
        # =========================
        elif choice == "4":

            print("Goodbye.")
            break

        # Invalid choice
        else:

            print("Invalid choice.")


# Start the program
main()