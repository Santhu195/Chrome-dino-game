import os
import time
os.system("cd requirements && pip install -r requirements.txt")
os.system("clear")
print("wait untill installation is finished and after the game ctrl+c or cmd+z to exit")
time.sleep(5)
os.system("cd dino && python main.py")
