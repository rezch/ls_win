import sys
from os import walk
from sys import argv, setrecursionlimit


class COLORS:
    GREY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'

    ALL_COLORS = [
        GREY, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN
    ]


def colored_print(name: str, is_folder: bool, adder_size: int, is_end=False) -> None:
    is_shadow = name[0] == '.'
    adder = '│  ' * adder_size
    if is_end and not is_folder:
        adder += '└──'
    else:
        adder += '├──'
    print(f'{COLORS.GREY}{adder}{COLORS.END}', end='')
    if is_folder:
        if is_shadow:
            print(f'{COLORS.PURPLE}{name}{COLORS.END}')
        else:
            print(f'{COLORS.BLUE}{name}{COLORS.END}')
        return
    if is_shadow:
        print(f'{COLORS.YELLOW}{name}{COLORS.END}')
    else:
        print(name)


def ls(depth: int, current_folder='.', current_depth: int = 0) -> None:
    if depth == 0:
        return

    try:
        (root, folders, files) = next(walk(current_folder))
    except:
        return

    all_items = sorted(folders + files)
    for item in all_items:
        if item in files:
            colored_print(item, is_folder=False, adder_size=current_depth, is_end=(item == all_items[-1]))
        else:  # folder
            colored_print(item, is_folder=True, adder_size=current_depth, is_end=(item == all_items[-1]))
            ls(depth - 1, current_folder + '/' + item, current_depth=current_depth + 1)


def main():
    setrecursionlimit(10_000)
    if len(sys.argv) > 2:
        print('Invalid number of arguments')
        return
    if len(sys.argv) == 2:
        depth = sys.argv[1]
    else:
        depth = -1
    try:
        depth = int(depth)
    except (ValueError, TypeError):
        print(f'Invalid parse depth value "{depth}"')
        return
    ls(depth)


if __name__ == "__main__":
    main()

