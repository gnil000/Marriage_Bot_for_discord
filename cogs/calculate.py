<<<<<<< HEAD
import disnake
from disnake.ext import commands


class CalculateCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def calculate(self, inter, x: int, oper: str, y: int):
        """Калькулятор + - / *"""
        if oper == '+':
            result = x+y
        elif oper == '-':
            result = x-y
        elif oper == '/':
            result = x/y
        elif oper == '*':
            result = x*y
        else:
            result = 'Неверный оператор!'

        await inter.send(str(result))


def setup(bot: commands.Bot):
    bot.add_cog(CalculateCommand(bot))
=======
import disnake
from disnake.ext import commands


class CalculateCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def calculate(self, inter, x: int, oper: str, y: int):
        """Калькулятор + - / *"""
        if oper == '+':
            result = x+y
        elif oper == '-':
            result = x-y
        elif oper == '/':
            result = x/y
        elif oper == '*':
            result = x*y
        else:
            result = 'Неверный оператор!'

        await inter.send(str(result))


def setup(bot: commands.Bot):
    bot.add_cog(CalculateCommand(bot))
>>>>>>> master
