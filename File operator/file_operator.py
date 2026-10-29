
import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        if not filename.endswith(".txt"):
            raise ValueError("Only .txt files are allowed.")

        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ").strip()

            if not entry:
                print("Journal entry cannot be empty!")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append mode creates the file if it does not exist.
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n{entry}\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")

        except OSError as error:
            print(f"File error: {error}")

    def view_entries(self):
        try:
            # Read mode is used to display saved entries.
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if content.strip():
                print("\nYour Journal Entries:")
                print("-" * 40)
                print(content)
            else:
                print("Your journal is empty. Add a new entry first.")

        except FileNotFoundError:
            print(
                "Error: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("Error: Permission denied while reading the file.")

        except OSError as error:
            print(f"File error: {error}")

    def search_entry(self):
        try:
            keyword = input(
                "\nEnter a keyword or date to search: "
            ).strip()

            if not keyword:
                print("Search keyword cannot be empty!")
                return

            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            entries = [
                entry.strip()
                for entry in content.split("\n\n")
                if entry.strip()
            ]

            matches = [
                entry for entry in entries
                if keyword.lower() in entry.lower()
            ]

            if matches:
                print("\nMatching Entries:")
                print("-" * 40)

                for entry in matches:
                    print(entry)
                    print()

            else:
                print(
                    f"No entries were found for the keyword: {keyword}"
                )

        except FileNotFoundError:
            print(
                "Error: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("Error: Permission denied while reading the file.")

        except OSError as error:
            print(f"File error: {error}")

    def delete_all_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? "
                "(yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                # Write mode clears the file's contents.
                # The file is then removed from the directory.
                with open(self.filename, "w", encoding="utf-8"):
                    pass

                os.remove(self.filename)
                print("All journal entries have been deleted.")

            elif confirmation == "no":
                print("Deletion cancelled.")

            else:
                print("Invalid confirmation. Please enter yes or no.")

        except PermissionError:
            print("Error: Permission denied while deleting the file.")

        except OSError as error:
            print(f"File error: {error}")

    def run(self):
        print("Welcome to Personal Journal Manager!")

        while True:
            print("\nPlease select an option:")
            print("\n1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_all_entries()

            elif choice == "5":
                print(
                    "\nThank you for using Personal Journal Manager. "
                    "Goodbye!"
                )
                break

            else:
                print(
                    "Invalid option. Please select a valid option "
                    "from the menu."
                )


if __name__ == "__main__":
    journal = JournalManager()
    journal.run()
