from obj import Objeto  # Pega a classe Objeto do arquivo obj.py
import pygame  # Pega a biblioteca Pygame

# Tela de Menu Inicial
class Menu:  # Classe pra TELA INICIAL do jogo

    def __init__(self, imagem):  # Construtor da classe Menu
        #  -  `imagem`:  Onde está o desenho do fundo do menu
        self.fundo = Objeto(imagem, 0, 0)  # Cria um Objeto pra ser o fundo do menu
        #  -  Usa a classe Objeto pra controlar a imagem de fundo
        self.mudar_cena = False  # Começa dizendo que NÃO é pra mudar de tela

    def desenhar(self, janela):  # Função pra DESENHAR o menu na tela
        #  -  `janela`:  Onde o menu vai aparecer (a tela do jogo)
        self.fundo.desenhar(janela)  # Desenha o fundo do menu

    def evento(self, evento):  # Função pra SABER o que o jogador fez no menu
        #  -  `evento`:  O que aconteceu no jogo (ex: apertar uma tecla)
        if evento.type == pygame.KEYDOWN:  # Se o jogador APERTOU uma tecla...
            if evento.key == pygame.K_RETURN:  # ...e a tecla foi o ENTER...
                #  -  `pygame.K_RETURN`:  É o nome da tecla ENTER
                self.mudar_cena = True  # ...então é pra MUDAR de tela (começar o jogo)


# Tela de Fim de Jogo (HERDA de Menu)
class FimDeJogo(Menu):  #  <-  **Herança:** FimDeJogo PEGA COISAS da classe Menu
    #  -  FimDeJogo TEM TUDO que Menu tem...
    #  -  ...e pode ter coisas SÓ DELA (mas nesse caso, não tem nada extra)

    def __init__(self, imagem):  # Construtor da classe FimDeJogo
        super().__init__(imagem)  # CHAMA o construtor da classe Menu
        #  -  Isso "prepara" as coisas que FimDeJogo HERDOU de Menu