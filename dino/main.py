from selenium import webdriver
from sys import platform
from PIL import Image, ImageGrab
import pyautogui as gui
import time


def hit(key):
  gui.keyDown(key)
  return

if platform == "linux" or platform == "linux2":
    browser = webdriver.Chrome("drivers\chromedriver_linux64\chromedriver")
elif platform == "darwin":
    browser = webdriver.Chrome("drivers\chromedriver_mac64\chromedriver")
elif platform == "win32":
    browser = webdriver.Chrome("drivers\chromedriver_win32\chromedriver.exe")
print(platform)   
browser.get("chrome://dino/")
time.sleep(2)
hit('space')

def isCollide(data):
  # Draw the rectangle for birds
  for i in range(300, 415):
    for j in range(410, 563):
      if data[i, j] < 100:
        hit("down")
        return

  for i in range(287, 495):
    for j in range(542, 666):
      if data[i, j] < 90:
        hit("up")
        return
  return

if __name__ == "__main__":
  print("Hey.. Dino game about to start in 4 seconds")
  time.sleep(4)
  # hit('up') 
  try:
    while True:
      image = ImageGrab.grab().convert('L')  
      data = image.load()
      isCollide(data)
  except KeyboardInterrupt:
    pass
    
  
    # # Draw the rectangle for cactus
    # for i in range(287, 495):
    #   for j in range(545, 665):
    #     data[i, j] = 0
    
    # # Draw the rectangle for birds
    # # for i in range(300, 415):
    # #   for j in range(410, 563):
    # #     data[i, j] = 171

    # image.show()
    # break