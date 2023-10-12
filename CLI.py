## CLI.py File
## This file is used to implement the CLI styles for users

import os

def get_terminal_size():
    size = os.get_terminal_size()
    return size.lines, size.columns

rows, columns = get_terminal_size()

# separator_style = '='*columns
# print('='*columns)
# print(columns)

def make_menu(title, text = "", style = "default", newline = True, separator_style = "="):
    """
    A função aceita quatro parâmetros: `title`, `text`, `style` e `newline`.
    Os parâmetros `text`, `style` e `newline` não são obrigatórios.
    """
    
    if newline == True:
        print()
    if style == "short":
        # print("1. Short Style Selected")
        print(f'{separator_style}' * columns)
        print(f"{title}")
        print(f"{text}")
        print(f'{separator_style}' * columns)
    elif style == "long":
        # print("2. Long Style Selected")
        print("=" * columns)
        print(f"{title}")
        print("=" * columns)
        print(f"{text}")
        print("=" * columns)
    else:
        # print("3. Default Style Selected")
        print(f'{separator_style}' * columns)
        print(f"{title}")
        print(f'{separator_style}' * columns)

def separator(style = "="):
    print(f'{style}' * columns)

### EXEMPLES OF USE ###
    # make_menu("1. Title", "Short description", "short", True)
    # make_menu("2. Title", "Long description", "long", newline=True)
    # make_menu("3. Title")
### EXEMPLES OF USE ###