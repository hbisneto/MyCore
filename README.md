# MyCore 2.3

MyCore é um aplicativo gerador de arquivos de código e Jupyter NoteBooks com facilidade e eficiência.

**MyCore is a program entirely developed in Python. To run the program, open the `__init__.py` file located at the root of this project.**

> Note:
>> MyCore was born from Python 3.9. For this reason, the same version of Python (version 3.9) or higher is recommended to run the system.

## Requisitos

- Python 3.9 ou superior

## Instalação

Você pode instalar o MyCore usando o pip, que é um gerenciador de pacotes para Python. Abra o terminal e digite o seguinte comando:

```bash
pip install MyCore
```

#

# Features

Abaixo, uma lista com os principais recursos do programa

<details>
<summary> Efficiency </summary>

MyCore can quickly create large amounts of code, saving time and effort.
</details>

<details>
<summary> Consistency </summary>

MyCore generates consistent code, following the same conventions and standards throughout the project.
</details>

<details>
<summary> Ease of maintenance </summary>

If business logic or requirements change, you only need to update the MyCore and regenerate the code, rather than manually changing multiple parts of the code.
</details>

<details>
<summary> Learning </summary>

For beginners, MyCore can serve as a learning tool to understand how a certain code is structured.
</details>

## Interface de Linha de Comando (CLI)

Uma das principais características do MyCore é a sua interface de linha de comando (CLI) fácil de usar. A CLI foi projetada para ajudar você a tomar decisões rápidas na hora de criar seus códigos.

Ao iniciar o MyCore, você será apresentado a um menu de escolha numérica. Cada número corresponde a um tipo diferente de projeto que você pode criar:

- **Blank Application**
- **Menu Loop Application**
- **Twitter Application**
- **Jupyter NOTEBOOK**

Basta escolher a opção que corresponde ao tipo de projeto que você deseja criar e o MyCore cuidará do resto, criando todos os arquivos necessários para você. Isso torna o processo de criação de código mais eficiente e menos propenso a erros.

<details>
<summary> Exceptions </summary>

MyCore has a standard error handling library that can run in any environment. Every method implemented within the library can be called from any part of the code. That way, it is not necessary to implement the raise RuntimeError() exception call inside the program's runtime library. Just import the module and reference the function call according to the treatment that must be executed.

> Note: Read more about the `exception` module in **MyCore Modules** below.

</details>

<details>
<summary> Backup </summary>

O MyCore não apenas ajuda você a criar projetos, mas também se preocupa com a segurança deles. Ele possui uma funcionalidade de backup que permite compactar seus projetos em um arquivo .zip ou simplesmente salvar os projetos na pasta "Backup".

Sempre que você quiser fazer um backup de seu projeto, o MyCore irá apresentar um menu com duas opções:

1. **Backup Only**
2. **Backup as compressed file (.zip)**

Ambas as opções armazenam os arquivos de backup na pasta "Backup", que está localizada no mesmo diretório em que o MyCore está sendo executado.

Essa funcionalidade proporciona uma camada extra de segurança para seus projetos, permitindo que você tenha sempre uma cópia segura de seu trabalho. Com o MyCore, você pode se concentrar em criar, sabendo que seus projetos estão seguros.

</details>

<details>
<summary> Sample Codes </summary>

O MyCore também oferece a possibilidade de baixar códigos de exemplo. Estes são projetos gerados pelo próprio MyCore e servem para demonstrar suas funcionalidades.

Você tem a opção de baixar quatro projetos de exemplo diferentes. Cada um desses projetos demonstra um tipo diferente de projeto que você pode criar com o MyCore:

##### Blank Application Sample

