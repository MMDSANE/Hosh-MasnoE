# # # Author : MMDSANE # # #
## Dear editor ; When i wrote this only god and i khow how this code works. Now only god knows.
## do not touch it PLEASE.
## DATE : 2024 / July / 1

import time
import datetime
import requests
import pygame
import cv2
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Smart Mirror")

cap = cv2.VideoCapture(0) 

def showtime():
  """نمایش زمان فعلی روی آینه"""
  now = datetime.datetime.now()
  font = pygame.font.Font(None, 64)
  text = font.render(now.strftime("%H:%M:%S"), True, (255, 255, 255))
  text_rect = text.get_rect(center=(screen.get_width() // 2, 100))
  screen.blit(text, text_rect)

def showdate():
  """نمایش تاریخ فعلی روی آینه"""
  now = datetime.datetime.now()
  font = pygame.font.Font(None, 32)
  text = font.render(now.strftime("%d %B %Y"), True, (255, 255, 255))
  text_rect = text.get_rect(center=(screen.get_width() // 2, 180))
  screen.blit(text, text_rect)

## !!!!!! tarjihan estefade Nakonid !!!!!!
def showWeather():
  """نمایش وضعیت آب و هوا از طریق API"""
  city = "tehran" 
  api_key = "YOUR_API_KEY"  ### agar API darid inja vared karde va az in def estefade konid ###

  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
  response = requests.get(url)
  data = response.json()

  if data["cod"] == "404":
    print("شهر مورد نظر یافت نشد!")
    return

  temp = round(data["main"]["temp"] - 273.15)
  description = data["weather"][0]["description"]

  font = pygame.font.Font(None, 48)
  temp_text = font.render(f"{temp}°C", True, (255, 255, 255))
  desc_text = font.render(description, True, (255, 255, 255))

  temp_rect = temp_text.get_rect(center=(screen.get_width() // 2, 300))
  desc_rect = desc_text.get_rect(center=(screen.get_width() // 2, 350))

  screen.blit(temp_text, temp_rect)
  screen.blit(desc_text, desc_rect)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  ret, frame = cap.read()

#   frame = cv2.flip(frame, 1)

#   frame = cv2.flip(frame, 1)

## braye rotate safhe be matrix apply midahim >>>> !!!! DO NOT TOUCH IT !!!!
  rotation_matrix = cv2.getRotationMatrix2D((frame.shape[1] // 2, frame.shape[0] // 1), 90, 1.2)


  rotated_frame = cv2.warpAffine(frame, rotation_matrix, (frame.shape[1], frame.shape[0]))

  frame = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)

  frame = pygame.surfarray.make_surface(frame)
  screen.blit(frame, (0, 0))

  showtime()
  showdate()
#   showWeather() # be khat 35 negah konid

  pygame.display.flip()
  pygame.transform.flip(frame, 100, 100)

  time.sleep(0.2)

cap.release()
pygame.quit()