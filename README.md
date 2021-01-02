# TerminalGames
TerminalGames is a gaming center made in python
# How to install (for Windows 10)
Go to the Microsoft Store and search for "Python 3.8". Go to the Python 3.8 program, and press "Install". You can log in with your Microsoft account, but you don't have to. Next, download the git repository as a zip file and unzip. Then, scroll down here to find out how to open...

For some games, you need Java JDK SE 15. These include hoogsteKaart and UNO. If you play Minecraft and use a mod called Optifine, you already have this installed. Else, you should check if you have it installed with the command "java --version" in the cmd program. If you get an error message like "java is not recocnized", you should download Java JDK at [Orcale's website](https://www.oracle.com/be/java/technologies/javase-jdk15-downloads.html) (use the Windows x64 installer)
# How to install (for Ubuntu and variants)
Download the git repository as a zip file. Unzip everything (best in a folder called TerminalGames-main, for the updater) and delete the installers folder, it's just for MacOS. Open the terminal, ant run "sudo apt update" and "sudo apt upgrade". This will update your whole OS, just like the update manager will do. Then use the cd command to go to the place you unzipped the files, run "python3 main.py" and enjoy your games!

For some games, you need Java JDK SE 15. These include hoogsteKaart and UNO. If you play Minecraft and use a mod called Optifine, you already have this installed. Else, you should check if you have it installed with the command "java --version" in the cmd program. If you get an error message like "java is not recocnized", you should download Java JDK at [Orcale's website](https://www.oracle.com/be/java/technologies/javase-jdk15-downloads.html) (use the Linux x64 Debian Package)
# How to update (for Ubuntu and variants)
Make sure the installation folder is called TerminalGames-main. Else, the update will not install in the correct folder and the program will run the old version of TerminalGames. After you are in the correct folder (cd to get there), run "python3 updater.py". This program needs to run as ROOT if you are updating the first time. The program will automatically search for updates on my web server, and then install them. If your updater askes to overwrite a file, type "A" from "All" to overwrite the old TerminalGames files.
# System requierments
All games are tested on a 2.5Ghz CPU and are single core. Just make sure your CPU can go higher than 2.5Ghz and it should work. For Hard disk or SSD room, I recommend having 1GB of free room. For screen resolution, please do nothing higher than 1920x1080. I will try to test them later on higher resolutions, but 4K and bigger is probably too big for some games. Lower resolution is better, but please don't run this on 800x600. The only reason you need a powerful GPU is if you are playing on an 8K TV, and that could be too big for those games...

The chess program does need a modern cpu to run this. I tested it on a 4th generation Intel cpu, and that worked. If you got a Ryzen or Zen-based Athlon, it will also work just fine. But I think second-gen Intel CPU or AMD Phenom II, it will crash before it gave you the chance to move e4.
# How to open (for Windows 10)
Use the search bar and search "cmd". Open the windows terminal, and use the cd command to go to the place where you unzipped all the files. Then, just run "python3 main.py", and enjoy your games!
# How to help making it better
Thank you if you want to help. You can fork this repository and start a pull request if you want to help. This is the easiest way to help most. If you are not fammiliar with Python, you can also test the beta versions of TerminalGames and report bugs you find.
# What is it about? (Description)
TerminalGames started as PyGames, as a holiday project to practace for my Python exam. After my python exam was moved because of Covid, I needed a way to don't forget my python stuff. When I found out that Java could also be used for games in the terminal, I renamed the project to TerminalGames. Fun fact, the project folder on my PC is still called PyGames! This is actually more for fun, but also for fun for you, because you can get 
* A new way of playing UNO
* Singleplayer memory
* A weird way of playing hangman
* (one of) The strongest chess program availible
