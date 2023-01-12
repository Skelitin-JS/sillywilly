import discord
import sillywilly

from token_1 import TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

client.user.setActivity('*commands', { type: "STREAMING"})

if __name__ == '__main__':
    
    sillywilly.run_discord_bot()
