# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Max Bader
# mibader@uci.edu
# 77466224
from functions import create_new_file, open_file
from functions import list_file, delete_file, read_file, edit_file, print_file_data, write_to_server

file_path = None


def introduction():
    print("Welcome!")
    print("Type 'c' to create or 'o' to open a dsu file.")
    print("Type 'l' to list out files.")
    print("Type 'p' to post journal to server.")
    print("Type 'admin' to enter admin mode.")
    print("Type 'q' to quit.")
    user_input = input().lower()
    return user_input


def for_files():
    file_path = input("Enter the directory of the path.")
    file_path = 'l ' + file_path
    print(file_path)
    list_commands = input("Type '-r' to recursively search, '-e' [extension] to get the extension, 's' [file] to search for files, and '-f' to just list files.\n")
    print(list_commands)
    real_command = file_path + " " + list_commands
    print(real_command)
    real_file = real_command.split()
    return real_file


def for_create():
    file_path = input("Enter the directory of the path of the dsu file followed by '-n' [FILE NAME]\n")
    file_path = 'c ' + file_path
    a = file_path.split()
    create_new_file(a)
    print(f'{file_path} created!')
    return file_path


def for_open():
    file_path = input("Enter the file you want to load.\n")
    a = 'a ' + file_path
    open_file(a)
    print(f'{file_path} loaded successfully!')
    return file_path


def for_server():
    file_path = input("Enter the file you want to use.\n")
    write_to_server(file_path)


def editing_dsu_commands():
    print("Choose ways to edit the dsu file with the following format.")
    print("[command] [edits]")
    print("Use '-usr' command to change username.")
    print("Use '-pwd' command to change the password.")
    print("Use '-bio' command to change the bio")
    print("Use '-addpost' to add new posts to the profile.")
    print("Use -delpost' to delete a post in the profile.")
    user_input = input()
    return user_input


def printing_dsu_commands():
    print("Choose ways to print from the dsu file in the format.")
    print("P [command]")
    print("Use '-usr' command to print the username.")
    print("Use '-pwd' command to print the password.")
    print("Use '-bio' command to print the bio.")
    print("Use '-posts' command to print all the posts.")
    print("Use '-post [id]' command to print a specific post.")
    print("Use '-all' commadn to print all the profile contents.")
    user_input = input()
    return user_input


def admin():
    global file_path
    print("Now in admin mode. Type 'q' to exit.")
    print("Format: [command] [path_directory]")
    print("Type 'l' to list files")
    print("Type 'c' to create a new file. Format: -n [FILENAME]")
    print("Type 'd' to delete a file")
    print("Type 'r' to read file contents")
    print("Type 'o' to open a file")
    print("Type 'e' to edit a file")

    while True:
        user_input = input("command: ").split()
        command = user_input[0]
        if command == 'q':
            break
        elif command == "l":
            print("Use '-r' to recursively search directory")
            print("Use '-f' to just list the contents")
            print("Use '-s' [file] to search for files")
            print("use '-e' [extension] to get the extension files")
            command_for_l = input().split()
            for elem in command_for_l:
                user_input.append(elem)
            print(user_input)
            list_file(user_input)
        elif command == 'c':
            file_path = create_new_file(user_input)
        elif command == 'd':
            delete_file(user_input)
        elif command == "r":
            read_file(user_input)
        elif command == 'o':
            file_path = open_file(user_input)
        elif command == "e":
            edit_file(file_path, user_input)
        elif command == "p":
            print_file_data(file_path, user_input)
        else:
            print("Error: Not a valid command")
