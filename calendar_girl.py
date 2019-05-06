# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:35:20 2018

@author: Amanda
"""
import datetime
from discord.ext.commands import Bot
from discord.ext import commands


BOT_PREFIX = ("!")
TOKEN = "NDc2MzY5MzI3MzkwNTg4OTI5.DksmTA.YMis-rZ-ax5CFcBp1Wm845S8HEs"

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def today(ctx):
    t = datetime.date.today()
    await ctx.send("Today is " + t.strftime("%m/%d/%Y") + "\nIt is a " + t.strftime("%A")
                       + "\nHave a wonderful day ~")

@client.command()
async def addEvent(ctx, *event, date):
    cal = open("calendar.txt", "a+")
    cal.write(date + " " + event + "\n")
    cal.close()
    await ctx.send("Event added!")





client.run(TOKEN)