from music import pygame_textinput #importando arquivo para poder fazer o input para o ranking
import pygame as py
import time #importa tempo para regular a velocidade do jogo
import random #importa random para randomizar a queda de objetos no jogo
import math #importa a biblioteca de matematica para o temporizador no jogo
import csv #importa arquivo para guardar o ranking

py.init()#Inicia pygame
display_width = 800 #largura da tela
display_height = 600 #altura da tela
screen = py.display.set_mode((display_width,display_height))#Varíavel para armazenar medidas da tela
py.display.set_caption("Health or Trash!")#Titulo do jogo

#lista de cores
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (200,200,0)
blue = (0,200,200)
purple = (139,0,139)
gray = (128,128,128)
rosa = (255,192,203)
green = (0,200,0)
#cores claras para efeitos de botões
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue= (0,255,255)
bright_rosa= (255,28,174)
bright_yellow = (255,255,0)
bright_purple = (255,0,255)
bright_gray = (192,192,192)
#Medida do balão
bal_height = 80
bal_width = 66

clock = py.time.Clock()#Varíavel para armazenar a função de tempo do pygame e para framerate do jogo
#Desktop - Trabalho - Abrindo em pen drive
agulha = py.image.load('imagens/Agulha.png')#importa imagem da agulha
gordimBlack = py.image.load('imagens/gordimBlack.png')#importa imagem do personagem preto
gordimGreen = py.image.load('imagens/gordimGreen.png')#importa imagem do personagem vermelho
gordimBlue = py.image.load('imagens/gordimBlue.png')#importa imagem do personagem azul
gordimPink = py.image.load('imagens/gordimPink.png')#importa imagem do personagem verde
#fundos de tela
ceuintro = py.image.load('imagens/backgroundMenu.png')#importa imagem para fundo da introdução/menu do jogo
ceuranking = py.image.load('imagens/backgroundbase.png')#importa imagem para fundo da tela para input de nome que é a parte do ranking
ceuinst = py.image.load('imagens/backgroundbase.png')#importa a imagem para fundo de tela de instruções
ceucustomize = py.image.load('imagens/backgroundMenu.png')#importa a imagem para fundo de tela de customização
ceujogo = py.image.load('imagens/backgroundMenu.png')#importa a imagem para fundo de tela de jogo
ceurank2 = py.image.load('imagens/backgroundbase.png')
ceucreditos = py.image.load('imagens/backgroundbase.png')
#sons musicais
dodge = 0 #varíavel para contar quantos objetos desviados
py.mixer.init() #inicia a função para música do jogo
py.mixer.music.load('music/trilha_top_gear.mp3')#carrega a música no jogo
py.mixer.music.play(-1)#coloca para tocar a música indefinidamente

#movimento do gif balão em menus
balcont = 1#varíavel para contar a mudança de frames
balImg = gordimBlack#varíavel para carregar uma imagem padrão de personagem preto
#Input
textinput = pygame_textinput.TextInput()#variavel para texto

def is_on_screen_limit():
    return x >= display_width - bal_width or x <= 0

def ranking():

    texto = csv.reader(open("Bas.csv","r"))
    fhand = []
    for i in texto:
        if len(i) == 0: continue
        fhand.append(i)
    for num in fhand:
        num[0] = int(num[0])

        #print(num)
    fhand.sort(reverse = True)

    ranking = True
    while ranking:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        screen.blit(ceurank2,(0,0))

        largeText = py.font.Font('freesansbold.ttf', 95)
        TextSurf, TextRec = text_objects("Ranking", largeText)
        TextRec.center = ((display_width/2),60)
        screen.blit(TextSurf, TextRec)
        disp = 200
        if len(fhand) < 5:

            for line in range(0,len(fhand) ,1):
                largeText = py.font.Font('freesansbold.ttf', 20)
                TextSurf, TextRec = text_objects(str(fhand[line]), largeText)
                TextRec.center = ((display_width/2),disp)
                screen.blit(TextSurf, TextRec)
                disp += 30
        else:
            for line in range(0,5,1):
                largeText = py.font.Font('freesansbold.ttf', 20)
                TextSurf, TextRec = text_objects(str(fhand[line]), largeText)
                TextRec.center = ((display_width/2),disp)
                screen.blit(TextSurf, TextRec)
                disp += 30

        button("Play",650,500,100,50, green, bright_green, game_loop)
        button("Menu",50,500,100,50,purple,bright_purple,game_intro)
        py.display.flip()


