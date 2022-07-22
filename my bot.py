from itertools import starmap
from pickle import STOP
from tracemalloc import start
import discord
from discord.ext import commands




bot = commands.Bot(command_prefix ='!')

@bot.event

async def on_ready():
    print('bot prosnuvsia')


@bot.command( pass_context = True )

async def mood( ctx ):
    await ctx.send('це тобі моє сердечко 💟💟💟 щоб настрій був завжди добрий ')





@bot.command( pass_context = True )

async def дарова( ctx ):
    await ctx.send('хав ду ю ду братан')

#clear message
@bot.command(pass_context = True )
async def clear(ctx, ):
    await ctx.channel.purge(limit=None)


@bot.command( pass_context = True )


async def Путін( ctx ):
    await ctx.send('хуйло')


@bot.command( pass_context = True )

async def слава_Україні( ctx ):
    await ctx.send('героям слава')


@bot.command( pass_context = True )

async def слава_нації( ctx ):
    await ctx.send('смерть ворогам')


@bot.command( pass_context = True )

async def Україна( ctx ):
    await ctx.send('понад усе')







bot.run('OTk4ODUwNTQzNDI4NTc1MjQy.GDfDpw.hb3tUTF2C3AH0L84fs3GtndLhaZ9He_GVPtWWE')