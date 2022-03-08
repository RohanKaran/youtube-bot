import datetime
from selenium.webdriver.common.by import By
from youtube.youtube import YouTube
from google_client.gspwrite import write

with YouTube(teardown=True) as bot:
    bot.land_first_page()
    rand = bot.find_elements(By.ID, "details")
    for i in range(len(rand)):
        if rand[i].find_element(By.ID, "video-title").text:
            write([[str(datetime.datetime.now()), rand[i].find_element(By.ID, "video-title").text,
              rand[i].find_element(By.ID, "channel-name").text]])
