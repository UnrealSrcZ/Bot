import discord
from discord.ext import commands
import requests
import json

bot = commands.Bot(command_prefix='?!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def locmyip(ctx, ip_address: str):
    ipapi_url = f"https://ipapi.co/{ip_address}/json/"
    ipapi_response = requests.get(ipapi_url)
    ipapi_data = ipapi_response.json()

    ip_api_url = f"http://ip-api.com/json/{ip_address}"
    ip_api_response = requests.get(ip_api_url)
    ip_api_data = ip_api_response.json()

    embed = discord.Embed(title="IP Geolocation Info", color=0x00ff00)
    embed.add_field(name="IP Address", value=ip_address, inline=False)
    embed.add_field(name="City", value=ipapi_data.get('city'), inline=True)
    embed.add_field(name="Region", value=ipapi_data.get('region'), inline=True)
    embed.add_field(name="Country", value=ipapi_data.get('country_name'), inline=True)
    embed.add_field(name="Latitude", value=ip_api_data.get('lat'), inline=True)
    embed.add_field(name="Longitude", value=ip_api_data.get('lon'), inline=True)
    embed.add_field(name="Time Zone", value=ip_api_data.get('timezone'), inline=True)
    embed.add_field(name="Postal Code", value=ip_api_data.get('zip'), inline=True)
    embed.add_field(name="ISP", value=ipapi_data.get('org'), inline=True)
    embed.add_field(name="ASN", value=ipapi_data.get('asn'), inline=True)
    embed.add_field(name="Country Code", value=ipapi_data.get('country_code'), inline=True)
    embed.add_field(name="Currency", value=ipapi_data.get('currency'), inline=True)
    embed.add_field(name="Languages", value=ipapi_data.get('languages'), inline=True)
    embed.add_field(name="Calling Code", value=ipapi_data.get('country_calling_code'), inline=True)
    embed.add_field(name="Google Maps", value=f"https://maps.google.com/?q={ip_api_data.get('lat')},{ip_api_data.get('lon')}", inline=False)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
