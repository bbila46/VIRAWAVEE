import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def scan(ctx, member: discord.Member):
    await ctx.send(f"🧬 Scanning {member.mention}... No infection detected!")

@bot.command()
async def isolate(ctx, member: discord.Member):
    await ctx.send(f"🔒 {member.mention} has been isolated in the medbay!")

@bot.command()
async def vaccinate(ctx, member: discord.Member):
    role = discord.utils.get(ctx.author.roles, name="Medic")
    if role:
        await ctx.send(f"💉 {member.mention} has been vaccinated!")
    else:
        await ctx.send(f"⛔ {ctx.author.mention}, you need the Medic role to vaccinate.")

@bot.command(name='outbreak_stats')
async def outbreak_stats(ctx):
    await ctx.send("📊 Infected: 5\n💉 Vaccinated: 3")

bot.run(os.getenv("DISCORD_TOKEN"))
