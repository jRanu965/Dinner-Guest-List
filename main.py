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
guest_meals = []

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
    