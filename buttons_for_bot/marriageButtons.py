from typing import Optional

import disnake
from disnake.ext import commands


class Confirm(disnake.ui.View):
    def __init__(self, whoPress):
        super().__init__(timeout=10.0)
        self.value = None  # Optional[bool]
        self.whoPress = whoPress

    @disnake.ui.button(label='Да!', style=disnake.ButtonStyle.green, emoji='❤️')
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        if (inter.author != self.whoPress):
            print('нажал не тот пользователь')
            # self.value = False
            # self.stop()
        elif inter.author == self.whoPress:
            await inter.response.send_message('Ура, свадьба состоялась!')
            self.value = True
            self.stop()

    @disnake.ui.button(label='Нет!', style=disnake.ButtonStyle.danger, emoji='💔')
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        if (inter.author != self.whoPress):
            print('нажал не тот пользователь')
            # self.value = False
            # self.stop()
        elif inter.author == self.whoPress:
            # await inter.response.send_message('Небеса сегодня плачут(')
            self.value = False
            self.stop()