def w_ranking(nome, dodge):#função para escrever pontos
    with open(r'Bas.csv','a') as data:#abre arquivo csv como dados

        writer = csv.writer(data)#define variavel para escrever dados
        writer.writerow([dodge,nome])#escreve variavel com nome do jogador e pontos desviados

def r_ranking():#função para ler o arquivo
  texto = csv.reader(open("Bas.csv","r"))#abre arquivo

def input():#função para chamar a tela onde será colocado o seu nome
    scree = py.display.set_mode((800, 600))#outro display com mesmas proporções
    clock = py.time.Clock()#clock de novo para framerate

    while True:#ciclo para input de nome
        nome = ''#variavel com nome vazio para input
        scree.fill((225, 225, 225))#preenche tela com branco
        screen.blit(ceuranking,(0,0))#carrega imagem de fundo para o ranking

        largeText = py.font.Font('freesansbold.ttf', 60)#variavel para fonte de texto
        TextSurf, TextRec = text_objects("Digite seu nome", largeText)#Duas variaveis sendo definidas pela função text_objects
        TextRec.center = ((display_width/2),(display_height/2))#centraliza o texto
        screen.blit(TextSurf, TextRec)#printa o texto na sua posição
        py.display.flip()#atualiza a tela

        events = py.event.get()#chama evento
        for event in events:#evento de saída do jogo padrão
            if event.type == py.QUIT:
                exit()

        # Atualiza o texto na superficie da tela
        scree.blit(textinput.get_surface(), (10, 10))#input de texto com posição

        if textinput.update(events):#evento chamado para input do nome
            nome = (textinput.get_text())#pega o input do nome
            w_ranking(nome, dodge)#chama função para escrever ranking
            r_ranking()#chama função para ler o ranking

        for event in events:#um laço for para digitar
            if event.type == py.KEYDOWN:#caso uma tecla seja pressionada para escrever o nome
                if event.key == py.K_RETURN:#depois de escrever o nome
                    continue#ranking()#chama a funçao de Ranking
            if event.type == py.KEYUP:#caso uma tecla seja pressionada para escrever o nome
                if event.key == py.K_RETURN:
                    ranking()

        py.display.update()#da update na tela para escrever o nome
        clock.tick(30)#frames da tela de ranking

    #return nome#retorna a variavel nome armazenada para o ranking

def things_dodge(count):#função para mostrar na tela quantas coisas você desviou
    font = py.font.SysFont(None, 25)#tamanho da fonte ao ser usada
    text = font.render("Score: " + str(count), True, black)#texto para ser renderizado com base na variavel count (pontuação), com contorno e de cor preta
    screen.blit(text,(0,0))#renderização do texto na tela

def things(thingx, thingy):#função para renderizar a agulha. Chamamos a agulha de 'thing' no código
    screen.blit(agulha,(thingx,thingy))#renderização da agulha com seu x e y

def bal(x,y):#função para renderizar o balão.
    screen.blit(balImg,(x,y))#renderização do balão com seu x e y

def text_objects(text, font):#Definição importante para texto na tela, recebe texto e fonte
    textSurface = font.render(text, True, white)#variavel para receber variavel texto, com contorno verdadeiro e cor preta
    return textSurface, textSurface.get_rect()#retorna a renderização pelo textSurface no text e sua fonte

def message_display(text):#função de mensagem que recebe texto
    largeText = py.font.Font('freesansbold.ttf', 115)#variavel que define fonte e seu tamanho
    TextSurf, TextRec = text_objects(text, largeText)#duas variaveis usando a função text_objects
    TextRec.center = ((display_width/2),(display_height/2))#posicionando o texto no centro da tela
    screen.blit(TextSurf, TextRec)#renderiza o texto
    py.display.flip()#atualiza a tela

    time.sleep(2)#depois de 2 segundos chama o input de nome para ranking

    nome = input()#chama o input

