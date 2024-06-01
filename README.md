# Rainbow-Six-siege-script-to-find-cheaters
If you have never used python before you will need to install requests and bs4 beautifulsoup with pip. 

This script was coded in python and looks up everyone in your lobby. This works by grabbing the account IDs of all players by using the avatars folder and looks them up on stats.cc.

This script is capable of getting stats before a game starts giving you a chance to dodge cheaters before it starts(this is rare as typically you instantly find a game but ive done it a few times)

Make sure after each game you delete your avatars in C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\cache\avatars when you launch the game otherwise when you start the script again it will display previous players you versed.




Blue output = important look at it

If the KD is over 1.5 their KD will be blue showing you to look at it, if their account level is under 150 it will also be blue.


Example of blue KD and Blue levels

![image](https://github.com/jordan01236/Rainbow-Six-siege-script-to-find-cheaters/assets/120287007/9df0444f-ba4f-44e3-ab76-f7b67a3cb132)
![image](https://github.com/jordan01236/Rainbow-Six-siege-script-to-find-cheaters/assets/120287007/b200fab9-299e-4e09-9b6f-a8f4118c8aa2)

Red output = sus stats, you should probably dodge.

If KD is over 2.0 it will show in red

If the cheater is banned on stats.cc you will get a red error message showing they are banned.


Example

![image](https://github.com/jordan01236/Rainbow-Six-siege-script-to-find-cheaters/assets/120287007/f975a3f2-38f1-49d6-8273-d4facc52647e)

Green output = Person sucks so either an easy game or they are queued with a cheater

Green output is if the player has under a 1.0 KD

![image](https://github.com/jordan01236/Rainbow-Six-siege-script-to-find-cheaters/assets/120287007/b1d7ff9a-2d6e-4b3d-b05b-eac8dccf4985)


If you know someone was cheating but they dont have sus stats you can create a folder at C:\ named Cheaters and inside that folder create a Cheaters.txt file. Add the account ID to that file and if you verse them again it will output in red showing you they are cheating.


