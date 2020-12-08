import discord
import utilities as util
import config

# secret token >:(
TOKEN = config.token

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
            reply = '{.author.mention} attach a pic to your message'
            await channel.send(reply.format(msg))


    if content.startswith('!haru post'):
        if util.numPics() < 1:
            reply = '{.author.mention} you have not added any pics'
            await channel.send(reply.format(msg))
        else:
            img = util.getPic()
            await channel.send(file = discord.File(p + img))
            await msg.add_reaction(u'\U0001F44D')

@client.event
async def on_ready():
    print('Running:')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