def crash():#função para mostrar uma mensagem ao chamar a função de mensagem
    message_display("Game Over!")#texto dentro da função de mensagem para ser definido como a variavel text

#função botão que recebe mensagem, posição de mouse(x,y), largura e altura do botão que será um retangulo,ic é caso o mouse não esteja em cima do botão, e uma ação que podera chamar funções
def button(msg, x, y, w, h, ic, ac, action = None):#ic é caso o mouse não esteja em cima do botão,ac é caso o mouse esteja em cima do botão, e uma ação que podera chamar funções
    mouse = py.mouse.get_pos()#variavel mouse para pegar a posição dele
    click = py.mouse.get_pressed()#variavel para pegar o click do mouse

    #se o clique esquerdo estiver entre a posição x do mouse+ largura do botão e a posição x do mouse
    if x+w > mouse[0] > x and y+h > mouse[1] > y:# e o clique direito estiver entre posição y+altura e a posição y

        py.draw.rect(screen, ac,(x,y,w,h))#botão desenhado se o mouse estiver em cima usando a variavel 'ac'.
        #AS VARIAVEIS 'AC' E 'IC' SERVEM PARA MUDAR A COR DO BOTÃO CASO O MOUSE
        if click[0] == 1 and action != None:# e for clicado com o botão esquerdo
            action()#chama a ação que será uma função dentro da variavel botão

#            if action == "Play":
#                game_loop()
#            elif action == "quit":
#                py.quit()
#                quit()
#            print("Ok")
    else:# se o mouse não estiver em cima
        py.draw.rect(screen, ic,(x,y,w,h))#botão desenhado se o mouse não estiver em cima usando a variavel 'ic'

    smallText = py.font.Font("freesansbold.ttf",20)#essas quatro variaveis garantem o texto dentro do botão com um texto base pequeno de tamanho vinte
    textSurf, textRect = text_objects(msg, smallText)#recebe msg que será o texto e sua fonte
    textRect.center = ( (x+(w/2)), (y+(h/2)) )#garante o texto centralizado dentro do botão
    screen.blit(textSurf, textRect)#renderiza o texto

def game_instruction():#função para a pagina instrução
    instruction = True #variavel para loop
    while instruction:#entra em loop
        for event in py.event.get(): #loop para evento
            if event.type == py.QUIT: #condição padrão para caso queiram sair do jogo
                py.quit()
                quit()

        screen.fill(white)#fundo base
        screen.blit(ceuinst,(0,0))#fundo de imagem

        Text = py.font.SysFont('freesansbold.ttf',100)#texto maior
        Stext = py.font.SysFont('freesansbold.ttf',40)#texto menor
        TextSurf, TextRec = text_objects("Instruções",Text)#Texto maior para instruções
        #criação de varias variaveis para pular a linha
        TextSurf1, TextRec1 = text_objects("Use as setas esquerda e direita para desviar" ,Stext)
        TextSurf2, TextRec2 = text_objects("das comidas ruins que vão cair randômicamente",Stext)
        TextSurf3, TextRec3 = text_objects("ao longo do tempo de jogo, e pegar as que são saudaveis.",Stext)
        TextSurf4, TextRec4 = text_objects("A velocidade das comidas aumentam gradativamente,",Stext)
        TextSurf5, TextRec5 = text_objects("cuidado! Quanto mais saudavel for, mais pontos ganha",Stext)
        TextSurf6, TextRec6 = text_objects("Game over se comer muito mal e ficar sem pontos!",Stext)

        #Posição das variaveis
        TextRec.center = ((display_width/2),(display_height/6))#posição do texto 'Instruções' bem em cima da tela (por isso a altura dividida por 6)
        TextRec1.center = ((display_width/2),(display_height/3))#começo dos textos
        TextRec2.center = ((display_width/2),((display_height/3)+30))#aumentar a altura para descer os textos
        TextRec3.center = ((display_width/2),((display_height/3)+60))
        TextRec4.center = ((display_width/2),((display_height/3)+120))
        TextRec5.center = ((display_width/2),((display_height/3)+150))
        TextRec6.center = ((display_width/2),((display_height/3)+200))

        #atualização de todos os textos
        screen.blit(TextSurf, TextRec)
        screen.blit(TextSurf1, TextRec1)
        screen.blit(TextSurf2, TextRec2)
        screen.blit(TextSurf3, TextRec3)
        screen.blit(TextSurf4, TextRec4)
        screen.blit(TextSurf5, TextRec5)
        screen.blit(TextSurf6, TextRec6)


        #função de botões sendo usada
        button("Play",650,500,100,50, green, bright_green, game_loop)#primeiros dois valores são referentes a posição
        button("Back",50,500,100,50,purple,bright_purple,game_intro)#os segundos são o tamanho do botão
        #os ultimos são referentes a 'ic'(sem mouse em cima cor mais escura) e 'ac'(com mouse em cima cor mais clara) e função chamada quando o botão é clicado
        #botões para jogar e voltar na tela de introdução

        py.display.flip()#atualização da tela
        clock.tick(30)#frames da tela

