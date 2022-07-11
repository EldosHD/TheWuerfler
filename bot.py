import discord
import random
from discord.ext import commands

krit_erfolg=["Kritischer Erfolg, gib ihm.","Mit dir ist eben nicht zu spaßen!","Das Geheimnis des Erfolgs ist anzufangen.","Erfolg hat drei Buchstaben: TUN - Goethe","Erfolg ist nicht etwas, das einfach passiert.","Nicht nur wiederholen, gelegentlich auch überholen.","Sei du selbst die Veränderung, die du dir wünschst für diese Welt.","Suche nicht nach Fehlern, suche nach Lösungen.","Ist dein Verlangen gross genug, wird man glauben, du hast übermenschliche Kräfte.","Wer die Freiheit aufgibt, um Sicherheit zu gewinnen, wird am Ende beides verlieren."]
krit_misserfolg=["Ouh, that one hurt.","Schade Marmelade ;)","Es gibt Tage, die laufen alles andere als nach Plan.","Vielleicht fiel das Training aus...","Einige würden das Misserfolg nennen.","Aber in Wirklichkeit sind solche vermeintlichen Rückschritte Teil jedes erfolgreichen Lebens.","Misserfolge sind Wegweiser auf dem Weg zum Erfolg.","Scheitern ist einfach nur eine Möglichkeit, es nochmals zu versuchen.","Wer noch nie einen Misserfolg hatte, hat noch nie etwas Neues versucht. - Albert Einstein","Wenn Du immer tust, was Du immer getan hast, bekommst Du immer, was Du immer bekommen hast. - Mark Twain"]
print(len(krit_erfolg))
print(len(krit_misserfolg))
bot=commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("I'm online!")

@bot.event
async def on_message(message):
    if message.author.bot:#bot reagiert nicht auf sich selbst
        return
    if message.content.startswith("!"):
        for y in range(1,101):
            for x in range(1,101):
                ziel = str(y) + "d" + str(x)
                if ziel in message.content:
                    dice_list=[]
                    dice_val=0
                    for dice in range(1,y+1):
                        dice_val_act=random.randint(1,x)
                        dice_list.append(dice_val_act)
                        dice_val+=dice_val_act
        await message.channel.send(str(dice_list)+" , sum ="+str(dice_val))
    if message.content.startswith("ds!"):
        for y in range(1,101):
            for x in range(1,101):
                ziel = str(y) + "d" + str(x)
                if ziel in message.content:
                    y_val=y
                    dice_list=[]
                    dice_val=0
                    for dice in range(1,y+1):
                        dice_val_act=random.randint(1,x)
                        #if x==20: #zum spruch testen
                        #    dice_val_act=1
                        dice_list.append(dice_val_act)
                        dice_val+=dice_val_act
                    postmes=""
                    if x==20 and y==1:
                        if 20 in dice_list:
                            spruch=random.randint(0, len(krit_misserfolg)-1)
                            postmes=krit_misserfolg[spruch]
                        if 1 in dice_list:
                            spruch = random.randint(0, len(krit_erfolg)-1)
                            postmes = krit_erfolg[spruch]
        if y_val==1:
            await message.channel.send(str(dice_list) + " " + postmes)
        else:
            await message.channel.send(str(dice_list)+" , sum ="+str(dice_val)+" "+postmes)
    else:
        return

bot.run("Bot-Token")