import random

import discord

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'goiaba teste de viadagem':
        return 'Você possui um coeficiente de viadagem de ' + str(random.randint(0, 100)) + '%'

    if p_message == "goiaba help":
        return '**FALA SEU VIADO DO CARALHO!**\n*Para chamar o bot digite "**goiaba**" e o comando desejado!*\n\nAtualmente os comandos suportados são:\n' \
               '**1-** Teste de viadagem\n**2-** O cid já deu o butico hoje?\n**3-** Qual é a frase do dia'

    if p_message == 'goiaba o cid já deu o butico hoje?':
        aux = random.randint(1, 5)
        if aux == 1:
            return 'Ss men o cid da a bunda'
        if aux == 2:
            return 'Ainda não mas uma hora vai'
        if aux == 3:
            return 'Ainda não mas uma hora vai'
        if aux == 4:
            return 'Ainda não mas uma hora vai'
        if aux == 5:
            return 'Ainda não mas uma hora vai'

    if p_message == 'goiaba qual é a frase do dia':
        aux = random.randint(1, 20)
        if aux == 1:
            return 'lobotomia'
        if aux == 2:
            return 'metalinguística'
        if aux == 3:
            return 'Até agora os filósofos ficam preocupados na interpretação do mundo de várias maneiras. O que importa é transformá-lo.'
        if aux == 4:
            return 'A religião é o ópio do povo'
        if aux == 5:
            return 'jkcvhljksxchvlkjxzhckhlvkfjhbvkljxchlbkhdflxzkjh vhvvvvvvvvvvvvvvvvvvvvvvvvv ggggggggggggggggbvjcvnbxcmn         bbbbb'
        if aux == 6:
            return 'Quem acorda cedo cedo madrugo'
        if aux == 7:
            return 'O movimento proletário é o movimento autônomo da imensa maioria no interesse da imensa maioria'
        if aux == 8:
            return 'Comunisdo vuvuzelo comuna 1 bilhão zero foda fome mortes'
        if aux == 9:
            return 'Eu queria que você soubesse que eu adoro o jeito que você sorri.'
        if aux == 10:
            return 'Ter em si próprio uma confiança exagerada é um excelente treino intelectual.'
        if aux == 11:
            return 'Não tenho tempo para lembrar de quem me deixou triste, estou mais preocupado com quem me faz feliz.'
        if aux == 12:
            return 'Você não acha que o capitalismo tá em crise, Cid? Porque eu tava vendo um vídeo da Raluca no TikTok...'
        if aux == 13:
            return 'Se você perguntar pra mim: ‘Paulo, quantas vezes você se sente motivado no seu dia?’\n– Meia vez.\n‘Quanto da sua vida é motivação?’\n– 3%. O resto, 97% é compromisso, eu tenho que fazer, porque eu tenho que fazer.\nhttps://tenor.com/w8t3.gif'
        if aux == 14:
            return 'Esses achocolatados (sic) que ficam roubando nossas vagas na Universidade!'
        if aux == 15:
            return 'Deus não existe e a terra é plana SOMOS ATEUS!'
        if aux == 16:
            return 'Estou acompanhando tudo e sou totalmente contra essa obra do pão de açúcar'
        if aux == 17:
            return 'Aqui é a casa da Dona Encrenca onde mora um grupo de olho em tudo.'
        if aux == 18:
            return 'Perfil oficial do Colégio Salesiano Santa Teresinha'
        if aux == 19:
            return '史上 最 贱 游戏 trollface quest'
        if aux == 20:
            return 'A sociedade que coloca a igualdade à frente da liberdade irá terminar sem igualdade e liberdade.'
