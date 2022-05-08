import discord
import asyncio

client = discord.Client()
token = "OTcyNzEwMDM0MzQ3ODE0OTUy.GUxGJl.NMLEvep-x68lu989Nv4DwL0IPDPxOSoAhxedqQ"


@client.event
async def on_message(message):
    if message.author.bot: return
    if message.content == "안녕":
        return await message.channel.send("안녕하세요")



client.run(token)