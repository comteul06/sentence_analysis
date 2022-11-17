import discord
import data_writer as dw

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg_str = message.content
    if msg_str.startswith(COMMAND_INDICATOR):
        msg_str = msg_str[1 : : ]
        contents = msg_str.split(' ')
        
        if contents[0] == "sq" and not message.author.id in [x[0] for x in sq_queue]:
            sq_queue.append([message.author.id, dw.get_snt_empty()]) # index(csv)
            await message.channel.send(f'{sq_queue[len(sq_queue) - 1][1].sentence}\n(Input -1 if none)\nFind S')
    else:
        for i in range(len(sq_queue)):
            element = sq_queue[i]
            if element[0] == message.author.id:
                save_key = element[1].save(message.content)
                if save_key == 3:
                    await message.channel.send("Find V")
                elif save_key == 2:
                    await message.channel.send("Find O")
                elif save_key == 1:
                    await message.channel.send("Find C")
                elif save_key == 0:
                    await message.channel.send("Thank you for your cooperation!")
                    sq_queue.pop(i)

client.run('MTAzNzAzNTc4MzYzNjM4NTgwMg.GcLJgi.K_WPyOSZyHI5iHlbvWI0E2zgGvLd7bbJRa4T9E')
