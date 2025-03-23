import os
import shutil
import tempfile
import ctypes

def delete_directory(directory_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"{directory_path} supprimé avec succès.")
    else:
        print(f"{directory_path} n'existe pas.")

def delete_temp_files():
    temp_dir = tempfile.gettempdir()
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)
    print("Fichiers temporaires supprimés.")

def empty_recycle_bin():
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
    print("Corbeille vide.")

def delete_fivem_mods():
    fivem_mods_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'mods')
    delete_directory(fivem_mods_folder)


def startclearmods():
    delete_fivem_mods()
    delete_temp_files()
    empty_recycle_bin()
