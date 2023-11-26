import discord
from discord.ext import commands
from discord_slash import SlashCommand
import base64
from urllib.parse import urlparse, parse_qs

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@slash.slash(name="decodificar", description="Decodifica una cadena en base64.")
async def _decodificar(ctx, enlace):
    try:
        # Parsear el enlace para obtener los parámetros
        parsed_url = urlparse(enlace)
        params = parse_qs(parsed_url.query)

        # Extraer el valor del parámetro 'p' si existe
        base64_str = params.get('p', [''])[0]

        if not base64_str:
            raise ValueError('No se encontró el parámetro "p" en el enlace.')

        # Decodificar el BASE64
        decoded_str = base64.b64decode(base64_str).decode('utf-8')

        # Crear un embed
        embed = discord.Embed(title="Resultado de Decodificación", color=0x00ff00)
        embed.add_field(name="Resultado", value=f"`{decoded_str}`", inline=False)
        embed.set_footer(text="De está forma podras ver el link que oculta linkvalidator de xat.com  \n\n- 'xat external page check'\n\n - 'This page is blocked.'")

        # Enviar el embed
        await ctx.send(embed=embed)
    except Exception as e:
        # En caso de error, enviar un mensaje de error
        await ctx.send(f'Error al decodificar: {str(e)}')








bot.run(' ')  # Reemplaza 'TOKEN' con el token de tu bot
