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