import disnake
from disnake.ext import commands


class UserCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def user(self, inter, member: disnake.Member):
        await inter.response.send_message(f'{inter.guild.id} {inter.author.mention} {inter.author.id} \n{member.id} {member.name} {member.nick} {member.global_name}')


def setup(bot: commands.Bot):
    bot.remove_cog(UserCommand(bot))
