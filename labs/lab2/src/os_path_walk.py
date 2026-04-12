import os


def walk_path(parent_path: str) -> None:
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)

    for child in childs:
        child_path = os.path.join(parent_path, child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            print(f"Last access: {last_access}")
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tLast access: {last_access}")
            print(f"\tSize: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)


# walk_path(os.getcwd())


def walk_path_v2(parent_path: str) -> None:
    for parent_path, _, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tLast access: {last_access}")
            print(f"\tSize: {size}")


# walk_path_v2(os.getcwd())
