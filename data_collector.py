import discord

#region Startup

COMMAND_INDICATOR = "!"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#endregion

sq_queue = []

class InputData:
    def __init__(self, str_index: int, userid: int):
        pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg_str = message.content
    if msg_str.startswith(COMMAND_INDICATOR):
        msg_str = msg_str[1 : : ]
        contents = msg_str.split(' ')
        
        if contents[0] == "sq":
            await message.channel.send('Find S')
            sq_queue.append([None, message.author.id, 3]) # NoneÀÚ¸®¿¡ µé¾î°¥ index(csv)ï¿½ï¿½ ï¿½ï¿½ ï¿½ï¿½ï¿½ï¿½
            await message.channel.send(sq_queue)
    else:
        for i in range(len(sq_queue)):
            element = sq_queue[i]
            if element[1] == message.author.id:
                if element[2] == 3:
                    await message.channel.send('Find V')
                    element[2] -= 1
                    await message.channel.send(sq_queue)
                elif element[2] == 2:
                    await message.channel.send('Find O')
                    element[2] -= 1
                    await message.channel.send(sq_queue)
                elif element[2] == 1:
                    await message.channel.send('Find C')
                    element[2] -= 1
                    await message.channel.send(sq_queue)
                else:
                    sq_queue.pop(i)
                    await message.channel.send('Thank you for your cooperation!')

client.run('MTAzNzAzNTc4MzYzNjM4NTgwMg.GcLJgi.K_WPyOSZyHI5iHlbvWI0E2zgGvLd7bbJRa4T9E')
