import discord
import datetime
import colorama
from colorama import Fore, Style
import asyncio
ver = "DiscordUtils 1.4"

async def chatlogcmd(message):
    channel = message.channel
    await message.delete()
    if isinstance(message.channel, discord.DMChannel):
        print(f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Style.RESET_ALL}\nLogging messages with {channel.recipient}...")
        f = open(f"MessageLogs/MESSAGE HISTORY - {channel.recipient}.txt", 'w')
        channelname = channel.recipient
        f.write(
            f"-DM logged with {ver}-\n \nMESSAGE HISTORY - {channelname}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
        )
        endmsg = f"{Fore.GREEN}Finished logging messages with {Style.RESET_ALL}{channel.recipient}!\n"
    if isinstance(message.channel, discord.GroupChannel):
        print(f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Style.RESET_ALL}\nLogging messages in {channel.name}...")
        f = open(f"MessageLogs/MESSAGE HISTORY - {channel.name}.txt", 'w')
        channelname = channel.name
        f.write(
            f"-GC logged with {ver}-\n \nMESSAGE HISTORY - {channelname}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
        )
        endmsg = f"{Fore.GREEN}Finished logging messages in {Style.RESET_ALL}{channelname}!\n"
    if isinstance(message.channel, discord.TextChannel):
        print(f"{Fore.YELLOW}[{datetime.datetime.now()} UTC]{Style.RESET_ALL}\nLogging messages in {channel.name}...")
        f = open(f"MessageLogs/MESSAGE HISTORY - {channel.name}.txt", 'w')
        channelname = channel.name
        f.write(
            f"-Chat logged with {ver}-\n \nMESSAGE HISTORY - {channelname}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
        )
        endmsg = f"{Fore.GREEN}Finished logging messages in {Style.RESET_ALL}{channelname}!\n"
    messages = await channel.history(limit=None, oldest_first=True).flatten()
    for message in messages:
      if len(message.attachments) == 0:
        f.write(f"""
{message.author.name}#{message.author.discriminator} [{message.created_at}] [{message.id}]
{message.system_content}
""")
      if len(message.attachments) > 0:
            f.write(f"""
{message.author.name}#{message.author.discriminator} [{message.created_at}] [{message.id}]
{message.system_content}
   MESSAGE ATTACHMENTS
""")
            for attachment in message.attachments:
                f.write(f"     {attachment.filename}\n     {attachment.url}\n")
    print(endmsg)
    f.close()