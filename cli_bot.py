import re
from typing import List, Dict, Tuple, Callable


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    args = parts[1].split() if len(parts) > 1 else []
    return cmd, args


# def validate_phone(phone: str) -> bool:
#     return bool(re.match(r'^\+?\d{10,15}$', phone))


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Error: Please provide both a name and a phone number."
    name, phone = args
    # if not validate_phone(phone):
    #     return "Error: Invalid phone number format."
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Error: Please provide both a name and a new phone number."
    name, phone = args
    # if not validate_phone(phone):
    #     return "Error: Invalid phone number format."
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Error: Contact not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return "Error: Please provide a name."
    name = args[0]
    return f"{name}: {contacts[name]}" if name in contacts else "Error: Contact not found."


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts: Dict[str, str] = {}
    commands: Dict[str, Callable[[List[str], Dict[str, str]], str]] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": lambda args, contacts: show_all(contacts)
    }

    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command in commands:
                print(commands[command](args, contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
