import discord
import requests
import pyttsx3
from discord.ext import commands

# Inicializando o bot
intents = discord.Intents.default()
intents.message_content = True  # Para ler mensagens
bot = commands.Bot(command_prefix="!", intents=intents)

dicas_ambiente = [
    "Reduza o uso de plástico descartável.",
    "Recicle sempre que possível.",
    "Economize água e energia.",
    "Plante árvores e cuide do meio ambiente.",
    "Use transporte público ou bicicleta para reduzir a emissão de poluentes."
]

engine = pyttsx3.init()

def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        return response.text.strip()
    return "Erro ao obter dados do tempo."

def get_facts():
    base_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        return response.json().get("text", "Erro ao obter fato.")
    return "Erro ao obter fato."

    
@bot.command()
async def fact(ctx):
    fact = get_facts()
    engine_say = pyttsx3.init()
    engine_say.say(fact)
    engine_say.runAndWait()
    await ctx.send(f"Fato aleatório: {fact}")


@bot.command()
async def weather(ctx, *, city: str):
    weather_info = get_weather(city)
    await ctx.send(f"Previsão do tempo para {city}: {weather_info}")

# Manipulador de comandos !start
@bot.command()
async def start(ctx):
    await ctx.send("Olá! Sou um bot que anuncia a previsão do tempo.")

@bot.command()
async def meio_ambiente(ctx):
    await bot.change_presence(activity=discord.Game(name="🌱 Meio Ambiente"))
    await ctx.send("O bot agora está anunciando sobre o meio ambiente!")

# Inicia o bot
bot.run("MTU1NDk0NzIyNzMwNTI1MDkwMA.GZHZFy.oMkupQ9BJHGmM94SCIM1TwVYpJLTK1C7VNC4y0")