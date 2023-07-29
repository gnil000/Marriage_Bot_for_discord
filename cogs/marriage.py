import disnake
from disnake.ext import commands
import database
from datetime import date
from buttons_for_bot import marriageButtons
from table2ascii import table2ascii as t2a, PresetStyle
import source_strings


class MarriageCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def get_all_marriage(self, inter):
        """Получить инфу по всем бракам на сервере"""
        data = database.getAllData(inter.guild.id)
        new_data = []
        for i in range(len(data)):
            guild = self.bot.get_guild(data[i][0])
            first = guild.get_member(int(data[i][1]))
            second = guild.get_member(int(data[i][2]))
            new_data.append([first.name if first.nick is None else first.nick,
                             second.name if second.nick is None else second.nick, (date.today()-data[i][3]).days])
        output = t2a(header=['Супруг 1', 'Супруг 2', 'Дней вместе'],
                     body=new_data, style=PresetStyle.thin_compact)

        await inter.send(f"```\n{output}\n```")

    @commands.slash_command()
    async def get_my_marriage(self, inter):
        """Получить инфу о собственном браке"""
        data = database.getOneData(inter.guild.id, inter.author.id)

        if data is None:
            await inter.send(f'Вы ещё не состоите в браке!')

        embed = disnake.Embed(
            title="Ваш брак",
        )

        embed.set_author(
            name="Meow Bot",
        )
        if (data[1] == 499681922780233739 or data[2] == 499681922780233739):
            embed.set_image(
                file=disnake.File(source_strings.pathToImgForMyMarriage))
            embed.color = 0xFFABFC
        else:
            embed.set_image(
                file=disnake.File(source_strings.pathToImgForOtherMarriage))
            embed.color = 0x612f00

        embed.add_field(name="Дней вместе",
                        value=f"{(date.today()-data[3]).days}", inline=False)
        embed.add_field(name="Дата свадьбы",
                        value=f"{data[3]}", inline=False)

        embed.add_field(name="Первый супруг",
                        value=f"{self.bot.get_user(int(data[1])).name}", inline=True)
        embed.add_field(name="Второй супруг",
                        value=f"{self.bot.get_user(int(data[2])).name}", inline=True)

        await inter.send(embed=embed)

    @commands.slash_command()
    async def marry_me(self, inter, spouse: disnake.Member):
        """Заключить брак"""
        if inter.author == spouse:
            await inter.send('Нельзя жениться на самом себе ;(')
            return
        if database.getOneData(inter.guild.id, spouse.id) is not None:
            await inter.send(f'{spouse.name if spouse.nick is None else spouse.nick} уже состоит в браке!')
            return
        if database.getOneData(inter.guild.id, inter.author.id) is not None:
            await inter.send(f'Вы уже состоите в браке!')
            return

        if (inter.author.voice):
            channel = inter.author.voice.channel
            voice = await channel.connect()
            source = disnake.FFmpegPCMAudio(
                executable='C:/ffmpeg/ffmpeg.exe', source='audio/wedding_song.mp3')
            voice.play(source)

        view = marriageButtons.Confirm(spouse)

        await inter.send(f'{spouse.mention}, согласны ли вы заключить брак с {inter.author.name if inter.author.nick is None else inter.author.nick}?', view=view)
        await view.wait()

        if view.value is None:
            await inter.send(f'{spouse.name if spouse.nick is None else spouse.nick} бежит из под венца. Свадьба не состоялась(')
            if (inter.guild.voice_client is not None):
                await inter.guild.voice_client.disconnect()
            return
        elif view.value is not None:
            if view.value == True:
                x = (inter.guild.id, inter.author.id, spouse.id,
                     date.today())
                database.insertData(x)
            elif view.value == False:
                if (inter.guild.voice_client is not None):
                    await inter.guild.voice_client.disconnect()
                await inter.send(f'Небеса сегодня плачут(')

    @commands.slash_command()
    async def divorce_me(self, inter):
        """Развестись"""
        data = database.getOneData(inter.guild.id, inter.author.id)

        if (data is None):
            await inter.send(f'Вы не состоите ни в каком браке.')
            return
        elif database.deleteData(inter.guild.id, inter.author.id):
            await inter.send(
                f'{self.bot.get_user(data[1]).mention} и {self.bot.get_user(data[2]).mention} больше не вместе.\nОни были в браке {(date.today()-data[3]).days} дней.')
        else:
            await inter.send(
                f'Упс... Кажется что-то пошло не так, сегодня Бог против вашего расставания. Возможно это ещё один шанс всё исправить.')


def setup(bot: commands.Bot):
    bot.add_cog(MarriageCommand(bot))
