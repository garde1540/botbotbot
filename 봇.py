import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("상태메시지")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/전달 건의"):
        msg = message.content[7:]
        await client .get_channel(int(690199478401237072)).send(msg)




@client.event
async def on_message(message):
    if message.content.startswith("/전달 자유"):
        msg = message.content[7:]
        await client .get_channel(int(716264699267776563)).send(msg)


        
        
client.run("NzI5OTk2MzcwNTQ2NTI0MjUx.XwRELQ._CSdHP9VcmOzCAXitCWPCu5pqNY")
