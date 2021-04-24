# bot.py
import os
import webscrapper
import discord 

from discord.ext import commands 

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='gallerist', help = 'Sends object of the day at the SAINT LOUIS ART MUSEUM ')
async def gallery(ctx):
    response = webscrapper.scrape()
    embed = discord.Embed(title=response.title, description=response.metadata,
                          color=0x00ff00)  # creates embed
    file = discord.File(response.title, filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


bot.run(TOKEN)
