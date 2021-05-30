import discord
token = "ODQ4MDYyMzA3MzI1MDUwOTEw.YLHJkg.DxtjLbh_CQh5oarts3tHeDHZrOQ"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료")
    print(client.user)
    print("=============================")

@client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")

    if message.content == "임베드":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="제-목", description="설-명")
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

client.run(token)