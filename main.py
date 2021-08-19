import pygame
from pygame.locals import *
from sys import exit
import pygame_menu
largura= 1000
altura= 400
Speed= 10
Nave_Speed=7

pygame.init()

def controles():

    #Criação da Janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Imagens/Mapa.jpg')
    background = pygame.transform.scale(background, (largura, altura))

    retangulo=pygame.image.load('Imagens/retangulo.png')
    retangulo=pygame.transform.scale(retangulo,(225//1, 225//4))

    #Texto
    Fonte_Controles = pygame.font.SysFont('arial', 50, True, True)
    Fonte_Texto = pygame.font.SysFont('arial', 20, True, True)
    Fonte_Tecla = pygame.font.SysFont('arial', 20, True, True)

    while True:
        #Imagens
        tela.blit(background, (0, 0))
        tela.blit(retangulo, (300, 35))
        tela.blit(retangulo, (300, 85))
        tela.blit(retangulo, (300, 135))
        tela.blit(retangulo, (300, 185))
        tela.blit(retangulo, (300, 235))
        tela.blit(retangulo, (300, 285))
        tela.blit(retangulo, (300, 335))

        #Texto
        Texto_Controles = Fonte_Controles.render('Controles', True, (255, 255, 255))
        Texto_W = Fonte_Texto.render('Mover Para Cima', True, (255, 255, 255))
        Texto_S = Fonte_Texto.render('Mover Para Baixo', True, (255, 255, 255))
        Texto_A = Fonte_Texto.render('Mover Para Esquerda', True, (255, 255, 255))
        Texto_D = Fonte_Texto.render('Mover Para Direita', True, (255, 255, 255))
        Texto_Pausar = Fonte_Texto.render('Pausar Jogo', True, (255, 255, 255))
        Texto_Sair = Fonte_Texto.render('Sair do Jogo', True, (255, 255, 255))
        Texto_Retornar = Fonte_Texto.render('Retornar', True, (255, 255, 255))
        Tecla_W = Fonte_Texto.render('W', True, (255, 255, 255))
        Tecla_S = Fonte_Texto.render('S', True, (255, 255, 255))
        Tecla_A = Fonte_Texto.render('A', True, (255, 255, 255))
        Tecla_D = Fonte_Texto.render('D', True, (255, 255, 255))
        Tecla_P = Fonte_Texto.render('P', True, (255, 255, 255))
        Tecla_Q = Fonte_Texto.render('Q', True, (255, 255, 255))
        Tecla_BackSpace = Fonte_Texto.render('BackSpace', True, (255, 255, 255))

        tela.blit(Texto_Controles, (largura//2.5, -10))
        tela.blit(Texto_W,(50,50))
        tela.blit(Texto_S, (50, 100))
        tela.blit(Texto_A, (50, 150))
        tela.blit(Texto_D, (50, 200))
        tela.blit(Texto_Pausar, (50, 250))
        tela.blit(Texto_Sair, (50, 300))
        tela.blit(Texto_Retornar, (50, 350))
        tela.blit(Tecla_W, (400, 50))
        tela.blit(Tecla_S, (400, 100))
        tela.blit(Tecla_A, (400, 150))
        tela.blit(Tecla_D, (400, 200))
        tela.blit(Tecla_P, (400, 250))
        tela.blit(Tecla_Q, (400, 300))
        tela.blit(Tecla_BackSpace, (360, 350))

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_BACKSPACE:
                    menu()

        pygame.display.update()

def historia():

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Imagens/Mapa.jpg')
    background = pygame.transform.scale(background, (largura, altura))

    while True:
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    menu()

        pygame.display.update()

def creditos():

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Rota de Fuga')
    background = pygame.image.load('Imagens/Mapa.jpg')
    background = pygame.transform.scale(background, (largura, altura))

    while True:
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    menu()

        pygame.display.update()

def menu():

    tela = pygame.display.set_mode((1000, 400))
    pygame.display.set_caption('Rota de Fuga')
    
    font = pygame_menu.font.FONT_8BIT
    mybackground = pygame_menu.baseimage.BaseImage(image_path='Imagens/Fundo.jpg',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    mytheme = pygame_menu.themes.THEME_DARK.copy()
    mytheme.widget_font=font
    mytheme.background_color=mybackground
    mytheme.title_font_shadow=True
    mytheme.widget_padding=8
    mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
    
    menu = pygame_menu.Menu(title='Rota de Fuga',width=1000,height=400,theme=mytheme)

    menu.add.button('História',historia)
    menu.add.button('Iniciar', game)
    menu.add.button('Controles',controles)
    menu.add.button('Créditos',creditos)
    menu.add.button('Sair', pygame_menu.events.EXIT)
    menu.mainloop(tela)

def game():
    #Criando Nave
    class Nave(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites=[]
            self.sprites.append(pygame.image.load('Imagens/sprite_0.png'))
            self.sprites.append(pygame.image.load('Imagens/sprite_1.png'))
            self.sprites.append(pygame.image.load('Imagens/sprite_2.png'))
            self.atual = 0
            self.image= self.sprites[self.atual]
            self.image=pygame.transform.scale(self.image,(5253//60,2771//60))

            self.rect = self.image.get_rect()
            self.rect.topleft = 50, 160

        def update(self):
            self.atual=self.atual+1
            if self.atual>=len(self.sprites):
                self.atual=0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (5253 // 60, 2771 // 60))


            def move_player(self):
                key=pygame.key.get_pressed()
                if key[pygame.K_w]:
                    self.rect[1] -= Nave_Speed
                if key[pygame.K_s]:
                    self.rect[1] += Nave_Speed
                if key[pygame.K_d]:
                    self.rect[0] += Nave_Speed
                if key[pygame.K_a]:
                    self.rect[0] -= Nave_Speed
            move_player(self)

        def movimento(self):
            if self.rect.x<=0:
                self.rect.x=0
            if self.rect.x>=915:
                self.rect.x=915
            if self.rect.y<=0:
                self.rect.y=0
            if self.rect.y>=355:
                self.rect.y=355

    #Criando Asteroides
    class Obstaculo(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load('Imagens/Asteroide-2.png')
            self.image=pygame.transform.scale(self.image,(232//2,217//2))

            self.rect=self.image.get_rect()
            self.rect.topleft= 1000,0

        def update(self):
            self.rect[0] -= Speed
            if self.rect[0]<-150:
                self.rect.topleft = 1000,0

    class Obstaculo2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load('Imagens/Asteroide-2.png')
            self.image=pygame.transform.scale(self.image,(232//2,217//2))

            self.rect=self.image.get_rect()
            self.rect.topleft= 1200,150

        def update(self):
            self.rect[0] -= Speed
            if self.rect[0]<-150:
                self.rect.topleft = 1200,150

    class Obstaculo3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load('Imagens/Asteroide-2.png')
            self.image=pygame.transform.scale(self.image,(232//2,217//2))

            self.rect=self.image.get_rect()
            self.rect.topleft= 1100,300

        def update(self):
            self.rect[0] -= Speed
            if self.rect[0]<-150:
                self.rect.topleft = 1100,300

    #Criando Moeda
    class Moeda(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('Imagens/Moeda.png')
            self.image = pygame.transform.scale(self.image, (555 // 8, 449 // 8))

            self.rect = self.image.get_rect()
            self.rect.topleft = 1500, 300

        def update(self):
            self.rect[0] -= Speed
            if self.rect[0]<-150:
                self.rect.topleft = 1500,300

    Nave_Sprites= pygame.sprite.Group()
    nave=Nave()
    Nave_Sprites.add(nave)

    Moeda_Sprites=pygame.sprite.Group()
    Moeda_Sprites.add(Moeda())

    Obstaculo_Sprites= pygame.sprite.Group()
    Obstaculo_Sprites.add(Obstaculo())
    Obstaculo_Sprites.add(Obstaculo2())
    Obstaculo_Sprites.add(Obstaculo3())

    #Música de Fundo
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load('Músicas/Snes.mp3')
    pygame.mixer.music.play(-1)

    #Texto
    fonte_pontos=pygame.font.SysFont('arial', 30, True, True)
    fonte_perdeu=pygame.font.SysFont('arial', 50, True, True)
    pontos=0

    #Criando Janela
    tela=pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('Rota de Fuga')
    background= pygame.image.load('Imagens/Mapa.jpg')
    background= pygame.transform.scale(background,(largura,altura))

    clock= pygame.time.Clock()

    def pause():
        paused= True
        while paused:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_p:
                        paused=False

    while True:
        nave.movimento()
        clock.tick(80)
        tela.blit(background, (0, 0))

        mensagem= f'Pontos: {pontos}'
        Mensagem= 'Game Over'
        texto_perdeu= fonte_perdeu.render(Mensagem, True, (0, 0, 0))
        texto_formatado = fonte_pontos.render(mensagem, True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key== K_p:
                    pause()
                if event.key == K_BACKSPACE:
                    pygame.mixer.music.load('Músicas/Snes.mp3')
                    pygame.mixer.pause()
                    menu()
                elif event.key== K_q:
                    pygame.quit()
                    quit()

        tela.blit(texto_formatado, (830, 0))
        colisoes=pygame.sprite.spritecollide(nave,Obstaculo_Sprites,False,pygame.sprite.collide_mask)
        colisoes2=pygame.sprite.spritecollide(nave,Moeda_Sprites,pygame.sprite.collide_rect)
        Nave_Sprites.draw(tela)
        Obstaculo_Sprites.draw(tela)
        Moeda_Sprites.draw(tela)

        if colisoes:
            pass
            pygame.mixer.music.load('Músicas/Snes.mp3')
            pygame.mixer.pause()
            tela.blit(texto_perdeu, (400, 175))
        else:
            Nave_Sprites.update()
            Obstaculo_Sprites.update()
            Moeda_Sprites.update()

        if colisoes2:
            pontos=pontos+1

        pygame.display.update()

menu()
