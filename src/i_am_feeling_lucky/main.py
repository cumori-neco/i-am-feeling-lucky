import os
import random
import question
from rockpaperscissors import game


def main():
    if check_admin() == False:
        print('You are not an administrator, no fun.')
        exit(1)
    if not passed_question():
        print('Unlucky.')
        delete_random_root_item()
        exit(0)

    print('You truly are lucky.')


def check_admin() -> bool:
    if os.name == 'nt':
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    elif os.name == 'posix':
        return os.geteuid() == 0
    else:
        return False


def delete_random_root_item():
    root = "C:\\" if os.name == 'nt' else "/"
    try:
        dest = find_random_file(root)

        if not dest:
            print("no files?")
            return

        if should_actually_delete():
            os.remove(dest)
            print(f"Deleted: {dest}")
        else:
            print(f"Would have deleted: {dest} (Change .config/i-am-feeling-lucky.txt to 'yes' if you dare)")
    except Exception as e:
        print(f"Lucky enough, failed to delete file: {e}")


def find_random_file(current_dir: str) -> str | None:
    try:
        items = os.listdir(current_dir)
    except (PermissionError, FileNotFoundError):
        return None

    ignored_dirs = {'proc', 'sys', 'dev', 'boot', 'efi', 'Volumes', '.file'} if os.name != 'nt' else {'$Recycle.Bin', 'System Volume Information'}

    files = []
    dirs = []

    for item in items:
        full_path = os.path.join(current_dir, item)
        if current_dir in ("/", "C:\\") and item in ignored_dirs:
            continue
        try:
            if os.path.isfile(full_path):
                files.append(full_path)
            elif os.path.isdir(full_path):
                dirs.append(full_path)
        except (PermissionError, FileNotFoundError):
            continue

    if files and dirs:
        if random.choice([True, False]):
            return random.choice(files)
        else:
            random.shuffle(dirs)
            for sub_dir in dirs:
                found_file = find_random_file(sub_dir)
                if found_file:
                    return found_file
            return random.choice(files)

    if files:
        return random.choice(files)

    if dirs:
        random.shuffle(dirs)
        for sub_dir in dirs:
            found_file = find_random_file(sub_dir)
            if found_file:
                return found_file

    return None

def passed_question() -> bool:
    match random.randint(0,2):
        case 0:
            return game()
        case 1:
            a = random.randint(0,100)
            b = random.randint(0,100)
            return int(input(f'What is {a} + {b}? :')) == a+b
        case 2:
            return question.question()
        case _:
            return True

def should_actually_delete() -> bool:
    config_path = os.path.expanduser("~/.config/i-am-feeling-lucky.txt")

    if not os.path.exists(config_path):
        return False

    try:
        with open(config_path, "r") as f:
            content = f.read().strip().lower()
            return content == "yes"
    except Exception:
        return False

if __name__ == '__main__':
    main()
