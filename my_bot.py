import discord
import time

TOKEN = 'secret'

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
        else:
            msg = 'Bonjour {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith('>cool'):
        await client.send_message(message.channel, 'Qui est cool ? Ecris >name suivi du nom du membre')

        def check(msg):
            return msg.content.startswith('>name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('>name'):].strip()
        server = message.server
        find = server.get_member_named(name)
        if find is None:

            await client.send_message(message.channel, "L'utilisateur n'existe pas")
        else:
         await client.send_message(message.channel, '{} est cool effectivement'.format(find.mention))


    if message.content.startswith('>react'):
        msg = await client.send_message(message.channel, "Réagis à mon message avec l'émote de ton choix.")
        res = await client.wait_for_reaction(message=msg)
        await client.send_message(message.channel, '{0.user.mention} reacted with {0.reaction.emoji}!'.format(res))




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
