import discord
from discord.ext import commands
import random
import os

#cofiguracion de las intenciones (permisos)
intenciones=discord.Intents.default()
intenciones.message_content=True

#creacion de la instancia del bot
bot=commands.Bot(command_prefix="/", intents=intenciones)

#crear el evento de inicio del boton
@bot.event
async def on_ready():
    print(f"El bot {bot.user} esta en linea")

#creacion de comando para clasificar residuos 
@bot.command()
async def clasificar(ctx, *, objeto:str):
    reciclables=['botella de plastico']
    no_reciclables=['pañal','cascara de platano']

    objeto=objeto.lower()
    if objeto in reciclables:
        await ctx.send(f'El {objeto} es reciclable')
    elif objeto in no_reciclables:
        await ctx.send(f'El {objeto} no es reciclable')
    else:
        await ctx.send(f'No se tiene informacion sobre {objeto}')

#creacion de comando para imagenes de ideas con plastico caseras
@bot.command()
async def ideaPlastico(ctx):
    listaImagenes=os.listdir("imagen")
    imagenEnviar=random.choice(listaImagenes)
    with open(f'imagen/{imagenEnviar}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(content="Aquí tienes algunas imagenes sobre manualidades caseras de plastico elegidas al azar:", file=picture)

#creacion de comando para ver cuando tiempo demora en desintegrarse algunos objetos
@bot.command()
async def TiempoDesc(ctx, *, objeto:str):
    degradables = {
        'papel': '1 año',
        'filtro de cigarro': '10 años',
        'trozo de madera': '2 años',
        'chicle': '5 años',
        'bolsa de plástico': '150 años',
        'toallitas húmedas': '100 años',
        'bastoncillos': '300 años',
        'compresas': '500 años',
        'pañales tradicionales': '450 años',
        'botellas de plástico': '500 años',
        'pilas': '1,000 años',
        'botellas de vidrio': '4,000 años',
        'frutas': '2 semanas',
        'ropa de algodón': '1 año',
        'zapato': '50 años'

    }
    no_degradables = [
        'metal', 'neumáticos', 'cartuchos de tinta', 
        'dispositivos electrónicos', 'plásticos rígidos', 
        'espuma de poliestireno', 'tuberías de PVC', 
        'vidrio templado', 'cerámica', 'pintura seca',
        'aceite usado', 'plomo', 'asbesto', 'cables eléctricos'
    ]
    objeto=objeto.lower()
    if objeto in degradables:
        tiempo = degradables[objeto]
        await ctx.send(f'El {objeto} es degradable y se demora en descomponer aprox {tiempo}.')
    elif objeto in no_degradables:
        await ctx.send(f'El {objeto} no es degradable y no se descompone facilmente')
    else:
        await ctx.send(f'No se tiene informacion sobre {objeto}')

#creacion del comando ayuda
@bot.command()
async def ayuda(ctx):
    await ctx.send("Estos son todos los comandos que puedes usar:/clasificar /ideaPlastico /ayuda /TiempoDesc /objetosnodegrareconocidos /objetosdegrareconocidos")

@bot.command()
async def objetosdegrareconocidos(ctx):
    await ctx.send("papel, filtro de cigarro, trozo de madera, chicle, bolsa de plástico, toallitas húmedas, bastoncillos, compresas, pañales tradicionales, botellas de plástico, pilas, botellas de vidrio, frutas, ropa de algodón, zapato")

@bot.command()
async def objetosnodegrareconocidos(ctx):
    await ctx.send("metal, neumáticos, cartuchos de tinta, dispositivos electrónicos, plásticos rígidos, espuma de poliestireno, tuberías de PVC, vidrio templado, cerámica, pintura seca,aceite usado, plomo, asbesto, cables eléctricos")

bot.run("TU_TOKEN_AQUI")
