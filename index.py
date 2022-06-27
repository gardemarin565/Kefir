import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = '*')
bot: Bot = commands.Bot(command_prefix = "*", intents = discord.Intents.all())

token = "OTg5ODQ3MjYxNDk0MjYzODU5.GSDItk.3Jed30c_QC3xG6SWfX5xjHd8fbfKpO7x3G5004"

curseWord = ["Хуй"]

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.autor.mention}, маты запрещены")
    else:
        return

@client.command(name="бан", brief="Банит участника", usage="ban <@user> <reason>")
async def ban_(ctx: commands.context.Context, member: discord.Member, *, reason):
    await ctx.guild.ban(user=member, reason=reason)
    message: discord.Message = await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

@client.command(name="мут", brief="Мутит участника", usage="mute <@user> <reason>")
async def ban_(ctx: commands.context.Context, member: discord.Member, *, reason):
    await ctx.guild.mute(user=member, reason=reason)
    message: discord.Message = await ctx.send(f"Пользователь {member.mention} был замьючен по причине {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

 
client.run(token)