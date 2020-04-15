import discord
import datetime
import colorama
from colorama import Fore, Style
import asyncio
ver = "DiscordUtils 1.4"

async def guildlogcmd(message):
            await message.delete()
            guild = message.guild
            print(f"Logging {guild.name}.")
            f = open(f"GuildLogs/GUILD INFO - {guild.name}.txt", 'w')
            f.write(f"-Info grabbed with {ver}-\n")
            f.write(f"""
GUILD INFO - {guild.name}
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
Member Count - {guild.member_count}
Guild Owner  - {guild.owner}
Guild ID     - {guild.id}
      """)
            f.write(
                "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\nCHANNELS\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
            )
            for channel in message.guild.channels:
                f.write(f"{channel.name} ({channel.id})\n")
            print(
                f"{Fore.GREEN}Finished logging {Style.RESET_ALL}{guild.name}!\n"
            )
            f.close()
          