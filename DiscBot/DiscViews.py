import discord
from discord import ui
from .EskomSePush import ESP_API_Client

class AreaSelectView(ui.View):
    
    areas: list[discord.SelectOption] = []
    client: ESP_API_Client
    
    def __init__(self, area: list, espclient: ESP_API_Client):
        super().__init__()
        self.client = espclient
        for a in area:
            option = discord.SelectOption(
                label=a['name'],
                value=a['id'],
                )
            self.areas.append(option)

    @discord.ui.select(
        placeholder="Choose an area",
        min_values=1,
        max_values=1,
        options= areas
    )
    async def select_callback(self, interaction, select):
        newUser = {
          'id': interaction.user.id.__str__(),
          'name': interaction.user.name,
          'area': select.values[0],
        }
        added: bool = await self.client.addUser(newUser)
        if added:
            await interaction.response.send_message(f"User added")
        else:
            await interaction.response.send_message(f"User has been already added")