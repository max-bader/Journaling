# max bader
# mibader@uci.edu
# 77466224

from pathlib import Path
import pathlib
from Profile import Profile, DsuFileError, DsuProfileError, Post
from ds_client import send

PORT = 3021

def write_to_server(file_path):
    profile = Profile()
    profile.load_profile(file_path)

    if profile.dsuserver == None:
        server = input("Enter the server address: ")
        profile.dsuserver = server

    entry = input("Enter the message you want to write:\n")
    post = Post(entry = entry)
    profile.add_post(post)

    try:
        profile.save_profile(file_path)
    except DsuFileError as e:
        print(f"Error as {e}")

    user = profile.username
    pwd = profile.password
    server = profile.dsuserver

    send(server, PORT, user, pwd, entry)



def printcontent(file_path, recursive=False, f_only=False, suffix=False, extension=False, name=""):
    itempath = Path(file_path)
    content = sorted(itempath.iterdir())

    for item in content:
        if item.is_file():
            if f_only:
                if item.is_file():
                    if extension:
                        if item.suffix == f'.{name}':
                            print(item)
                    elif suffix:
                        if item.name == name:
                            print(item)
                    elif not suffix and not extension:
                        print(item)
            else:
                if extension:
                    if item.suffix == f'.{name}':
                        print(item)
                elif suffix:
                    if item.name == name:
                        print(item)
                elif not suffix and not extension:
                    print(item)
    for item in content:
        if item.is_dir():
            if f_only:
                if item.is_file():
                    if suffix:
                        if item.suffix == f'.{name}':
                            print(item)
                    elif extension:
                        if item.name == name:
                            print(item)
                    elif not suffix and not extension:
                        print(item)
            else:
                if suffix:
                    if item.suffix == f'.{name}':
                        print(item)
                elif extension:
                    if item.name == name:
                        print(item)
                elif not suffix and not extension:
                    print(item)
        if item.is_dir() and recursive:
            printcontent(Path(item), recursive, f_only, suffix, extension, name)


def list_file(user_input):
    recursive = '-r' in user_input
    f_only = '-f' in user_input
    suffix = '-s' in user_input
    extension = '-e' in user_input
    name = ""
    
    if suffix:
        search_idx = user_input.index('-s') + 1
        if search_idx < len(user_input):
            name = user_input[search_idx]
    if extension:
        search_idx = user_input.index('-e') + 1
        if search_idx < len(user_input):
            name = user_input[search_idx]

    if len(user_input) > 1:
        # assume there is no whitespace in the path
        path_directory = user_input[1]
        printcontent(path_directory, recursive, f_only, suffix, extension, name)


def create_new_file(user_input):
    if '-n' in user_input:
        # assume there is no whitespace in the path
        name = user_input[-1]
        file = user_input[1]
        file_name = f"{file}/{name}.dsu"
        file_path = file_name
        username = input("Enter username: ")
        password = input("Enter password: ")
        bio = input("Enter a bio: ")
        user = Profile(username=username, password=password)
        user.bio = bio
        try:
            file = open(file_name, 'x')
            path = Path(file_name)
            print(path)
            file.close()
        except FileExistsError:
            print("ERROR")
        
        try:
            user.save_profile(file_name)
            print("successfully saved")
        except FileExistsError:
            print("File already exists")
    else:
        print("ERROR")
    return file_path


def delete_file(user_input):
    try:
        # assume there is no whitespace in the path
        path_directory = user_input[1]
        path = Path(path_directory)
        if path_directory.endswith(".dsu"):
            path.unlink()
            print(f"{path} DELETED")
        else:
            print("ERROR")
    except (ValueError, IndexError):
        print("ERROR")


def read_file(user_input):
    path_directory = user_input[1]
    path = Path(path_directory)
    if path_directory.endswith(".dsu"):
        my_file = open(path)
        content = my_file.read()
        if content:
            print(content, end="")
            my_file.close()
        else:
            print("EMPTY")
    else:
        print('ERROR')


def open_file(user_input):
    path_directory = user_input[1]
    print(user_input)
    file_path = path_directory
    path = Path(path_directory)
    try:
        with open(path, 'r') as file:
            profile = Profile()
            profile.load_profile(path)
            print(f'{path} was successfully loaded.')
    except FileNotFoundError:
        print("ERROR")
    except DsuProfileError as e:
        print("Failed to load")
    except DsuFileError as e:
        print("ERROR")
    return file_path


def edit_file(path_directory, user_input):
    path = Path(path_directory)
    try:
        profile = Profile()
        profile.load_profile(path)

        if "-usr" in user_input:
            idx = user_input.index("-usr") + 1
            if user_input[idx].startswith('"') and user_input[idx].endswith('"'):
                user = user_input[idx][1:-1]
                profile.username = user
            else:
                profile.username = user_input[idx]

        if "-pwd" in user_input:
            idx = user_input.index("-pwd") + 1
            if user_input[idx].startswith('"') and user_input[idx].endswith('"'):
                pwd = user_input[idx][1:-1]
                profile.password = pwd
            else:
                profile.password = user_input[idx]

        if "-bio" in user_input:
            idx = user_input.index("-bio") + 1
            joint_list = " ".join(user_input)
            split_quote = joint_list.split('"')
            idx_bio = None
            for idx, item in enumerate(split_quote):
                if "-bio" in item:
                    idx_bio = idx + 1
                    break
            profile.bio = split_quote[idx_bio]

        if "-addpost" in user_input:
            # TODO when there is a post in the dsu file, the file doesn't load with O command
            idx = user_input.index("-addpost") + 1
            joint_list = " ".join(user_input)
            split_quote = joint_list.split('"')
            idx_addpost = None
            for idx, item in enumerate(split_quote):
                if "-addpost" in item:
                    idx_addpost = idx + 1
                    break
            post = Post(entry=split_quote[idx_addpost])
            profile.add_post(post)

        if "-delpost" in user_input:
            idx = int(user_input.index("-delpost") + 1)
            post_idx = int(user_input[idx])
            profile.del_post(post_idx)

        profile.save_profile(path)

    except FileNotFoundError:
        print("ERROR")


def print_file_data(path_directory, user_input):
    path = Path(path_directory)
    try:
        profile = Profile()
        profile.load_profile(path)
        if "-usr" in user_input:
            print(profile.username)
        if "-pwd" in user_input:
            print(profile.password)
        if "-bio" in user_input:
            print(profile.bio)
        if "-posts" in user_input:
            posts = profile.get_posts()
            for post in posts:
                print(post.entry)
        if "-post" in user_input:
            posts = profile.get_posts()
            post_idx = user_input.index("-post") + 1
            print(posts[int(user_input[post_idx])].entry)
        if "-all" in user_input:
            print(profile.username)
            print(profile.password)
            print(profile.bio)
            posts = profile.get_posts()
            for post in posts:
                print(post.entry)
                
    except FileExistsError:
        print("File not found")