#lista de funções para selecionar a cor do balão
def balblack():#balão preto
    global balImg #variavel global em todas as funções para poder mudar a variavel 'balImg' com a cor desejada
    balImg = gordimBlack
    return balImg #retorna a variavel base de imagem do balão

def balred():#balão vemelho
    global balImg
    balImg = gordimGreen
    return balImg

def balgreen():#balão verde
    global balImg
    balImg = gordimPink
    return balImg

def balblue():#balão azul
    global balImg
    balImg = gordimBlue
    return balImg

def game_customize():#função para a pagina de customização
    customize = True
    while customize:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        screen.blit(ceucustomize,(0,0))

        largeText = py.font.Font('freesansbold.ttf', 100) #fontes para textos com tamanhos diferentes
        mediumText = py.font.Font('freesansbold.ttf',50)

        TextSurf1, TextRec1 = text_objects("Escolha o seu personagem!",mediumText)
        TextRec1.center = ((display_width/2),(display_height/2.5))
        screen.blit(TextSurf1, TextRec1)

        screen.blit(gordimBlack,(115,300))
        screen.blit(gordimGreen,(290,300))
        screen.blit(gordimBlue,(470,300))
        screen.blit(gordimPink,(615,300))
        button("Cor preta",100,400,100,50, gray, bright_gray,balblack)# botões que chamam a função para definir o balão com cor preta,vermelha,azul e verde
        button("Cor verde",250,400,150,50, green, bright_green,balred)#
        button("Cor azul",450,400,100,50, blue, bright_blue,balblue)#
        button("Cor rosa",600,400,100,50, rosa, bright_rosa,balgreen)#
        
        button("Play",650,500,100,50, green, bright_green, game_loop)#botões para jogar e voltar na tela de introdução
        button("Back",50,500,100,50,purple,bright_purple,game_intro)

        py.display.flip()
        clock.tick(30)

