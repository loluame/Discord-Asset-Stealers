import discord
from discord.utils import get
import os
import requests

XiQ = discord.Client()

osuser = os.getlogin()

SubFolder = 'Downloads'
try:DIR = os.mkdir(f'C:\\Users\\{osuser}\\{SubFolder}\\banners')
except:DIR = f'C:\\Users\\{osuser}\\{SubFolder}\\banners'

@XiQ.event
async def on_ready():
    while True:
            PATH = f'C:\\Users\\{osuser}\\Downloads\\banners\\'
            user = await XiQ.fetch_user(int(input('User ID: ')))
            req = await XiQ.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
            banner_id = req["banner"]
            if banner_id:banner = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            if not banner_id:print('No Banner Found')
            benner = requests.get(banner)
            banners = os.listdir(PATH)
            exists = False
            for banner in banners:
                if f'{user.name}' in banner:exists = True
                else:continue
            if not exists:
                with open(f'{PATH}{user.name}\'s Banner.png','wb') as g:
                        g.write(benner.content)
                        g.close()
                        name = f'{PATH}{user.name}\'s Banner.png'
            elif exists:
                t = os.listdir(PATH)
                x = 0
                for g in t:
                    if f'{user.name}' in g:
                        x += 1
                with open(f'{PATH}{user.name}\'s Banner ({x}).png','wb') as g:
                        g.write(benner.content)
                        g.close()
                        name = f'{PATH}{user.name}\'s Banner ({x}).png'
            e = open(name,'rb').read()
            if 'GIF' in str(e):
                nameGif = name.replace('.png','.gif')
                os.rename(name,nameGif)

XiQ.run('ODc5ODk0OTIyMjk4Mjg2MTYw.GfdSmo.ZKmKW20zLXQ6rjdot8JZlWp1TY1e1QoLaFTiOU')
