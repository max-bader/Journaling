# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Max Bader
# mibader@uci.edu
# 77466224

# path: C:\Users\bader\OneDrive\Desktop\a3
# server address: 168.235.86.101

from pathlib import Path
from Profile import Profile, DsuFileError, DsuProfileError, Post
from functions import edit_file, print_file_data, list_file
from ui import introduction, for_files, for_create, for_open, admin, editing_dsu_commands, printing_dsu_commands, for_server

file_path = None
port = 3021

def main():
    global file_path
    while True:
        # here we assume that the input can be split by whitespace and that the file path has no whitespace
        # if there was whitespace in the file path it would mess up the variables
        command = introduction()

        if command == 'c':
            created_file = for_create()
            c_command = input("Type 'e' to edit, 'p' to print dsu contents, or 's' to send dsu contents to a server\n")
            if c_command == 'e':
                user_input = editing_dsu_commands()
                z = user_input.split()
                edit_file(created_file, z)
            elif c_command == 'p':
                user_input = printing_dsu_commands()
                y = user_input.split()
                print_file_data(created_file, y)
            elif c_command == 's':
                for_server()

        elif command == 'o':
            opened_file = for_open()
            o_command = input("Type 'e' to edit or 'p' to print dsu contents, or 's' to send dsu contents to server.\n")
            if o_command == 'e':
                user_input = editing_dsu_commands()
                a = user_input.split()
                edit_file(opened_file, a)
            elif o_command == 'p':
                user_input = printing_dsu_commands()
                b = user_input.split()
                print_file_data(opened_file, b)
            elif o_command == 's':
                for_server()

        elif command == 'l':
            file_path = for_files()
            list_file(file_path)
            
        elif command == 'admin':
            admin()

        elif command == 'q':
            print("Exiting now")
            break

        else:
            print("Command not found.")
     

if __name__ == "__main__":
    main()

