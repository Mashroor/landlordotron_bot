from discord.flags import Intents
from discord.ext import tasks, commands
from datetime import datetime
from dotenv import load_dotenv
import discord
import os

#Load in env file, set token
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
userIDDictionary = {}

@tasks.loop(hours = 1)
async def monthCheckLoop():
    #find general channel to post to
    genChannel = discord.Client(intents=discord.Intents.all()).get_channel(os.getenv("SERVER_CHANNEL_ID"))
    #Check for first of the month, post msg at Noon (local to bot timezone)
    if (datetime.now().day == 1 and datetime.now().hour == 12):
        await genChannel.send("@here It's a new month, and you know what that means. Pay your fucking rent by using `!payRent`.")
        #Ban everyone in userIDDictionary
        for member in userIDDictionary:
            if userIDDictionary[member.id] == False:
                await member.kick(reason="Tenant behavior")
        #Re-falsify all members
        for member in userIDDictionary:
           userIDDictionary[member.id] = False 
    #2 week reminder, msg at Noon
    #Add formatted list of people who haven't paid
    if (datetime.now().day == 15 and datetime.now().hour == 12):
        await genChannel.send("@everyone ATTENTION ALL RENTOIDS: Rent's due. If you haven't paid, use command `!payRent` to pay your fucking rent.")
              
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    #Initialize Rent dictionary from guild list
    guild = await bot.fetch_guild(os.getenv("SERVER_ID"))
    for member in bot.guilds[0].members:
        userIDDictionary[member.id] = False
    #Start rent check method
    monthCheckLoop.start()

@bot.command(
    help="Politely greets the user",
    brief="Greets the user"
)
async def hello(ctx):
    if ctx.message.author.id == int(os.getenv("SERVER_OWNER_ID")):
        await ctx.message.channel.send("Hello `land-daddy` :)")
    else:
        await ctx.message.channel.send("Fuck off, rentoid")

@bot.command(
    help="Check if you have paid your rent for the month",
    brief="Check rent status"
)
async def rentStatus(ctx):
    if userIDDictionary[ctx.message.author.id]:
        await ctx.message.channel.send("You already paid your rent.")
    else:
        await ctx.message.channel.send("Pay your rent, you dumb fuck.")

@bot.command(
    help="Pay your rent for the month with this command",
    brief="Pays user rent"
)
async def payRent(ctx):
    if userIDDictionary[ctx.message.author.id]:
        await ctx.message.channel.send("You already paid your rent.")
    else:
        await ctx.message.channel.send("Thank you for paying your rent.")
        userIDDictionary[ctx.message.author.id] = True

@bot.command(
    help="Help a small bald man pay his rent mrmL",
    brief="Links to a good ass store"
)
async def domey(ctx):
    await ctx.channel.send("https://moutonmerch.com/")

bot.run(os.getenv("DISCORD_TOKEN"))