def game_creditos():#função para créditos
    creditos = True
    while creditos:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        screen.blit(ceucreditos,(0,0))    
        mediumText = py.font.Font('freesansbold.ttf',25)
        largeText = py.font.Font('freesansbold.ttf', 100)

        TextSurf, TextRec = text_objects("Créditos", largeText)
        TextSurf1, TextRec1 = text_objects("Guilherme Araújo Sette",mediumText)
        TextSurf2, TextRec2 = text_objects("TIA: 41783441",mediumText)
        TextSurf3, TextRec3 = text_objects("Luiz H. Monteiro de Carvalho",mediumText)
        TextSurf4, TextRec4 = text_objects("TIA: 41719468",mediumText)
        TextSurf5, TextRec5 = text_objects("Sarah Beatriz Ferreira",mediumText)
        TextSurf6, TextRec6 = text_objects("TIA: 41732219",mediumText)

        TextRec.center = ((display_width/2),(display_height/6))
        TextRec1.center = ((display_width/2-17),(display_height/3))
        TextRec2.center = ((display_width/2-17),(display_height/3+30))
        TextRec3.center = ((display_width/2-17),(display_height/3+120))
        TextRec4.center = ((display_width/2-17),(display_height/3+150))
        TextRec5.center = ((display_width/2-17),(display_height/3+230))
        TextRec6.center = ((display_width/2-17),(display_height/3+260))

        screen.blit(TextSurf, TextRec)
        screen.blit(TextSurf1, TextRec1)
        screen.blit(TextSurf2, TextRec2)
        screen.blit(TextSurf3, TextRec3)
        screen.blit(TextSurf4, TextRec4)
        screen.blit(TextSurf5, TextRec5)
        screen.blit(TextSurf6, TextRec6)
        
        button("Back",50,500,100,50,purple,bright_purple,game_intro)
        py.display.flip()
        clock.tick(30)

def quitgame():#função para sair do jogo normalmente chamada em botões
    py.quit()
    quit()

def game_intro():#função para o menu de introdução

    balcont = 1#variavel para fazer a animação do gif
    intro = True
    while intro:
        for event in py.event.get():
            #print(event)
            if event.type == py.QUIT:
                py.quit()
                quit()

        screen.fill(white)
        screen.blit(ceuintro,(0,0))

        largeText = py.font.Font('freesansbold.ttf', 95)#fonte do texto
        #TextSurf, TextRec = text_objects("Balloon Survey", largeText)
        #TextRec.center = ((display_width/2),(display_height/4))
        #screen.blit(TextSurf, TextRec)

        button("Play",350,250,100,50, green, bright_green, game_loop)#botões que chamam todas as funções do jogo
        button("Personagens",335,350,150,50,blue,bright_blue,game_customize)
        button("Instructions",325,450,150,50, yellow,bright_yellow,game_instruction)
        button("Quit",350,550,100,50, red, bright_red, quitgame)
        button("Creditos",50,550,125,50,purple,bright_purple,game_creditos)

        py.display.flip()
        clock.tick(30)

