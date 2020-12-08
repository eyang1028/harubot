import discord
import utilities as util

# secret token >:(
TOKEN = util.getToken()

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    channel = msg.channel
    content = msg.content.lower()
    p = './pics/'

    if content.startswith('!haru hi'):
        reply = 'hi {.author.mention}, you simp'
        await channel.send(reply.format(msg))

    if content.startswith('!haru add'):
        if len(msg.attachments) > 0:
            for i in msg.attachments:
                if util.isImage(i):
                    await i.save(p + i.filename)
                    await msg.add_reaction(u'\U0001F44D')
        else:
            reply = '{.author.mention} attach a pic to add to your message'
            await channel.send(reply.format(msg))


    if content.startswith('!haru post'):
        if util.numPics() < 1:
            reply = '{.author.mention} you have not added any pics'
            await channel.send(reply.format(msg))
        else:
            img = util.getPic()
            await channel.send(file = discord.File(p + img))
            await msg.add_reaction(u'\U0001F44D')

    if content.startswith('!haru del'):
        if len(msg.attachments) > 0:
            for i in msg.attachments:
                if util.isImage(i):
                    if not util.delPic(i.filename):
                        reply = '{.author.mention} pic does not exist'
                        await channel.send(reply.format(msg))
                    else:
                        await msg.add_reaction(u'\U0001F44D')
        else:
            reply = '{.author.mention} attach a pic to delete to your message'
            await channel.send(reply.format(msg))

    if content.startswith('!haru kiss'):
        rand = util.getRandom()
        if rand < 0.25:
            reply = '{.author.mention} smooch ' + u'\U0001F618'
        elif rand < 0.50:
            reply = '{.author.mention} ewww no ' + u'\U0001F92E'
        elif rand < 0.75:
            await channel.send(file = discord.File('./ryo.png'))
            reply = '{.author.mention} ryo: \"haha, you really think you can kiss my haru?\"'
        else:
            await channel.send(file = discord.File('./daisuke.png'))
            reply = '{.author.mention} daisuke: \"get away from my haru.\"'
        await channel.send(reply.format(msg))

@client.event
async def on_ready():
    print('Running:')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

