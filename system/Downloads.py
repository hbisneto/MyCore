import cli
from system import filesystem as fs
import requests
import shutil
import time
from pathlib import Path
from zipfile import ZipFile

DICT_SAMPLES = {
    0:["GetInfo", "https://github.com/hbisneto/GetInfo/archive/refs/heads/main.zip"],
    1:["JoKenPo", "https://github.com/hbisneto/JoKenPo/archive/refs/heads/main.zip"],
    2:["MyTimeline", "https://github.com/hbisneto/MyTimeline/archive/refs/heads/main.zip"],
    3:["JupyterBridge", "https://github.com/hbisneto/JupyterBridge/archive/refs/heads/main.zip"]
}

def download_samples():
    cli.make_menu("DOWNLOAD SAMPLE CODE", separator_style=">")
    for i in DICT_SAMPLES:
        print(f'[{i+1}] - {DICT_SAMPLES[i][0]}')
    print('[0] - << Go Back')
    print()
    opc = int(input('>>[!] Type a number: '))
    cli.separator(style = "<")
    if opc == 0:
        return

    # print(UserOption)
    app_name = DICT_SAMPLES[opc-1][0]
    app_url = DICT_SAMPLES[opc-1][1]
    # print(app_name)
    # print(app_url)

    # Verify if Samples folder exists
    fs.create_samples_folder()
    fs.create_custom_folder(app_name, fs.samples_folder)
    download_sample_item(app_name, app_url)

def download_sample_item(appname, url):
    cli.make_menu(f"DOWNLOADING: {appname}...", new_line = True)
    print("[Status]: Starting Download...")
    print('[Status]: Verifying repository to download...')

    try:
        FROM = f'{fs.CURRENT_LOCATION}/main.zip'
        TO = f'{fs.samples_folder}/{appname}/{appname}.zip'

        ServerResponse = requests.get(url, stream = True)
        FileName = url.split("/")[-1]
        with open(FileName, 'wb') as f:
            for Chunk in ServerResponse.iter_content(chunk_size = 1024):
                if Chunk:
                    f.write(Chunk)
        print(f'[Status]: "{appname}" download 100% completed!')
        print(f'[Status]: Verifying "{appname}"...')
        print(f'[Done]: "{appname}" download process complete!')
    except:
        print("[ERROR]: Could't connect to the server!")
        print(f'[Process]: Cleaning cache...')
        time.sleep(3)
        shutil.rmtree(f'{fs.samples_folder}/{appname}/')
        print("[Process]: Cache cleaned!")
        
    try:
        Path(FROM).rename(TO)
        cli.separator()
    except:
        return
    
    cli.make_menu(f"EXTRACTING: {appname}...", new_line = True)
    with ZipFile(TO, 'r') as zipObj:
        zipObj.extractall(f'{fs.samples_folder}/{appname}/')
    print(f'[Done]: "{appname}" extraction process complete!')
    cli.separator()