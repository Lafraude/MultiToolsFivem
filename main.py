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
    from src.spoofer365j import *
    from src.add_pack_admin import *
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
    <link rel="stylesheet" href="public/favoristyle.css">
    <link rel="stylesheet" href="public/loading.css">

    <style>
        &::-webkit-scrollbar {
          display: none;
        }

        #console::-webkit-scrollbar {
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

        .loading {
            font-size: 100px;
            display: flex;
            gap: 10px;
            font-weight: bold;
            text-shadow: 0 0 15px rgba(88, 166, 255, 0.8);
        }
        
        .loading span {
            display: inline-block;
            animation: blink 1.5s infinite ease-in-out;
        }
        
        @keyframes blink {
            0% { opacity: 0.2; }
            50% { opacity: 1; }
            100% { opacity: 0.2; }
        }
        
        .loading span:nth-child(1) { animation-delay: 0s; }
        .loading span:nth-child(2) { animation-delay: 0.2s; }
        .loading span:nth-child(3) { animation-delay: 0.4s; }

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
            font-weight: bold;
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

        .btnexit
        {
            margin-top: 10px;
            background-color: rgb(196, 1, 1);
            color: var(--text-color);
            font-weight: bold;
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
        .btnexit:hover {
            background-color: red;
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

        .imgstart {
            width: 200px;
            height: 200px;
            margin-top: 20px;
            border-radius: 50%;
            animation: fadeInUp 1.5s ease;
        }
        
      </style>

</head>
<body>

    <div class="loading" id="loadingid">
        <span>.</span>
        <span>.</span>
        <span>.</span>
    </div>

    <img class="imgstart" id="imgstartid" src="img/logo.jpg" alt="">
    <h1 id="titlehome">Bienvenue</h1>
    <iframe class="srcdiscordjoin" id="srcdiscordjoinid" src="https://discord.com/widget?id=1353365571369963643&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
    <button class="btnexit" id="btnexitid" onclick="widgetdiscordclose()">Exit</button>
    <div class="home" id="homeid">
        <button class="btn" onclick="clearCache()">Clear Cache</button>
        <button class="btn" onclick="clearMods()">Clear Mods</button>
        <button class="btn" id="btnfivemcag" onclick="packFivem()">Pack Fivem</button> <p>
        <button class="btn" onclick="widgetdiscord()">Discord</button>
        <button class="btn" onclick="spooferfivem()">Spoofer Fivem</button>
    </div>

    <div>
        <nav id="navbar" class="navbar">
            <img class="imgnavbar" onclick="returnhome()" src="/img/logo.jpg" alt="">
            <ul>
                <input type="text" id="searchBar" class="search-bar" placeholder="Rechercher..." oninput="filterDivs()">
                <button class="btnnav" onclick="returnhome()">Home</button>
                <button class="btnnav" onclick="packrealistefivem()">Pack Réaliste</button> 
                <button class="btnnav" onclick="packgunfightfivem()">Pack GunFight</button>
                <button class="btnnav" onclick="packsonfivem()">Pack Son</button> 
                <button class="btnnav" onclick="modsfivem()">Mods Fivem</button>
                <button class="btnnav" onclick="showFavoris()">Favoris</button>
                <button class="btnexit" onclick="returnhome()">Exit</button>
            </ul>
        </nav>
    </div>
    <div id="packrealistefivemid" class="packrealistefivem">
        <h2 class="titlepack">Pack Réaliste</h2>
        <div data-id="packrealiste-option1">
            <h4>Pack 1</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option1')">Exécuter Option 1</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packrealiste-option2">
            <h4>Pack 2</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option2')">Exécuter Option 2</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packrealiste-option3">
            <h4>Pack 3</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option3')">Exécuter Option 3</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packrealiste-option4">
            <h4>Pack 4</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option4')">Exécuter Option 4</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
    </div>
    
    <div id="packgunfightfivemid" class="packgunfight">
        <h2 class="titlepack">Pack GunFight</h2>
        <div data-id="packgunfight-option1">
            <h4>Pack 1</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option1')">Exécuter Option 1</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packgunfight-option2">
            <h4>Pack 2</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option2')">Exécuter Option 2</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packgunfight-option3">
            <h4>Pack 3</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option3')">Exécuter Option 3</button>
            <button class="btnF">Ajouter en favori</button>
        </div>
        <div data-id="packgunfight-option4">
            <h4>Pack 4</h4>
            <img class="packreaimg" src="img/200w.gif" alt="">
            <button class="btn" onclick="executeOption('option4')">Exécuter Option 4</button>
            <button class="btnF">Ajouter en favori</button>
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

            <div id="packfgfid" class="packfgf" onclick="packgunfightfivem()">
                <!-- <img src="img/PackGF.png" alt=""> -->
            </div>

            <div id="modsfid" class="modsf" onclick="modsfivem()">
                <!-- <img src="img/modsfivem.png" alt=""> -->
            </div>

            <div id="packfsonid" class="packfson" onclick="packsonfivem()">
                <!-- <img src="img/Packson.png" alt=""> -->
            </div>
        </div>

    </div>

    <div id="favoris-section" class="favoris-section" style="display: none;">
        <h2>Favoris</h2>
        <button class="btnresetF" onclick="resetFavoris()">Réinitialiser les favoris</button>
        <ul id="favoris-list"></ul>
    </div>
    

    <div class="commingsoonimg" id="commingsoonid">
        <img class="comingsoonimg" src="img/commingsoon.png" alt="">
    </div>

    <div id="console"></div>
    <div class="credit" id="creditid">
        <p>©Lafraude 2025</p>
    </div>

    <div class="spoofer" id="spooferid">
        <button class="btn" onclick="spooferdeclenchement()">Spoofer 365j</button>
        <button class="btnexit" onclick="returnhome()">Exit</button>
    </div>

    <div id="admin-interface" style="display: none;">
        <h2>Ajouter un Pack</h2>
    </div>

    <script>

        setTimeout(() => {
            const loading = document.getElementById('loadingid');
            const message = document.getElementById('homeid');
            const titlehome = document.getElementById('titlehome');
            const creditid = document.getElementById('creditid');
            const console = document.getElementById('console');
            const imgstartid = document.getElementById('imgstartid');

            if (loading && message) {
                loading.style.display = 'none';
                message.style.display = 'block';
                titlehome.style.display = 'block';
                creditid.style.display = 'block';
                console.style.display = 'block';
                imgstartid.style.display = 'block';
                setTimeout(() => {
                    message.style.opacity = '1';
                }, 100);
            }
        }, 3000);

        function updateConsole(message) 
        {
            const consoleElement = document.getElementById('console');
            consoleElement.innerText += message + "\\n";
        }

        function addpack()
        {
            pywebview.api.add_pack();
        }

        function clearCache() 
        {
            pywebview.api.clear_cache();
        }

        function clearMods() 
        {
            pywebview.api.clear_mods();  // Appel à la fonction Python 
        }

        function spooferdeclenchement()
        {
            pywebview.api.spoofer_declenchement();  // Appel à la fonction Python 
        }

        function executeOption(option) {
            if (option) {
                pywebview.api.runOption(option)
                    .then(response => {
                        updateConsole(response); // Affiche le message de retour dans la console
                        console.log(response);
                    })
                    .catch(error => {
                        console.error("Erreur lors de l'exécution de l'option :", error);
                    });
            } else {
                console.error("Aucune option spécifiée.");
            }
        }

        window.onload = function() 
        {
            var homediv = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var navbar = document.getElementById("navbar");
            var packgf = document.getElementById("packgunfightfivemid");
            var srcdiscordjoinid = document.getElementById("srcdiscordjoinid");
            var btnexitid = document.getElementById("btnexitid");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");
            var homeid = document.getElementById("homeid");
            var creditid = document.getElementById("creditid");
            var titlehome = document.getElementById("titlehome");
            var console = document.getElementById("console");
            var spooferid = document.getElementById("spooferid");
            var imgstartid = document.getElementById("imgstartid");

            if (Math.random() < 0) {
                packreadiv.style.setProperty("display", "block");
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
            if (Math.random() < 0) {
                packgf.style.setProperty("display", "block", "");
            } else {
                packgf.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                srcdiscordjoinid.style.setProperty("display", "block", "important");
            } else {
                srcdiscordjoinid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                btnexitid.style.setProperty("display", "block", "important");
            } else {
                btnexitid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                commingsoonid.style.setProperty("display", "block", "important");
            } else {
                commingsoonid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                favorislist.style.setProperty("display", "block", "important");
            } else {
                favorislist.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                homeid.style.setProperty("display", "block", "important");
            } else {
                homeid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                creditid.style.setProperty("display", "block", "important");
            } else {
                creditid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                titlehome.style.setProperty("display", "block", "important");
            } else {
                titlehome.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                console.style.setProperty("display", "block", "important");
            } else {
                console.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                spooferid.style.setProperty("display", "block", "important");
            } else {
                spooferid.style.setProperty("display", "none", "important");
            }
            if (Math.random() < 0) {
                imgstartid.style.setProperty("display", "block", "important");
            } else {
                imgstartid.style.setProperty("display", "none", "important");
            }
        };

        function widgetdiscord()
        {
            var srcdiscordjoinid = document.getElementById("srcdiscordjoinid");
            var homeid = document.getElementById("homeid");
            var console = document.getElementById("console");
            var btnexitid = document.getElementById("btnexitid");
            var imgstartid = document.getElementById("imgstartid");

            srcdiscordjoinid.style.display = "block";
            homeid.style.display = "none";
            console.style.display = "none";
            imgstartid.style.display = "none";
            btnexitid.style.display = "block";

        }

        function widgetdiscordclose()
        {
            var srcdiscordjoinid = document.getElementById("srcdiscordjoinid");
            var homeid = document.getElementById("homeid");
            var console = document.getElementById("console");
            var btnexitid = document.getElementById("btnexitid");
            var commingsoonid = document.getElementById("commingsoonid");
            var imgstartid = document.getElementById("imgstartid");

            srcdiscordjoinid.style.display = "none";
            homeid.style.display = "block";
            console.style.display = "block";
            btnexitid.style.display = "none";
            commingsoonid.style.display = "none";
            imgstartid.style.display = "block";
        }

        function packFivem() 
        {
            document.getElementById("btnfivemcag").addEventListener("click", function(){
                var homediv = document.getElementById("homeid");
                var consolediv = document.getElementById("console");
                var titlehome = document.getElementById("titlehome");
                var creditid = document.getElementById("creditid");
                var divpack = document.getElementById("divpackid");
                var favorislist = document.getElementById("favoris-list");
                var imgstartid = document.getElementById("imgstartid");

                homediv.style.display = "none";
                consolediv.style.display = "none";
                titlehome.style.display = "none";
                creditid.style.display = "none";
                divpack.style.display = "block";
                favorislist.style.display = "none";
                imgstartid.style.display = "none";

            })
        }

        function returnhome() 
        {
            var homediv = document.getElementById("homeid");
            var consolediv = document.getElementById("console");
            var titlehome = document.getElementById("titlehome");
            var creditid = document.getElementById("creditid");
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");
            var spooferid = document.getElementById("spooferid");
            var imgstartid = document.getElementById("imgstartid");


            homediv.style.display = "block";
            consolediv.style.display = "block";
            titlehome.style.display = "block";
            creditid.style.display = "block";
            divpack.style.display = "none";
            navbar.style.display = "none";
            commingsoonid.style.display = "none";
            favorislist.style.display = "none";
            spooferid.style.display = "none";
            imgstartid.style.display = "block";


            packreadiv.style.setProperty("display", "none", "important");
            packgf.style.setProperty("display", "none", "important");
            document.getElementById("favoris-section").style.display = "none";

        }

        function packrealistefivem()
        // Possible erreur ici !
        {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");


            packreadiv.style.display = "block";
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
            commingsoonid.style.display = "none";
            favorislist.style.display = "none";

            packreadiv.style.setProperty("display", "flex", "important");
            packgf.style.setProperty("display", "none", "important");
            document.getElementById("favoris-section").style.display = "none";
        }

        function packgunfightfivem()
        {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");


            packreadiv.style.setProperty("display", "none", "important");
            packgf.style.setProperty("display", "flex", "important");
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
            commingsoonid.style.display = "none";
            favorislist.style.display = "none";
            document.getElementById("favoris-section").style.display = "none";
        }

        function modsfivem()
        {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");


            packreadiv.style.setProperty("display", "none", "important");
            packgf.style.setProperty("display", "none", "important");
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
            commingsoonid.style.display = "block";
            favorislist.style.display = "none";
            document.getElementById("favoris-section").style.display = "none";
        }

        function packsonfivem()
        {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");


            packreadiv.style.setProperty("display", "none", "important");
            packgf.style.setProperty("display", "none", "important");
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
            commingsoonid.style.display = "block";
            favorislist.style.display = "none";
            document.getElementById("favoris-section").style.display = "none";
        }

        let favoris = JSON.parse(localStorage.getItem("favoris")) || [];

        function toggleFavori(itemId) {
            if (favoris.includes(itemId)) {
                favoris = favoris.filter(id => id !== itemId);
            } else {
                favoris.push(itemId);
            }
            localStorage.setItem("favoris", JSON.stringify(favoris));
            refreshFavoris();
        }

        function refreshFavoris() {
            const favorisList = document.getElementById("favoris-list");
            favorisList.innerHTML = "";
            favoris.forEach(id => {
                const li = document.createElement("li");
                li.textContent = id;
                favorisList.appendChild(li);
            });
        
            document.querySelectorAll("[data-id]").forEach(item => {
                const itemId = item.getAttribute("data-id");
                if (favoris.includes(itemId)) {
                    item.classList.add("favori");
                } else {
                    item.classList.remove("favori");
                }
            });
        }

        function showFavoris() {
            var divpack = document.getElementById("divpackid");
            var packreadiv = document.getElementById("packrealistefivemid");
            var packgf = document.getElementById("packgunfightfivemid");
            var homeid = document.getElementById("homeid")
            var navbar = document.getElementById("navbar");
            var commingsoonid = document.getElementById("commingsoonid");
            var favorislist = document.getElementById("favoris-list");

            packreadiv.style.display = "block";
            divpack.style.display = "none";
            homeid.style.display = "none"
            navbar.style.display = "block";
            commingsoonid.style.display = "none";
            favorislist.style.display = "block";

            packreadiv.style.setProperty("display", "none", "important");
            packgf.style.setProperty("display", "none", "important");
            document.getElementById("favoris-section").style.display = "flex";
        }

        function resetFavoris() {
            favoris = [];
            localStorage.removeItem("favoris");
            refreshFavoris();
            alert("Les favoris ont été réinitialisés !");
        }

        document.addEventListener("DOMContentLoaded", () => {
            document.querySelectorAll("[data-id]").forEach(item => {
                item.addEventListener("click", () => {
                    const itemId = item.getAttribute("data-id");
                    toggleFavori(itemId);
                });
        });

        refreshFavoris();
    });

    function filterDivs() {
        const searchTerm = document.getElementById("searchBar").value.toLowerCase();
        const divs = document.querySelectorAll("[data-id]");

        divs.forEach(div => {
            const title = div.querySelector("h4")?.textContent.toLowerCase() || "";
            if (title.includes(searchTerm)) {
                div.style.display = "block";
            } else {
                div.style.display = "none";
            }
        });
    }

    function spooferfivem()
    {
        var divpack = document.getElementById("divpackid");
        var packreadiv = document.getElementById("packrealistefivemid");
        var packgf = document.getElementById("packgunfightfivemid");
        var homeid = document.getElementById("homeid")
        var navbar = document.getElementById("navbar");
        var commingsoonid = document.getElementById("commingsoonid");
        var favorislist = document.getElementById("favoris-list");
        var titlehome = document.getElementById("titlehome");
        var console = document.getElementById("console");
        var creditid = document.getElementById("creditid");
        var spooferid = document.getElementById("spooferid");

        packreadiv.style.setProperty("display", "none", "important");
        packgf.style.setProperty("display", "none", "important");
        divpack.style.display = "none";
        homeid.style.display = "none"
        navbar.style.display = "none";
        commingsoonid.style.display = "none";
        favorislist.style.display = "none";
        titlehome.style.display = "none";
        console.style.display = "none";
        creditid.style.display = "none";
        spooferid.style.display = "block";
        document.getElementById("favoris-section").style.display = "none";
    }

    // const authorizedIPs = ["", ""];
    // async function checkAdminAccess() {
    //     try {
    //         const response = await fetch("https://api.ipify.org?format=json");
    //         const data = await response.json();
    //         const userIP = data.ip;
        
    //         console.log("Adresse IP détectée :", userIP);
        
    //         if (authorizedIPs.includes(userIP)) {
    //             document.getElementById("admin-interface").style.display = "block";
    //         } else {
    //             NaN
    //         }
    //     } catch (error) {
    //         console.error("Erreur lors de la vérification de l'IP :", error);
    //     }
    // }
    
    document.addEventListener("DOMContentLoaded", checkAdminAccess);
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

    def spoofer_declenchement(self):
        clear_digital_entitlements()
        toaster.show_toast("Multi Tools Fivem", "✅ Confirmation, vous avez été spoof avec succès", icon_path=icon_path, duration=5)

    def add_pack(self):
        toaster.show_toast("Multi Tools Fivem", "✅ Confirmation, votre pack a été ajouté avec succès", icon_path=icon_path, duration=5)

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
            return f"❌ Option '{option}' inconnue dans la configuration."

        option_config = self.config[option]

        self.delete_items(option_config.get("delete", []))
        self.add_items(option_config.get("add", []))

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
                dest = os.path.join(os.getenv("LOCALAPPDATA"), "FiveM", "FiveM.app", os.path.basename(item))
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