def game_loop():#o loop do jogo

    global dodge #deixando a variavel dodge em global para ser usada em outras funções como ranking
    dodge = 0
    x = (display_width * 0.45)# posição inicial do balão
    y = (display_height * 0.85)

    #variaveis
    x_change = 0 #mudança de x do balão
    y_change = 0 #mudança de y do balão
    bal_speed = 0 #velocidade do balão
    thing_startx = random.randrange(0, display_width)#posição x randomicamente, em um raio de 0 e indo até o valor total de largura da tela
    thing_starty = -600 #caindo do começo da tela
    thing_speed = 10 #velocidade da agulha
    thing_width = 15 #largura da agulha
    thing_height = 70 #altura da agulha
    timer = 0# Um timer começando do zero

    segundos = 0
    segundos -=clock.tick()#zerando o clock tick para o timer
    timer = 0
    displaytimer = 0

    gameExit = False #variavel de loop
    while not gameExit: #enquanto verdadeiro = not False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

            if event.type == py.KEYDOWN: #teclas sendo pressionadas
                if event.key == py.K_LEFT: #para a esquerda
                    if x <= 0: #se ele chegar no limite da tela
                        x_change = 0 #para de se mover
                    else:
                        x_change = -8 #se não continua movendo para a esquerda
                elif event.key == py.K_RIGHT:#para a direita
                    if x >= display_width - bal_width:#se chegar no limite da tela
                        x_change = 0#ele para de se mover
                    else:
                        x_change = 8#continua movendo para a direita
                elif event.key == py.K_UP:#para subir
                    if y-bal_height < 0:
                        y_change = 0
                        crash()
                    else:
                        y_change = -1
                        #y é decrescido para o balão subir
                        
                elif event.key == py.K_DOWN:#para descer
                    if y +bal_height > display_height:
                        y_change = 0
                        crash()
                    y_change = 2
                    
            if event.type == py.KEYUP:#caso a tecla seja deixado de ser pressionado
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:#se as teclas de esquerda e direita forem deixadas de ser pressionadas
                    x_change = 0#a posição a ser calculada no eixo x é 0

                elif event.key == py.K_UP or event.key == py.K_DOWN:#se as teclas de cima e baixo forem deixadas de ser pressionadas
                    y_change = 0#a posição a ser calculada no eixo y é 0

        x += x_change#movimento sendo calculado no final depois dos comandos
        y += y_change


        screen.fill((white))
        screen.blit(ceujogo,(0,0))

        things(thing_startx, thing_starty)#chama função para renderizar
        thing_starty += thing_speed #soma a velocidade a cada loop e desvio de agulha

        bal(x,y)# chama função para renderizar
        things_dodge(dodge)# função para renderizar pontuação

        #Incremento de tempo
        segundos = clock.tick()/460.0 # É um numero float. Por isso '.0'
        timer += segundos
        displaytimer = math.trunc(timer)
        
        #Sem chamar uma função para o tempo a renderização é feita dentro do próprio loop de jogo
        fontimer = py.font.SysFont(None,25)#tamanho da fonte do timer
        textimer = fontimer.render("Timer: " + str(displaytimer), True, black)#texto para ser renderizado com base no tempo
        screen.blit(textimer,(700,0))

        if is_on_screen_limit(): #não deixa o balão passar para fora da tela
            x_change = 0#

        if thing_starty > display_height:#caso a agulha chegue no final da tela
            thing_starty = 0 - thing_height#reseta a altura
            thing_startx = random.randrange(0, display_width)#reseta posição da agulha em uma posição randomica diferente
            dodge += 1 #aumenta em 1 a pontuação

        #Nível 2
        if dodge > 10 and dodge<12:#caso desvie de 11 objetos chega no nivel 2
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 2!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)#printa na tela que está no nivel dois
            py.display.flip()

            #time.sleep(1)
            thing_speed = 13 #aumenta a velocidade da agulha
            #E assim por diante
        #Nível 3
        elif dodge > 20 and dodge < 22:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 3!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 16
        #Nível 4
        elif dodge > 30 and dodge < 32:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 4!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 20
            if is_on_screen_limit():# a partir do nivel 4 se encostar nas paredes voce perde
                crash()
        #Nível 5
        elif dodge > 40 and dodge < 42:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 5!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 25
            if is_on_screen_limit():
                crash()
        #Nível 6
        elif dodge > 40 and dodge < 42:
            largeText = py.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRec = text_objects('Nível 6!', largeText)
            TextRec.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRec)
            py.display.flip()
            thing_speed = 35
            if is_on_screen_limit():
                crash()
        if y <= thing_starty + thing_height and thing_starty <= y + bal_height:
            #print("y cross")
#um if para colisão.
#Se o começo de x da agulha for maior que a posição x de movimento do balão + largura do balão
#'E' a posição 'x' de movimento '+' a largura do balão forem maiores que o começo x da agulha
#'Ou' a posição x + a largura do balão maior que o começo da agulha
#'E' a posição x + a largura do balão menor que o começo da agulha + sua largura
#'Ou' a posição x + a largura do balão dividida por 2 maior que o começo da agulha
#'E' a posição x + a largura do balão dividida por 2 menor que o começo da agulha+ sua largura: chama a função de colisão
            if   thing_startx >= x and x + bal_width >= thing_startx or x+bal_width >= thing_startx and x + bal_width <= thing_startx+thing_width or x+(bal_width / 2) >= thing_startx and x+(bal_width / 2) <= thing_startx+thing_width :

                crash()
                dodge = 0#reseta a pontuação
                timer -= clock.tick()#reseta timer
                clock.reset()
                displaytimer -=displaytimer

        py.display.flip()
        clock.tick(100)

game_intro()#chama a introdução/menu para o jogo
game_loop(balImg)
py.quit()#caso o loop acabe sai do jogo
quit()
