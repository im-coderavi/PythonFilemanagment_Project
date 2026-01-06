"""
PROJECT NAME  : Advanced File Management System
LANGUAGE      : Python
MODULE USED   : pathlib, time, os
TYPE          : Menu Driven Console Application

NOTE:
This project is written in a very human-readable style.
Each step is commented so beginners can understand easily.
"""

from pathlib import Path
import time
import os


# --------------------------------------------------
# Utility Function: Clear screen (for better UI)
# --------------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# --------------------------------------------------
# Utility Function: Pause screen
# --------------------------------------------------
def pause():
    input("\nPress ENTER to continue...")


# --------------------------------------------------
# Show all files and folders with details
# --------------------------------------------------
def show_files():
    clear_screen()
    path = Path('.')
    items = list(path.iterdir())

    if not items:
        print("No files or folders found.")
        return

    print(" Files & Folders in Current Directory\n")

    for i, item in enumerate(items, start=1):
        if item.is_file():
            size = item.stat().st_size
            modified = time.ctime(item.stat().st_mtime)
            print(f"{i}. {item.name} | FILE | {size} bytes | Modified: {modified}")
        else:
            print(f"{i}. {item.name} | FOLDER")

    pause()


# --------------------------------------------------
# Create file
# --------------------------------------------------
def create_file():
    clear_screen()
    name = input("Enter new file name: ")
    file_path = Path(name)

    if file_path.exists():
        print("File already exists.")
    else:
        content = input("Enter file content: ")
        file_path.write_text(content)
        print("File created successfully.")

    pause()


# --------------------------------------------------
# Read file
# --------------------------------------------------
def read_file():
    clear_screen()
    name = input("Enter file name to read: ")
    file_path = Path(name)

    if file_path.exists() and file_path.is_file():
        print("\n----- FILE CONTENT START -----\n")
        print(file_path.read_text())
        print("\n----- FILE CONTENT END -----")
    else:
        print("File not found.")

    pause()


# --------------------------------------------------
# Update file
# --------------------------------------------------
def update_file():
    clear_screen()
    name = input("Enter file name to update: ")
    file_path = Path(name)

    if not file_path.exists():
        print("File does not exist.")
        pause()
        return

    print("\n1. Rename File")
    print("2. Overwrite File Content")
    print("3. Append Data")

    choice = input("Select option: ")

    if choice == '1':
        new_name = input("Enter new file name: ")
        file_path.rename(new_name)
        print("File renamed successfully.")

    elif choice == '2':
        new_data = input("Enter new content: ")
        file_path.write_text(new_data)
        print("File content overwritten.")

    elif choice == '3':
        extra_data = input("Enter data to append: ")
        with open(file_path, 'a') as f:
            f.write("\n" + extra_data)
        print("Data appended successfully.")

    else:
        print("Invalid option.")

    pause()


# --------------------------------------------------
# Delete file (with confirmation)
# --------------------------------------------------
def delete_file():
    clear_screen()
    name = input("Enter file name to delete: ")
    file_path = Path(name)

    if file_path.exists() and file_path.is_file():
        confirm = input("Are you sure? (y/n): ").lower()
        if confirm == 'y':
            file_path.unlink()
            print("File deleted successfully.")
        else:
            print("Delete cancelled.")
    else:
        print("File not found.")

    pause()


# --------------------------------------------------
# Search file by name
# --------------------------------------------------
def search_file():
    clear_screen()
    keyword = input("Enter file name keyword to search: ")

    found = False
    for item in Path('.').iterdir():
        if keyword.lower() in item.name.lower():
            print(item.name)
            found = True

    if not found:
        print("No matching file found.")

    pause()


# --------------------------------------------------
# Main Menu
# --------------------------------------------------
def main_menu():
    while True:
        clear_screen()
        print("========== FILE MANAGEMENT SYSTEM ==========")
        print("1. Show Files & Folders")
        print("2. Create File")
        print("3. Read File")
        print("4. Update File")
        print("5. Delete File")
        print("6. Search File")
        print("7. Exit")
        print("============================================")

        choice = input("Select option (1-7): ")

        if choice == '1':
            show_files()
        elif choice == '2':
            create_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            update_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            search_file()
        elif choice == '7':
            print("Exiting program... Thank you!")
            time.sleep(1)
            break
        else:
            print("Invalid choice.")
            time.sleep(1)


# --------------------------------------------------
# Program starts here
# --------------------------------------------------
main_menu()


