import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config = {
    'token': os.getenv('TOKEN_BOT'),  # discordToken.discord_token,
    'prefix': 'meow',
}

bot = commands.Bot(
    command_prefix=config['prefix'], help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work")


bot.load_extensions("cogs")


bot.run(config['token'])
