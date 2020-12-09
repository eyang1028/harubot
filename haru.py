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
    content = '%s' % msg.content
    p = './pics/'

    if content.lower().startswith('!haru hi'):
        reply = 'hi {.author.mention}, you simp'
        await channel.send(reply.format(msg))

    if content.lower().startswith('!haru add'):
        if len(msg.attachments) > 0:
            for i in msg.attachments:
                if util.isImage(i):
                    await i.save(p + i.filename)
                    await msg.add_reaction(u'\U0001F44D')
        else:
            reply = '{.author.mention} attach a pic to add to your message'
            await channel.send(reply.format(msg))


    if content.lower().startswith('!haru post'):
        if util.numPics() < 1:
            reply = '{.author.mention} you have not added any pics'
            await channel.send(reply.format(msg))
        else:
            img = util.getPic()
            await channel.send(file = discord.File(p + img))
            await msg.add_reaction(u'\U0001F44D')

    if content.lower().startswith('!haru del'):
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

    if content.lower().startswith('!haru say'):
        if content.rstrip().lower() == '!haru say':
            reply = 'usage: !haru say insert-something-here'
        else:
            await channel.delete_messages([msg])
            reply = content[10:]
        await channel.send(reply.format(msg))

    if content.lower().startswith('!haru kiss'):
        self = False
        if len(msg.mentions) > 0:
            user_id = msg.mentions[0].id
            if user_id == client.user.id:
                self = True
                reply = 'i can\'t kiss myself...'
            else:
                to_mention = '<@' + str(user_id) + '>'
        else:
            to_mention = '{.author.mention}'

        if not self:
            rand = util.getRandom()
            if rand < 0.25:
                reply = to_mention + ' smooch ' + u'\U0001F618'
            elif rand < 0.50:
                reply = to_mention + ' ewww no ' + u'\U0001F92E'
            elif rand < 0.75:
                await channel.send(file = discord.File('./ryo.png'))
                reply = to_mention + ' ryo: \"haha, you really think you can kiss my haru?\"'
            else:
                await channel.send(file = discord.File('./daisuke.png'))
                reply = to_mention + ' daisuke: \"get away from my haru.\"'
        await channel.send(reply.format(msg))

@client.event
async def on_ready():
    print('Running:')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

