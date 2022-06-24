import os
from random import randint
from time import sleep
import discord
import meutoken
from discord.ext import commands

token = meutoken.meu_token()
client = commands.Bot(command_prefix='g!')
intents = discord.Intents.default()
intents.members = True

testing = False

client.remove_command('help')

# Bot login

@client.event
async def on_ready():
    print('Conseguimos logar em {0.user}'.format(client))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# roleta
@client.command(name="roleta", help="Sortea um numero de 1 a 10.")
async def roleta(ctx):
    r = randint(1, 10)
    if r == 5:
        await ctx.send('Parabens! você ganhou um chocolate.O numero foi {}'.format(r))
        print('{0.author} ganhou um chololate.'.format(ctx))
    else:
        await ctx.send('Infelizmente você não teve muita sorte e perdeu. O numero foi {}'.format(r))
        print('{0.author} não ganhou o chocolate.'.format(ctx))


# regras
@client.command(name="regras", help="Mostra as regras do servidor")
async def regras(ctx):
    await ctx.send('Regras gerais\n'
                   '1 - Não é permitido desrespeitar os jogadores ou Staff\n'
                   '2 - É estritamente proíbido nicknames e avatares ofensivos e/ou conteúdo sexual explícito no nosso servidor de Discord.\n'
                   '3 - Não é permitido divulgação de outras comunidades de forma direta ou indireta.\n'
                   '4 - Não perturbar os jogadores que usufruem de salas públicas.\n'
                   '5 - Não é permitido o uso de programas para adulterar a voz.\n'
                   '6 - Não é permitido gravar a voz doutros utilizadores sem a permissão dos mesmos ou a permissão da Staff.\n'
                   '7 - As salas de suporte devem ser utilizadas de forma consciente e apenas quando necessárias, caso contrário teremos de punir o jogador que usufrua da mesma de forma incorrecta.\n'
                   '8 - Proíbido Racismo, Xenofobia, Pedófilia e Homofobia no servidor.\n')


@client.command(name="jokenpo", help="Mostra como funciona a brincadeira jokenpo")
async def jokenpo(ctx):
    await ctx.send(
        'O Jokenpô funcionará da seguinte forma vc vai escolher entre Pedra, Papel, Tesoura e eu também, e vamos ver quem ganha. lembre-se sempre de colocar "!" na frente.')


j = randint(0, 2)
itens = 'Pedra', 'Papel', 'Tesoura'


# pedra
@client.command(name="pedra", help="Joga pedra na brincadeira jokenpo.")
async def pedra(ctx):
    await ctx.send('Processando...')
    sleep(2)
    if j == 0:
        await ctx.send('Eu escolhi {}, e deu empate!'.format(itens[j]))
    elif j == 1:
        await ctx.send('Eu escolhi {}, e eu ganhei!'.format(itens[j]))
    elif j == 2:
        await ctx.send('Eu escolhi {}, e você ganhou!'.format(itens[j]))


# papel
@client.command(name="papel", help="Joga papel na brincadeira jokenpo.")
async def papel(ctx):
    await ctx.send('Processando...')
    sleep(2)
    if j == 0:
        await ctx.send('Eu escolhi {}, e você ganhou!'.format(itens[j]))
    elif j == 1:
        await ctx.send('Eu escolhi {}, e deu empate!'.format(itens[j]))
    elif j == 2:
        await ctx.send('Eu escolhi {}, e eu ganhei!'.format(itens[j]))


# tesoura
@client.command(name="tesoura", help="Joga tesoura na brincadeira jokenpo.")
async def tesoura(ctx):
    await ctx.send('Processando...')
    sleep(2)
    if j == 0:
        await ctx.send('Eu escolhi {}, e eu ganhei!'.format(itens[j]))
    elif j == 1:
        await ctx.send('Eu escolhi {}, e você ganhou!'.format(itens[j]))
    elif j == 2:
        await ctx.send('Eu escolhi {}, e deu empate!'.format(itens[j]))


@client.command(name="escreva", help="Escreve o que quiser no chat.")
async def escreva(ctx, arg):
    await ctx.send(arg)


client.run(token)

