FILE_NAME = "to_do.txt"

print("\nWelcome in To_Do system\n")
def add_item():
    item = str(input("Type your new To-Do item: ")).strip()
    if item == "":
        print("Not saved, item is empty")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(item + "\n")
    print("Saved.")


def list_items():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            items = [line.strip() for line in f.readlines() if line.strip()]

        if not items:
            print("Your To-Do list is empty")
            return

        print("\nYour To-Do items:")
        for item in items:
            print(item)
        print()

    except FileNotFoundError:
        print("No To-Do file found yet")


def main():
    while True:
        ans = str(input('Do you want to add a new To-Do item? y - n or type exit: ')).strip().lower()

        if ans == "exit":
            print("thank you for using the To-Do system")
            break

        if ans == "y":
            add_item()

        elif ans == "n":
            ans2 = str(input('Do you want to list your To-Do items? y - n : ')).strip().lower()
            if ans2 == "y":
                list_items()
            elif ans2 == "n":
                pass
            else:
                print("Invalid input , Please enter y or n")
        else:
            print("Invalid input, Please enter y or n or exit")


if __name__ == "__main__":
    main()