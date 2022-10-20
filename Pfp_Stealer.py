import discord
import os
import socket

XiQ = discord.Client()

osuser = os.getlogin()


try:
    DIR = os.mkdir(f'C:\\Users\\{osuser}\\Downloads\\pfps')
except:
    DIR = f'C:\\Users\\{osuser}\\Downloads\\pfps'
PATH = f'{DIR}\\'


@XiQ.event
async def on_ready():
    while True:
        try:
            user = await XiQ.fetch_user(int(input('User ID: ')))
            Avatar = user.avatar_url
            Username = user.name.replace('<','').replace('>','').replace(' ','').replace('|','')
            PATH = f'C:\\Users\\{osuser}\\Downloads\\pfps\\'
            exists = False
            for i in range(0,2):
                y = ['png','gif']
                f = os.path.isfile(f'{PATH}{Username}\'s pfp.{y[i]}')
                if f and not exists:
                    exists = True
            h = user.is_avatar_animated()
            if not exists:
                if h:
                    await Avatar.save(f'{PATH}{Username}\'s pfp.gif')
                elif not h:
                    await Avatar.save(f'{PATH}{Username}\'s pfp.png')
            elif exists:
                t = os.listdir(PATH)
                x = 0
                for g in t:
                    if f'{Username}' in g:
                        x += 1
                if h:
                    await Avatar.save(f'{PATH}{Username}\'s pfp ({x}).gif') 
                elif not h:
                    await Avatar.save(f'{PATH}{Username}\'s pfp ({x}).png')
        except ValueError:
            continue
                
XiQ.run('ODc5ODk0OTIyMjk4Mjg2MTYw.GfdSmo.ZKmKW20zLXQ6rjdot8JZlWp1TY1e1QoLaFTiOU')

