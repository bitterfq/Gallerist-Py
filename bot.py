# bot.py

# bs4 src: https://realpython.com/beautiful-soup-web-scraper-python/#part-1-inspect-your-data-source
# src #2 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find

import os
import webscrapper
import discord 
from datetime import date

#using Bot discord api 
from discord.ext import commands 

# get env variable from the env file 
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# command prefix for bot
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='gallerist', help = 'Sends object of the day at the SAINT LOUIS ART MUSEUM ')
async def gallery(ctx):
    response = webscrapper.scrape()
    embed = discord.Embed(title=response.title + "  |  " + str(date.today()), description=response.metadata,
                          color=0x00ff00)  # creates embed
    file = discord.File(response.title, filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


bot.run(TOKEN)
