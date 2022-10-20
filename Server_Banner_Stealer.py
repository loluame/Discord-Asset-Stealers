import requests,os

osuser = os.getlogin()

def GetHtml(Code):
    Data = requests.get(f'https://discord.com/api/invites/{Code}').text
    GuildID = Data.split('{"id": ')[1].split(',')[0].replace('"','')
    ImageID = Data.split('"banner": ')[1].split(',')[0].replace('"','')
    Image = requests.get(f'https://cdn.discordapp.com/banners/{GuildID}/{ImageID}.webp?size=480').url
    return Image
    

def GetName(Code):
    Name = requests.get(f'https://discord.com/api/invites/{Code}').text.split('"name": ')[1].split(',')[0].replace('"','')
    return Name



def GetImage(Invite):
    Image = requests.get(GetHtml(Invite)).content
    FileName = GetName(Invite)
    Items = os.listdir(f'C:\\Users\\{osuser}\\Downloads\\Server Banners')
    x=0
    for item in Items:
        if item.split('.')[0] == FileName: x+=1
    if x == 0:
        with open(f'C:\\Users\\{osuser}\\Downloads\\Server Banners\\{FileName}.png','wb') as icon:icon.write(Image)
    elif x != 0:
        with open(f'C:\\Users\\{osuser}\\Downloads\\Server Banners\\{FileName}({x+1}).png','wb') as icon:icon.write(Image)

def Setup():
    os.system('cls')
    try:
        Exists = os.listdir(f'C:\\Users\\{osuser}\\Downloads\\Server Banners')
        Exists = True
    except:Exists=False
    if Exists:pass
    elif not Exists:
        os.mkdir(f'C:\\Users\\{osuser}\\Downloads\\Server Banners')
    Invite = input('Server Invite: ').split('/')[-1]
    GetImage(Invite)

while True:
    Setup()
