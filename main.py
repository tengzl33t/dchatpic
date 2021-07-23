from google_images_download import google_images_download
import discord
import time
import random
import os


## =============== Ebanij v rot ================
## =============== !!!! Super Puper Alpha Version !!!! ================
channel_id = 404321689422528524

class GetImage:
    def __init__(self, req_name):
        self.req_name = req_name
        self.arguments = {"keywords": self.req_name, "format": "jpg", "limit": 5, "size": "medium"}

    def download(self):
        response = google_images_download.googleimagesdownload()
        paths = response.download(self.arguments)
        return paths[0][self.req_name]

    def get_random(self):
        files = self.download()
        selected = random.choice(files)
        for f in files:
            if f is not selected:
                os.remove(f)
        return selected

    def __str__(self):
        return self.get_random()


class GetEvent:
    def every_day(self):
        return GetImage(f"{self.translate_dow(get_current_time()[2])} открытка")

    def translate_dow(self, dow):
        if dow == "Monday":
            return "Понедельник"
        elif dow == "Tuesday":
            return "Вторник"
        elif dow == "Wednesday":
            return "Среда"
        elif dow == "Thursday":
            return "Четверг"
        elif dow == "Friday":
            return "Пятница"
        elif dow == "Saturday":
            return "Суббота"
        elif dow == "Sunday":
            return "Воскресенье"

def get_current_time():
    current_time = time.strftime("%H:%M")  # check every minute so not count seconds
    current_date = time.strftime("%d.%m")
    current_dow = time.strftime("%A")
    return current_time, current_date, current_dow

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    channel = client.get_channel(channel_id)
    while True:
        if get_current_time()[0] == "23:26":
            image_path = str(GetEvent().every_day())
            await channel.send(file=discord.File(image_path))
            os.remove(image_path)  # removes used file
            os.rmdir(os.path.abspath(os.path.join(image_path, os.pardir)))  # removes empty directory
        time.sleep(60)

if __name__ == '__main__':
    client.run("ODMxNjQ3OTAyNjkzOTgyMjI4.YHYSdw.Ct-974U56swXO7_aoM30UKFfffE")

