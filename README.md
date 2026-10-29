# 📔 File Operator – Personal Journal Manager

## 📌 Project Overview

The **Personal Journal Manager** is a menu-driven Python application that allows users to create, view, search, and delete personal journal entries. It uses file handling to store journal entries permanently in a text file named `journal.txt`.

The project demonstrates Object-Oriented Programming (OOP), file handling operations, timestamps, and exception handling in Python.

## 🎯 Objectives

- Understand file handling in Python.
- Implement OOP concepts using classes and objects.
- Read and write data using text files.
- Use different file modes such as `r`, `w`, `a`, and `x`.
- Handle errors using exception handling.
- Build a menu-driven console application.

## ✨ Features

1. **Add a New Entry:** Write a journal entry with an automatically generated timestamp.
2. **View All Entries:** Display all previously saved journal entries.
3. **Search for an Entry:** Find entries using a keyword or date.
4. **Delete All Entries:** Delete the journal file after user confirmation.
5. **Exit:** Safely exit the application.
6. **Exception Handling:** Handle missing files, permission errors, and other file-related errors.
7. **Input Validation:** Display error messages for invalid menu options and empty entries.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** OOP, File Handling, Exception Handling
- **Modules:** `os`, `datetime`
- **Storage:** Text file (`journal.txt`)
- **Editor:** Visual Studio Code

## 📂 Project Structure

```text
File-Operator/
│
├── main.py
├── journal.txt       # Created automatically
└── README.md
```

## ⚙️ Requirements

- Python 3.8 or later
- Visual Studio Code or another Python-compatible editor
- A terminal or command prompt

No external Python libraries are required.

## 🚀 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Open the Project Folder

```bash
cd File-Operator
```

### Step 3: Run the Program

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## 🖥️ Main Menu

```text
Welcome to Personal Journal Manager!

Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter your choice:
```

## 📄 File Handling Modes

| Mode | Description |
|---|---|
| `r` | Opens an existing file for reading. |
| `w` | Opens a file for writing and clears existing content. |
| `a` | Appends new content to a file or creates it if missing. |
| `x` | Creates a new file and raises an error if it already exists. |

The application primarily uses `a` to add entries, `r` to read and search entries, and `w` to clear file contents before deleting the file.

## 🧠 OOP Concepts Used

- **Class:** `JournalManager` contains the application's functionality.
- **Object:** An instance of `JournalManager` is created to run the program.
- **Constructor:** `__init__()` initializes the journal filename.
- **Instance Methods:** Separate methods manage adding, viewing, searching, and deleting entries.
- **Encapsulation:** Journal operations and file-handling logic are grouped inside a class.

## 🛡️ Exception Handling

The program handles common errors, including:

- `FileNotFoundError` — when the journal file does not exist.
- `PermissionError` — when the program lacks the required file permissions.
- `OSError` — when another operating-system or file operation error occurs.
- `ValueError` — when an invalid file extension is supplied during initialization.

These checks help the application display useful error messages instead of terminating unexpectedly during common file operations.

## 💾 Data Storage

Journal entries are saved in `journal.txt` in the following format:

```text
[2026-10-29 10:00:00]
Today was a productive day. I learned about file handling in Python.

[2026-10-29 18:00:00]
Had a great session learning OOP concepts!
```

The timestamp is generated automatically whenever a new entry is added.

## 🔮 Future Enhancements

- Edit individual journal entries.
- Add password protection.
- Export journal entries to PDF.
- Add categories and tags.
- Develop a graphical user interface (GUI).
- Implement backup and restore functionality.

## 👨‍💻 Author

**Dipen Patni**

Python Project – File Operator

## 📜 License

This project is created for educational and learning purposes.

---

**"Quality is our Motto."**

*Thank you for checking out the Personal Journal Manager!*
