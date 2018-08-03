import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")



@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!balance'):
        await client.send_message(message.channel, 'You don\'t have that much money!')













client.run("NDY4MjY3NzMzODQzMzEyNjgx.Di2sBg.Ua1XTKWYYiELg0GCyyAZZaWf4OY")
