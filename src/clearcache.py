import os
import shutil
import time
from win10toast import ToastNotifier

def supprimer_cache():
    chemin_cache_fivem = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'data')
    chemin_racine_fivem = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app')
    
    dossiers_a_supprimer = [
        os.path.join(chemin_racine_fivem, 'crashes'),
        os.path.join(chemin_racine_fivem, 'logs'),
        os.path.join(chemin_cache_fivem, 'server-cache'),
        os.path.join(chemin_cache_fivem, 'server-cache-priv'),
        os.path.join(chemin_cache_fivem, 'cache'),
        os.path.join(chemin_cache_fivem, 'nui-storage')
    ]
    
    for dossier in dossiers_a_supprimer:
        if os.path.exists(dossier):
            print(f"[INFO] Suppression de {dossier}...")
            time.sleep(0.5)
            shutil.rmtree(dossier, ignore_errors=True)
            print(f"[SUCCÈS] Dossier {dossier} supprimé avec succès !")
        else:
            print(f"[AVERTISSEMENT] Dossier {dossier} non trouvé !")
            time.sleep(0.3)
    

