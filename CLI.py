## CLI.py File
## This file is used to implement the CLI styles for users


def showMenu(title, text = "", style = "default", newline = True, separatorStyle = "="):
    """
    A função aceita quatro parâmetros: `title`, `text`, `style` e `newline`.
    Os parâmetros `text`, `style` e `newline` não são obrigatórios.

    A função `showmenu` pode ser usada para exibir um menu com base nos parâmetros fornecidos.
    A variável `title` é usada para o título do menu, `text` é o conteúdo principal a ser exibido, `style` determina a formatação do texto e `newline` controla se uma nova linha deve ser impressa antes do menu.

    - Se a variável `newline` for verdadeira, uma nova linha será impressa.
    - Se o estilo for definido como `short`, o seguinte será impresso:
        - Uma linha de 80 caracteres de "=".
        - O título.
        - O texto fornecido.
        - Outra linha de 80 caracteres de "=".
    - Se o estilo for definido como `long`, o seguinte será impresso:
        - Uma linha de 80 caracteres de "=".
        - O título.
        - Outra linha de 80 caracteres de "=".
        - O texto fornecido.
        - Outra linha de 80 caracteres de "=".
    - Se nenhum estilo for especificado (nem `short` nem `long`), o seguinte será impresso por padrão:
        - Uma linha de 80 caracteres de "=".
        - O título.
        - Outra linha de 80 caracteres de "=".
    
    Exemplo:
    ```
    import CLI

    CLI.showMenu("Menu Title")
    ```

    Output:
    ```
    ================================================================================
    Menu Title
    ================================================================================
    ```
    
    Exemplo 2:
    ```
    import CLI
    CLI.showMenu("Menu Title", "Some desctiption", "short", True)
    ```

    Output:
    ```
    ================================================================================
    Menu Title
    Some desctiption
    ================================================================================
    ```

    Exemplo 3:
    ```
    import CLI
    CLI.showMenu("Menu Title", "Some desctiption", "long", True)
    ```

    Output:
    ```
    ================================================================================
    Menu Title
    ================================================================================
    Some desctiption
    ================================================================================
    ```
    """
    
    if newline == True:
        print()
    if style == "short":
        # print("1. Short Style Selected")
        print(f'{separatorStyle}'*80)
        print(f"{title}")
        print(f"{text}")
        print(f'{separatorStyle}'*80)
    elif style == "long":
        # print("2. Long Style Selected")
        print("="*80)
        print(f"{title}")
        print("="*80)
        print(f"{text}")
        print("="*80)
    else:
        # print("3. Default Style Selected")
        print(f'{separatorStyle}'*80)
        print(f"{title}")
        print(f'{separatorStyle}'*80)

def separator(style = "="):
    print(f'{style}' * 80)

### EXEMPLES OF USE ###
    # ShowMenu("1. Title", "Short description", "short", True)
    # ShowMenu("2. Title", "Long description", "long", newline=True)
    # ShowMenu("3. Title")
### EXEMPLES OF USE ###