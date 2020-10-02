from discord.ext.commands import Bot
from os import environ
from cogs import setup

bot = Bot(environ.get("BOT_PREFIX"))


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.load_extension("jishaku")
setup(bot)

bot.run(environ.get('DISCORD_TOKEN'))
