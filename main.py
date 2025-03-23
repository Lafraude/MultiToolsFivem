import webview
import os
import shutil
import json
import time
import sys
from win10toast import ToastNotifier
try:
    from src.clearcache import supprimer_cache  
    from src.deletemods import startclearmods
except Exception as e:
    print(f"Error {e}")
    time.sleep(10)
    exit()

toaster = ToastNotifier()
icon_path = os.path.join(os.getcwd(), './img/ico/logonotif.ico')


# HTML et CSS pour l'interface
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi Tools Fivem</title>
    <link rel="stylesheet" href="public/cagfivem.css">
    <link rel="stylesheet" href="public/divpackrea.css">

    <style>
        &::-webkit-scrollbar {
          display: none;
        }
        :root {
            --primary-bg: #000000;      
            --secondary-bg: #0f172a;    
            --accent-color: #1e3a8a;     
            --text-color: #ffffff;
            --button-bg: #1e3a8a;
            --button-hover: #3b82f6;
            --console-bg: #0f172a;
        }
      
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
      
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            color: var(--text-color);
            text-align: center;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(270deg, var(--primary-bg), var(--secondary-bg), var(--primary-bg));
            /* background-size: 600% 600%; */
            animation: gradientAnimation 10s ease infinite;
        }
      
        /* Titre avec animation de slide-in */
        h1 {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 40px;
            animation: slideIn 1.5s ease-out;
        }
      
        @keyframes slideIn {
            0% { transform: translateY(-50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
      
        .button-container {
            display: flex;
            flex-direction: flex;
            gap: 20px;
            justify-content: center;
            margin-bottom: 40px;
        }
      
        .btn {
            background-color: var(--button-bg);
            color: var(--text-color);
            border: none;
            width: 200px;
            height: 50px;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 40px;
            cursor: pointer;
            margin-inline: 5px;
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
     
        .btn:hover {
            background-color: var(--button-hover);
            transform: scale(1.05);
        }
    
        #console {
            margin-top: 15px;
            width: 80%;
            max-width: 600px;
            height: 150px;
            background-color: var(--console-bg);
            color: var(--text-color);
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
            padding: 30px;
            border-radius: 4px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            overflow-y: auto;
            animation: fadeInUp 1.5s ease;
        }
      
        @keyframes fadeInUp {
            0% { transform: translateY(50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        #creditid{
            color: var(--text-color);
        }
        
      </style>

</head>
<body>
    <h1 id="titlehome">Bienvenue</h1>
    <div class="home" id="homeid">
        <button class="btn" onclick="clearCache()">Clear Cache</button>
        <button class="btn" onclick="clearMods()">Clear Mods</button>
        <button class="btn" id="btnfivemcag" onclick="packFivem()">Pack Fivem</button> <p>
        <button class="btn" onclick="actionBtn4()">Soon</button>
        <button class="btn" onclick="actionBtn5()">Soon</button>
    </div>

    <nav id="navbar" class="navbar">
        <img class="imgnavbar" src="/img/200w.gif" alt="">
        <ul>
            <button class="btnnav">Home</button>
            <button class="btnnav">Pack Réaliste</button> 
            <button class="btnnav">Pack GunFight</button>
            <button class="btnnav">Pack Son</button> 
            <button class="btnnav">Mods Fivem</button>
        </ul>
    </nav>

    <div id="packrealistefivemid" class="packrealistefivem">
        <div>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option1')">Exécuter Option 1</button>
        </div>
        <div>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option2')">Exécuter Option 2</button>
        </div>
        <div>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option3')">Exécuter Option 3</button>
        </div>
        <div>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option4')">Exécuter Option 4</button>
        </div>
        
    </div>

    <div class="container" id="divpackid">

        <div class="navbarpack">
            <button id="returnhomeid" onclick="returnhome()">Home</button>
            <!-- <button id="returnhomeid" onclick="">Soon</button> -->
        </div>

        <div id="cagpackfivem">

            <div id="packreaid" class="packrea" onclick="packrealistefivem()">
                <!-- <img class="imgpackrea" src="img/packreaaaaa.png" onclick="packrealistefivem()"> -->
            </div>

            <div id="packfgfid" class="packfgf">
                <!-- <img src="img/PackGF.png" alt=""> -->
            </div>

            <div id="modsfid" class="modsf">
                <!-- <img src="img/modsfivem.png" alt=""> -->
            </div>

            <div id="packfsonid" class="packfson">
                <!-- <img src="img/Packson.png" alt=""> -->
            </div>
        </div>

    </div>

    <div id="console"></div>
    <div class="credit" id="creditid">
        <p>©Lafraude 2025</p>
    </div>
    <script>
        function updateConsole(message) 
        {
            const consoleElement = document.getElementById('console');
            consoleElement.innerText += message + "\\n";
        }

        function clearCache() 
        {
            updateConsole("Début de la suppression du cache fivem...");
            pywebview.api.clear_cache();
            updateConsole("Appel à la fonction...")
        }

        function clearMods() 
        {
            updateConsole("Mods cleared.");
            pywebview.api.clear_mods();  // Appel à la fonction Python pour supprimer les mods
        }

        window.onload = function() {
        var homediv = document.getElementById("divpackid");
        var packreadiv = document.getElementById("packrealistefivemid");
        var navbar = document.getElementById("navbar");

        if (Math.random() < 0) {
            packreadiv.style.setProperty("display", "block", "important");
        } else {
            packreadiv.style.setProperty("display", "none", "important");
        }
        
        if (Math.random() < 0) {
            homediv.style.setProperty("display", "block", "important");
        } else {
            homediv.style.setProperty("display", "none", "important");
        }

        if (Math.random() < 0) {
            navbar.style.setProperty("display", "block", "important");
        } else {
            navbar.style.setProperty("display", "none", "important");
        }
    };

        function packFivem() 
        {
            document.getElementById("btnfivemcag").addEventListener("click", function(){
                var homediv = document.getElementById("homeid");
                var consolediv = document.getElementById("console");
                var titlehome = document.getElementById("titlehome");
                var creditid = document.getElementById("creditid");
                var divpack = document.getElementById("divpackid");

                homediv.style.display = "none";
                consolediv.style.display = "none";
                titlehome.style.display = "none";
                creditid.style.display = "none";
                divpack.style.display = "block";
            })
        }

        function returnhome()
        {
            document.getElementById("returnhomeid").addEventListener("click", function(){
                var homediv = document.getElementById("homeid");
                var consolediv = document.getElementById("console");
                var titlehome = document.getElementById("titlehome");
                var creditid = document.getElementById("creditid");
                var divpack = document.getElementById("divpackid");
                var packreadiv = document.getElementById("packrealistefivemid");

                homediv.style.display = "block";
                consolediv.style.display = "block";
                titlehome.style.display = "block";
                creditid.style.display = "block";
                divpack.style.display = "none";
                packreadiv.style.display = "none";
            })
        }

        function packrealistefivem()
        // Possible erreur ici !
        {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");

            packreadiv.style.display = "block";
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
        }

        function executeOption(option) {
            window.pywebview.api.runOption(option)
                .then(response => updateConsole(response))
                .catch(err => updateConsole("Erreur : " + err));
        }

        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 10) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

    </script>
</body>
</html>
"""

html_file_path = "interface.html"
with open(html_file_path, "w") as file:
    file.write(html_content)

class Api:
    def __init__(self):
        self.config = self.load_config()

    def clear_cache(self):
        supprimer_cache()
        toaster.show_toast("Multi Tools Fivem", "✅ Confirmation, votre cache a été delete avec succès", icon_path=icon_path, duration=5)

    def clear_mods(self):
        startclearmods()  
        toaster.show_toast("Multi Tools Fivem", "✅ Confirmation, votre dossier mods a été delete avec succès", icon_path=icon_path, duration=5)

    def test(self):
        None
        print(f"test")

    def load_config(self):
        """Charge le fichier de configuration JSON."""
        try:
            with open("./src/config/config.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("❌ Le fichier config.json est introuvable.")
            return None

    def runOption(self, option):
        """Exécute l'option choisie en fonction du fichier de config."""
        if not self.config:
            return "❌ Impossible de charger la configuration."
        
        if option not in self.config:
            return "❌ Option inconnue dans la configuration."

        option_config = self.config[option]
        
        self.delete_items(option_config.get("delete", []))
        
        self.add_items(option_config.get("add", []))

        toaster = ToastNotifier()

        icon_path = os.path.join(os.getcwd(), './img/ico/logonotif.ico')

        toaster.show_toast("Multi Tools Fivem", 
                   "✅ Confirmation, votre pack a été initialisé avec succès", 
                   icon_path=icon_path, 
                   duration=10)

    def delete_items(self, items):
        """Supprime les fichiers ou dossiers."""
        for item in items:
            item = self.replace_user_variable(item)
            if os.path.exists(item):
                if os.path.isfile(item):
                    os.remove(item)
                    print(f"🗑️ Fichier supprimé : {item}")
                elif os.path.isdir(item):
                    shutil.rmtree(item)
                    print(f"🗑️ Dossier supprimé : {item}")
            else:
                print(f"⚠️ L'élément {item} n'existe pas.")

    def add_items(self, items):
        """Ajoute les fichiers ou dossiers existants."""
        for item in items:
            item = self.replace_user_variable(item)
            if os.path.exists(item):
                dest = f"destination/{os.path.basename(item)}"  
                if os.path.isdir(item):
                    shutil.copytree(item, dest)
                    print(f"📂 Dossier ajouté : {item} vers {dest}")
                elif os.path.isfile(item):
                    shutil.copy(item, dest)
                    print(f"📄 Fichier ajouté : {item} vers {dest}")
            else:
                print(f"⚠️ L'élément à ajouter {item} n'existe pas.")
                

    def replace_user_variable(self, path):
        """Remplace %USERNAME% par la valeur réelle de l'utilisateur."""
        if '%USERNAME%' in path:
            username = os.getenv("USERNAME")
            if username:
                path = path.replace("%USERNAME%", username)
            else:
                print("⚠️ La variable d'environnement USERNAME n'est pas définie.")
        return path


def run_app():
    api = Api()
    webview.create_window("Multi Tools Fivem", html_file_path, js_api=api)
    webview.start()

if __name__ == '__main__':
    run_app()
