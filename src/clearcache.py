import os
import shutil
import time
from win10toast import ToastNotifier
import webview


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
            message = f"[INFO] Suppression de {dossier}..."
            print(message)
            updateConsole(message)
            time.sleep(0.5)
            shutil.rmtree(dossier, ignore_errors=True)
            success_message = f"[SUCCÈS] Dossier {dossier} supprimé avec succès !"
            print(success_message)
            updateConsole(success_message)
        else:
            warning_message = f"[AVERTISSEMENT] Dossier {dossier} non trouvé !"
            print(warning_message)
            updateConsole(warning_message)
            time.sleep(0.3)

def updateConsole(message):
    try:
        if webview.windows:
            webview.windows[0].evaluate_js(f"""
                const consoleElement = document.getElementById('console');
                if (consoleElement) {{
                    consoleElement.innerText += `{message}\\n`;
                    consoleElement.scrollTop = consoleElement.scrollHeight;  // Scroll automatique vers le bas
                }}
            """)
        else:
            print("Erreur : Aucune fenêtre webview active.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour de la console : {e}")