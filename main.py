"""
Dinner Guest list
- Add guest.
- Modify guest.
- Remove guest.
- Sort guests.
- Show number of guests.
- Show invitations.
"""
guest_names = []

def add_guest():
    """Add a guest to the list."""
    name = input("Enter guest name: ").title().strip()

    # Check for empty name
    if name == "":
        print("Name cannot be empty.")
        return

    # Check for duplicate names
    if name in guest_names:
        print("That guest is already on the list.")
        return
    guest_names.append(name)
    print(f"{name} added to the guest list.")

def modify_guest():
    """Modify an existing guest name."""
    name = input("Enter guest name to modify: ").title().strip()

    if name in guest_names:
        index = guest_names.index(name)
        new_name = input("Enter the new name: ").title().strip()

        if new_name == "":
            print("Name cannot be empty.")
            return

        if new_name in guest_names:
            print("Duplicate names are not allowed.")
            return

        guest_names[index] = new_name
        print("Guest name updated.")
    else:
        print("Guest not found.")

def remove_guest():
    """Remove a guest from the list."""
    name = input("Enter guest name to remove: ").title().strip()

    if name in guest_names:
        index = guest_names.index(name)
        guest_names.pop(index)
        print("Guest removed.")
    else:
        print("No guest by that name.")

def sort_guests():
    """Sort guests alphabetically."""
    if not guest_names:
        print("No guests to sort.")
        return

    guest_names.sort()
    print("Guest list sorted alphabetically.")

def show_guest_count():
      """Show total number of guests."""
      print(f"Number of guests: {len(guest_names)}")

def show_invitations():
    """Display invitation messages."""
    if not guest_names:
        print("No guests to invite.")
        return

    print("\nInvitations:")
    for index in range(len(guest_names)):
        print(f"Dear {guest_names[index]}, you are invited to the event!") 

def main():
    """
    Main program loop
    """

    print("Welcome to the Guest Invitation App!")

    while True:
        print("\nPlease choose an option:")
        print("1 - Add guest")
        print("2 - Modify guest")
        print("3 - Remove guest")
        print("4 - Sort guests")
        print("5 - Show number of guests")
        print("6 - Show invitations")
        print("0 - Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_guest()
        elif choice == "2":
            modify_guest()
        elif choice == "3":
            remove_guest()
        elif choice == "4":
            sort_guests()
        elif choice == "5":
            show_guest_count()
        elif choice == "6":
            show_invitations()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
       