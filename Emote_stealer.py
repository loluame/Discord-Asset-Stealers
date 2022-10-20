import discord,os
import requests as rq


XiQ = discord.Client()
osuser = os.getlogin()
try:os.listdir(f'C:\\Users\\{osuser}\\Downloads\\Emotes')
except:os.mkdir(f'C:\\Users\\{osuser}\\Downloads\\Emotes')
@XiQ.event
async def on_ready():
    while True:
        os.system('cls')
        print('Instruction:\nStep 1: type a "\\" into the chat box\nStep 2: Chose your desired emote and put it into the chat box\nStep 3: Send Message, you should see something that looks like this "<a:EmoteName:EmoteID>"\nStep 4: Copy the message content')
        Emote = input('Step 5: Paste Emote Here: ')
        EmoteID = int(Emote.split(':')[-1].replace('>',''))
        EmoteName = Emote.split(':')[1]
        try:
            x = rq.get(f'https://cdn.discordapp.com/emojis/{EmoteID}.gif?size=512&quality=lossless')
            if x.status_code != 200:
                print(sdgyf)
            a = x.content
            b = 'gif'
        except:
            a = rq.get(f'https://cdn.discordapp.com/emojis/{EmoteID}.png?size=512&quality=lossless').content
            b = 'png'
        c = os.listdir(f'C:\\Users\\{osuser}\\Downloads\\Emotes')
        x = 0
        for i in c:
            if i.split('.')[0] == EmoteName:x+=1
        if x == 0:pass
        elif x > 0:EmoteName+=f' {x}'
        with open(f'C:\\Users\\{osuser}\\Downloads\\Emotes\\{EmoteName}.{b}','wb') as f:f.write(a)

XiQ.run('ODc5ODk0OTIyMjk4Mjg2MTYw.GfdSmo.ZKmKW20zLXQ6rjdot8JZlWp1TY1e1QoLaFTiOU')
