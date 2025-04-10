import os
import shutil

def clear_digital_entitlements():
    folder_path = os.path.expandvars(r'%LOCALAPPDATA%\DigitalEntitlements')
    
    if os.path.exists(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path) 
            except Exception as e:
                print(f"Erreur lors de la suppression de {item_path}: {e}")
        print("Le dossier DigitalEntitlements a été vidé.")
    else:
        print("Le dossier DigitalEntitlements n'existe pas.")