import discord
from discord.ext import commands
import requests

# basic discord bot setup
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print("BOT READY")
  
def get_status_code(url: str, headers=None):
  r = requests.get(url, headers=headers)
  res = None
  if r.status_code == 200:
    res = "Website available"
  elif r.status_code == 404:
    res = "Website or page not found"
  elif r.status_code == 403:
    res = "Forbidden"
  elif r.status_code == 400
    res = "Bad request"
  else:
    res = "An error has occured, check the website for more infos!"
  return res

@bot.command(name="webstatus", aliases=["ws", "status"], description="Show the statuses of websites.")
async def webstatus(ctx, urls=List[str]):
  embed = discord.Embed(title="Websites statuses", description="showing website statuses")
  for list in urls:
    stats = get_status_code(url=list)
    embed.add_field(name=list, value=res)
  await ctx.send(embed=embed)

  bot.run("YOUR TOKEN HERE")
