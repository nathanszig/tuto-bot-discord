import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

token = "YOUR TOKEN"
bot = commands.Bot(command_prefix="%")

@bot.command()
async def jeux(ctx, *game):
    url = "https://www.instant-gaming.com/fr/rechercher/?query=" + '%20'.join(game)
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    price = parser.find(class_= "price").text
    link = parser.find(class_="cover")
    img = parser.find(class_="picture")
    embed = discord.Embed(title = ' '.join(game), url = link['href']+"?igr=gamer-14a9e7")
    embed.set_thumbnail(url = img['data-src'])
    embed.add_field(name= "Prix", value=price)
    await ctx.send(embed= embed)

bot.run(token)