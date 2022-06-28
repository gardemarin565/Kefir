from asyncio import constants
from email import message
import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = '*')
bot: Bot = commands.Bot(command_prefix = "*", intents = discord.Intents.all())

token = "OTg5ODQ3MjYxNDk0MjYzODU5.GiWK9R.lKxR1k9ZB0a7g6G8bTCP43gtifeAUtJ9GXvblU"

curseWord = ['хуй', 'блядь', 'блять', 'хуе', 'пидар', 'пидор', 'ебл', 'Муд']

Пред = 0

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} На этом сервере запрещены маты, не матерись пожалуйста")
        Пред = Пред + 1
    else:
        return

@client.command(name="бан", brief="Банит участника", usage="ban <@user> <reason>")
async def ban_(ctx: commands.context.Context, member: discord.Member, *, reason):
    await ctx.guild.ban(user=member, reason=reason)
    message: discord.Message = await ctx.send(f"Пользователь {member.mention} был забанен по причине: {reason}.")
    await message.add_reaction("<:Ban:989458060638556190>")

@client.command(name = "разбан", brief = "Разбанивает участника", usage = "unban <@user>")
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Участник {user.mention} разбанен')
        else:
            return


@client.command(name = "мьют", brief = "Мьютит участника.", usage = "mute <@user> <reason>")
async def mute_(ctx: commands.context.Context, member: discord.Member, *, reason):
    role = discord.utils.get(ctx.guild.roles, id = 991023285393313853)
    await member.add_roles(role)
    message: discord.Message = await ctx.send(f"Пользователь {member.mention} был замьючен по причине: {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

client.run(token)