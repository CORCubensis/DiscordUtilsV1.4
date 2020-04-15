import discord
import datetime
import colorama
from colorama import Fore, Style
import asyncio
ver = "DiscordUtils 1.4"

async def chanclearcmd(message):
    await message.delete()
    channel = message.channel
    print(
        f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Style.RESET_ALL}\nDeleting messages..."
    )
    messages = await channel.history(limit=None).flatten()
    for message in messages:
        if message.author == bot.user:
            await message.delete()
    print(f"{Fore.GREEN}All messages deleted!{Style.RESET_ALL}\n")