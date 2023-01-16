import discord
import sillywilly

from token_1 import TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



if __name__ == '__main__':
    
    sillywilly.run_discord_bot()
