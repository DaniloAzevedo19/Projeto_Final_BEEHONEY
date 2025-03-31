import pygame  # Isso aqui "chama" a biblioteca Pygame, que ajuda a criar jogos

# Classe base para qualquer objeto do jogo (fundo, flores, aranhas...)
class Objeto:  # Aqui a gente CRIA um "molde" chamado Objeto

    def __init__(self, imagem, x, y):  # Esse é o "construtor", tipo um "preparador" do objeto
        #  -  `self`:  Isso é meio mágico, por enquanto vamos aceitar que precisa ter
        #  -  `imagem`:  Onde está o desenho do objeto
        #  -  `x`:  Posição horizontal do objeto na tela
        #  -  `y`:  Posição vertical do objeto na tela

        self.grupo = pygame.sprite.Group()  # Cria um "grupo" pra colocar os "sprites"
        #  -  "Sprite" é tipo a imagem do objeto na tela
        #  -  Grupo ajuda a organizar vários objetos

        self.sprite = pygame.sprite.Sprite(self.grupo)  # Cria o sprite e coloca no grupo
        #  -  `self.sprite`:  É onde a gente GUARDA o sprite do objeto

        self.sprite.image = pygame.image.load(imagem)  # CARREGA a imagem do objeto
        self.sprite.rect = self.sprite.image.get_rect()  # Pega o "retângulo" da imagem (pra saber onde ela tá)
        self.sprite.rect[0] = x  # Coloca o objeto na posição X
        self.sprite.rect[1] = y  # Coloca o objeto na posição Y

        self.quadro = 1  # Começa a animação no primeiro "quadro"
        self.tick = 0  # Começa o "contador" pra animação em zero

    # Desenha o objeto na janela do jogo
    def desenhar(self, janela):  # Função pra DESENHAR o objeto na tela
        #  -  `janela`:  Onde o objeto vai ser desenhado (a tela do jogo)
        self.grupo.draw(janela)  # Desenha o objeto na janela

    # Anima o objeto com base no nome da imagem, tempo de troca e número de quadros
    def animar(self, imagem, tempo, quadros):  # Função pra ANIMAR o objeto
        #  -  `imagem`:  O nome do arquivo da imagem
        #  -  `tempo`:  A velocidade da animação
        #  -  `quadros`:  Quantas imagens tem a animação

        self.tick += 1  # Aumenta o contador de tempo

        if self.tick == tempo:  # Se o tempo de trocar de imagem chegou...
            self.tick = 0  # ...zera o contador
            self.quadro += 1  # ...passa pra próxima imagem

        if self.quadro == quadros:  # Se chegou na última imagem...
            self.quadro = 1  # ...volta pra primeira (faz um loop)

        #  -  Isso junta pedacinhos de texto pra achar o arquivo da imagem
        self.sprite.image = pygame.image.load("arquivos/" + imagem + str(self.quadro) + ".png")


# Classe Abelha, "filha" de Objeto (herda de Objeto)
class Abelha(Objeto):  #  <-  **Herança:** Abelha PEGA COISAS da classe Objeto
    #  -  Abelha TEM TUDO que Objeto tem...
    #  -  ...e pode ter coisas SÓ DELA!

    def __init__(self, imagem, x, y):  # Construtor da classe Abelha
        super().__init__(imagem, x, y)  # CHAMA o construtor da classe Objeto
        #  -  Isso "prepara" as coisas que Abelha HERDOU de Objeto

        # Sons
        pygame.mixer.init()  # Inicia o "tocador" de sons do Pygame
        self.som_pontos = pygame.mixer.Sound("arquivos/sons/score.ogg")  # Carrega o som de ponto
        self.som_aranha = pygame.mixer.Sound("arquivos/sons/bateu.ogg")  # Carrega o som de colisão

        self.vida = 3  # Abelha começa com 3 de vida
        self.pontos = 0  # Abelha começa com 0 pontos

    # Movimenta a abelha com o mouse
    def mover(self, evento):  # Função pra MOVER a abelha
        #  -  `evento`:  Informações do que aconteceu no jogo (ex: mexer o mouse)
        if evento.type == pygame.MOUSEMOTION:  # Se o evento for mexer o mouse...
            #  -  `pygame.mouse.get_pos()`:  PEGA a posição do mouse na tela
            #  -  Ajusta a posição da abelha pra ficar no meio do mouse
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    # Detecta colisão com grupo de sprites
    def colisao(self, grupo, nome):  # Função pra VERIFICAR se a abelha bateu em alguma coisa
        #  -  `grupo`:  Grupo de objetos pra verificar a colisão
        #  -  `nome`:  O nome do objeto (Flor ou Aranha)
        colisao = pygame.sprite.spritecollide(self.sprite, grupo, True)  # Verifica se TEVE colisão
        #  -  `pygame.sprite.spritecollide`:  Função do Pygame pra ver se um objeto bateu em outro
        #  -  O `True` faz o objeto SUMIR depois que bateu

        if nome == "Flor" and colisao:  # Se bateu numa flor...
            self.pontos += 1  # ...ganha ponto
            self.som_pontos.play()  # ...toca o som de ponto
        elif nome == "Aranha" and colisao:  # Se bateu numa aranha...
            self.vida -= 1  # ...perde vida
            self.som_aranha.play()  # ...toca o som de colisão


# Classe para exibir texto na tela
class Texto:  # Classe pra ESCREVER texto na tela

    def __init__(self, tamanho, texto):  # Construtor da classe Texto
        #  -  `tamanho`:  Tamanho da letra
        #  -  `texto`:  O texto que vai aparecer
        self.fonte = pygame.font.SysFont("Arial Bold", tamanho)  # Escolhe a FONTE da letra
        #  -  "Arial Bold":  Nome da fonte
        #  -  `tamanho`:  Tamanho da fonte
        self.render = self.fonte.render(texto, True, (255, 255, 255))  # "Desenha" o texto numa imagem
        #  -  `texto`:  O texto pra desenhar
        #  -  `True`:  Deixa a letra mais bonitinha
        #  -  `(255, 255, 255)`:  Cor do texto (branco)

    def desenhar(self, janela, x, y):  # Função pra MOSTRAR o texto na tela
        #  -  `janela`:  Onde o texto vai aparecer (a tela do jogo)
        #  -  `x`:  Posição horizontal do texto
        #  -  `y`:  Posição vertical do texto
        janela.blit(self.render, (x, y))  # Coloca o texto na tela

    def atualizar_texto(self, novo_texto):  # Função pra MUDAR o texto que está aparecendo
        #  -  `novo_texto`:  O novo texto
        self.render = self.fonte.render(novo_texto, True, (255, 255, 255))  # Desenha o novo texto