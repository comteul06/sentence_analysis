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
    cnt = 3
    sbj = ""
    vrb = ""
    obj = ""
    cmpl = ""

    str_index = -1

    def __init__(self, str_index: int):
        self.str_index = str_index

    @property
    def count(self):
        return self.cnt

    def __str__(self):
        return f"{self.cnt}, {self.sbj}, {self.vrb}, {self.obj}, {self.cmpl}"

    def save(self, save_data):
        if self.cnt == 3:
            self.sbj = save_data
        elif self.cnt == 2:
            self.vrb = save_data
        elif self.cnt == 1:
            self.obj = save_data
        else:
            self.cmpl = save_data
        self.cnt -= 1
        return self.cnt + 1
    
    def to_list(self):
        return [self.str_index, self.sbj, self.vrb, self.obj, self.cmpl]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg_str = message.content
    if msg_str.startswith(COMMAND_INDICATOR):
        msg_str = msg_str[1 : : ]
        contents = msg_str.split(' ')
        
        if contents[0] == "sq" and not message.author.id in [x[0] for x in sq_queue]:
            await message.channel.send('Find S')
            sq_queue.append([message.author.id, InputData(-1)]) # index(csv)
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
