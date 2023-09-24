import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import bot
import random

import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA4NjM4NzMyNzAxMTY1NTcwMA.GaQLiO.Yf72qSMd-1moACtaZ5TFSM0xc9S-UypdFQDYgg'

    intents = discord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix="!", intents=discord.Intents.all() )



    @client.event
    async def on_ready():
        print(f'{client.user} está ativo!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} disse: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s) ")
        except Exception as e:
            print(e)

    @client.tree.command(name="porra", description="Eu não consegui nomear de '/help' então fica esse nome mesmo")
    async def porra(interaction: discord.Interaction):
        await interaction.response.send_message(f"**FALA SEU VIADO DO CARALHO!**\n*Para chamar o bot digite '**goiaba**' e o comando desejado!*\n\nAtualmente os comandos suportados são:\n**1-** Teste de viadagem\n**2-** O cid já deu o butico hoje?\n**3-** Qual é a frase do dia\n\n...Ou é só você digitar `/` e o comando desejado.", ephemeral=True)

    @client.tree.command(name="teste_de_viadagem", description="Vou medir o seu CV (Coeficiente de Viadagem")
    async def testedeviadagem(interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention}, você possui um coeficiente de viadagem de {str(random.randint(0, 100))}%")

    @client.tree.command(name="o_cid_ja_deu_o_butico_hoje", description="Será que o cidão já deu o toba hj no banheirão da USP?")
    async def buticodocid(interaction: discord.Interaction):
        aux = random.randint(1, 5)
        if aux == 1:
            aux2 = 'Ss men o cid da a bunda'
        if aux == 2:
            aux2 = 'Ainda não mas uma hora vai'
        if aux == 3:
            aux2 = 'Ainda não mas uma hora vai'
        if aux == 4:
            aux2 = 'Ainda não mas uma hora vai'
        if aux == 5:
            aux2 = 'Ainda não mas uma hora vai'
        await interaction.response.send_message(aux2)

    @client.tree.command(name="frase_do_dia", description="Vou falar a frase mais inteligente que me vem à cabeça")
    async def frasedodia(interaction: discord.Interaction):
        aux = random.randint(1, 20)
        if aux == 1:
            aux2 = 'lobotomia'
        if aux == 2:
            aux2 = 'metalinguística'
        if aux == 3:
            aux2 = 'Até agora os filósofos ficam preocupados na interpretação do mundo de várias maneiras. O que importa é transformá-lo.'
        if aux == 4:
            aux2 = 'A religião é o ópio do povo'
        if aux == 5:
            aux2 = 'jkcvhljksxchvlkjxzhckhlvkfjhbvkljxchlbkhdflxzkjh vhvvvvvvvvvvvvvvvvvvvvvvvvv ggggggggggggggggbvjcvnbxcmn         bbbbb'
        if aux == 6:
            aux2 = 'Quem acorda cedo cedo madrugo'
        if aux == 7:
            aux2 = 'O movimento proletário é o movimento autônomo da imensa maioria no interesse da imensa maioria'
        if aux == 8:
            aux2 = 'Comunisdo vuvuzelo comuna 1 bilhão zero foda fome mortes'
        if aux == 9:
            aux2 = 'Eu queria que você soubesse que eu adoro o jeito que você sorri.'
        if aux == 10:
            aux2 = 'Ter em si próprio uma confiança exagerada é um excelente treino intelectual.'
        if aux == 11:
            aux2 = 'Não tenho tempo para lembrar de quem me deixou triste, estou mais preocupado com quem me faz feliz.'
        if aux == 12:
            aux2 = 'Você não acha que o capitalismo tá em crise, Cid? Porque eu tava vendo um vídeo da Raluca no TikTok...'
        if aux == 13:
            aux2 = 'Se você perguntar pra mim: ‘Paulo, quantas vezes você se sente motivado no seu dia?’\n– Meia vez.\n‘Quanto da sua vida é motivação?’\n– 3%. O resto, 97% é compromisso, eu tenho que fazer, porque eu tenho que fazer.\nhttps://tenor.com/w8t3.gif'
        if aux == 14:
            aux2 = 'Esses achocolatados (sic) que ficam roubando nossas vagas na Universidade!'
        if aux == 15:
            aux2 = 'Deus não existe e a terra é plana SOMOS ATEUS!'
        if aux == 16:
            aux2 = 'Estou acompanhando tudo e sou totalmente contra essa obra do pão de açúcar'
        if aux == 17:
            aux2 = 'Aqui é a casa da Dona Encrenca onde mora um grupo de olho em tudo.'
        if aux == 18:
            aux2 = 'Perfil oficial do Colégio Salesiano Santa Teresinha'
        if aux == 19:
            aux2 = '史上 最 贱 游戏 trollface quest'
        if aux == 20:
            aux2 = 'A sociedade que coloca a igualdade à frente da liberdade irá terminar sem igualdade e liberdade.'
        await interaction.response.send_message(aux2)

    client.run(TOKEN)

