import discord
import time

TOKEN = 'NTAzMTY3MTI0NzE0NTUzMzQ0.Dqymtw.RnamHlYem-IyrgIOUCVsJk-rz9A'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>hello') or message.content.startswith('>bonjour'):
        now = time.strftime("%H")
        if (now>="18"):
            msg = 'Bonsoir {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)
        else :
            msg = 'Bonjour {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith('>cool'):
        await client.send_message(message.channel, 'Who is cool? Type >name namehere')

        def check(msg):
            return msg.content.startswith('>name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('>name'):].strip()
        await client.send_message(message.channel, '{} is cool indeed'.format(name))


    if message.content.startswith('>react'):
        msg = await client.send_message(message.channel, 'React with thumbs up or thumbs down.')
        res = await client.wait_for_reaction(message=msg)
        await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)