- **GetInfo:** Get the filename, creation date and modification date of a file anywhere, on any platform.
<br>[GetInfo: MyCore Sample Application](https://github.com/hbisneto/GetInfo/)

##### Menu Loop Application Sample

- **JoKenPo:** Famous game known as "Rock, Paper and Scissors".
<br>[JoKenPo: MyCore Sample Application](https://github.com/hbisneto/JoKenPo)

##### Twitter Application Sample

- **MyTimeline:** Get your Twitter home timeline".
<br>[MyTimeline: MyCore Sample Application](https://github.com/hbisneto/MyTimeline)

##### Jupyter NoteBook Sample

- **MyTimeline:** Get your Twitter home timeline".
<br>[MyTimeline: MyCore Sample Application](https://github.com/hbisneto/MyTimeline)


1. **App1: A Blank Application sample**
2. **App2: a Menu Loop Application sample**
3. **App3: A Twitter Application sample**
4. **App4: A Jupyter NoteBook sample**

Esses códigos de exemplo podem ser muito úteis para entender melhor como o MyCore funciona e para se inspirar para seus próprios projetos. Aproveite esta funcionalidade para explorar ainda mais as possibilidades com o MyCore!

</details>

<!--## Exceptions

MyCore has a standard ***error handling*** library that can run in any environment. Every method implemented within the library can be called from any part of the code. That way, it is not necessary to implement the ```raise RuntimeError()``` exception call inside the program's runtime library. Just import the module and reference the function call according to the treatment that must be executed.

> Note: Read more about the `exception` module in **MyCore Modules** below.-->

<!--## Interface de Linha de Comando (CLI)

Uma das principais características do MyCore é a sua interface de linha de comando (CLI) fácil de usar. A CLI foi projetada para ajudar você a tomar decisões rápidas na hora de criar seus códigos.

Ao iniciar o MyCore, você será apresentado a um menu de escolha numérica. Cada número corresponde a um tipo diferente de projeto que você pode criar:

1. Blank Application
2. Menu Loop Application
3. Twitter Application
4. Jupyter NOTEBOOK

Basta escolher a opção que corresponde ao tipo de projeto que você deseja criar e o MyCore cuidará do resto, criando todos os arquivos necessários para você. Isso torna o processo de criação de código mais eficiente e menos propenso a erros. Aproveite a facilidade que o MyCore oferece para suas necessidades de codificação!-->

<!--## Backup de Projetos

O MyCore não apenas ajuda você a criar projetos, mas também se preocupa com a segurança deles. Ele possui uma funcionalidade de backup que permite compactar seus projetos em um arquivo .zip ou simplesmente salvar os projetos na pasta "Backup".

Sempre que você quiser fazer um backup de seu projeto, o MyCore irá apresentar um menu com duas opções:

1. Backup Only
2. Backup as compressed file (.zip)

Ambas as opções armazenam os arquivos de backup na pasta "Backup", que está localizada no mesmo diretório em que o MyCore está sendo executado.

Essa funcionalidade proporciona uma camada extra de segurança para seus projetos, permitindo que você tenha sempre uma cópia segura de seu trabalho. Com o MyCore, você pode se concentrar em criar, sabendo que seus projetos estão seguros.-->

<!--## Códigos de Exemplo

O MyCore também oferece a possibilidade de baixar códigos de exemplo. Estes são projetos gerados pelo próprio MyCore e servem para demonstrar suas funcionalidades.

Você tem a opção de baixar quatro projetos de exemplo diferentes. Cada um desses projetos demonstra um tipo diferente de projeto que você pode criar com o MyCore:

1. App1: A Blank Application sample
2. App2: a Menu Loop Application sample
3. App3: A Twitter Application sample
4. App4: A Jupyter NOTEBOOK sample

Esses códigos de exemplo podem ser muito úteis para entender melhor como o MyCore funciona e para se inspirar para seus próprios projetos. Aproveite esta funcionalidade para explorar ainda mais as possibilidades com o MyCore!
-->

#

## Native Libraries

The following libraries were used to implement the tool:

<details>
<summary> codecs </summary>

The module defines functions for encoding and decoding with any codec.
<br><br>**Learn more at:** [codecs — Codec registry and base classes](https://docs.python.org/3.9/library/codecs.html)
</details>

<details>
<summary> datetime </summary>

The datetime module provides the classes for handling dates and times.
<br><br>**Learn more at:** [datetime — Basic date and time types](https://docs.python.org/3.9/library/datetime.html)
</details>

<details>
<summary> getpass </summary>

Portable password input.
<br><br>**Learn more at:** [getpass — Portable Password Input](https://docs.python.org/3.9/library/getpass.html)
</details>

<details>
<summary> os </summary>

This module provides a simple way to use functionality that is OS dependent.
<br><br>**Learn more at:** [os — Miscellaneous operating system interfaces](https://docs.python.org/3.9/library/os.html)
</details>

<details>
<summary> pathlib </summary>

This module offers classes representing filesystem paths with semantics appropriate for different operating systems. Path classes are divided between pure paths, which provide purely computational operations without I/O, and concrete paths, which inherit from pure paths but also provide I/O operations.
<br><br>**Learn more at:** [pathlib — Object-oriented filesystem paths](https://docs.python.org/3.9/library/pathlib.html)
</details>

<details>
<summary> shutil </summary>

The shutil module provides several high-level operations on files and file collections. In particular, functions are provided that support copying and removing files. For operations on individual files, see also the os module.
<br><br>**Learn more at:** [shutil — High-level file operations](https://docs.python.org/3.9/library/shutil.html)
</details>

<details>
<summary> sys </summary>

This module provides access to some variables used or maintained by the interpreter and functions that interact strongly with the interpreter.
<br><br>**Learn more at:** [sys — System-specific parameters and functions](https://docs.python.org/3.9/library/sys.html)
</details>

<details>
<summary> time </summary>
This module provides various time-related functions. For related functionality, see also the [datetime](https://docs.python.org/3.9/library/datetime.html) and [calendar](https://docs.python.org/3.9/library/calendar.html) modules.
<br><br>**Learn more at:** [time — Time access and conversions](https://docs.python.org/3.9/library/time.html)
</details>

<details>
<summary> zipfile </summary>

The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file. Any advanced use of this module will require an understanding of the format, as defined in [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT).
<br><br>**Learn more at:** [zipfile — Work with ZIP archives](https://docs.python.org/3.9/library/zipfile.html)
</details>

<!-- Third party libraries -->
## Third Party Libraries
The following libraries were used to implement the tool:

<details>
<summary> requests </summary>

Requests is an elegant and simple HTTP library for Python, built for human beings.

```
pip install requests
```

<br><br>**Learn more at:** [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)
> The use of the requests library is mandatory in cases of "Download Sample Projects" on MyCore.
</details>

<details>
<summary> tweepy </summary>

An easy-to-use library for accessing the Twitter API.

```
pip install tweepy
```

<br><br>**Learn more at:** [tweepy — An easy-to-use Python library for accessing the Twitter API](https://docs.tweepy.org/en/stable/)
</details>

<details>
<summary> filesystempro </summary>

FileSystem is designed to identify the operating system (OS) on which it’s running and define the paths to various user directories based on the OS.

```
pip install filesystempro
```

**Learn more at:** [FileSystem Pro](https://pypi.org/project/filesystempro/)
</details>

<details>
<summary> AAAAAAAAAAAAAA </summary>
</details>

<details>
<summary> AAAAAAAAAAAAAA </summary>
</details>

<details>
<summary> AAAAAAAAAAAAAA </summary>
</details>

#




* **tweepy:** An easy-to-use library for accessing the Twitter API.
    - Read more about the ```tweepy``` library at [tweepy — An easy-to-use Python library for accessing the Twitter API](https://docs.tweepy.org/en/stable/)

> The use of the tweepy library is optional and only mandatory in cases of "Twitter Application Project" created in MyCore.

#

* **requests:** Requests is an elegant and simple HTTP library for Python, built for human beings.
    - Read more about the ```requests``` library at [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)

> The use of the requests library is mandatory in cases of "Download Sample Projects" on MyCore.


>
Após a instalação, você pode começar a usar o MyCore para criar seus arquivos de código e Jupyter NoteBooks.
Esperamos que você aproveite o uso do MyCore para todas as suas necessidades de codificação! Se você tiver alguma dúvida ou problema, não hesite em nos contatar.