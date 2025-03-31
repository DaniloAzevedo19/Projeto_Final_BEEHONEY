import pygame  # Pega a biblioteca Pygame
from menu import Menu, FimDeJogo  # Pega as classes do arquivo menu.py
from game import Jogo  # Pega a classe Jogo do arquivo game.py

# Classe principal que controla o jogo TODO
class Principal:  # Classe pra CONTROLAR o jogo

    def __init__(self):  # Construtor da classe Principal
        pygame.init()  # Inicia o Pygame
        pygame.mixer.init()  # Inicia o "tocador" de sons do Pygame

        # Música de fundo
        pygame.mixer.music.load("arquivos/sons/bg.ogg")  # Carrega a música de fundo
        pygame.mixer.music.play(-1)  # Toca a música de fundo em loop (-1 significa loop infinito)

        # Janela do jogo
        self.janela = pygame.display.set_mode([360, 640])  # Cria a janela do jogo
        #  -  `[360, 640]`:  Tamanho da janela (largura e altura)
        pygame.display.set_caption("Bee Honey")  # Coloca o título na janela

        self.executando = True  # Começa dizendo que o jogo ESTÁ rodando
        self.relogio = pygame.time.Clock()  # Cria um "relógio" pra controlar a velocidade do jogo

        # Telas
        self.tela_inicial = Menu("arquivos/start.png")  # Cria a tela inicial (menu)
        self.jogo = Jogo()  # Cria o jogo
        self.fim_de_jogo = FimDeJogo("arquivos/gameover.png")  # Cria a tela de fim de jogo

    def eventos(self):  # Função pra SABER o que o jogador fez
        for evento in pygame.event.get():  # Pega TUDO que aconteceu no jogo
            #  -  `pygame.event.get()`:  Pega uma lista de eventos do Pygame
            if evento.type == pygame.QUIT:  # Se o jogador FECHOU a janela...
                #  -  `pygame.QUIT`:  É o nome do evento de fechar a janela
                self.executando = False  # ...então o jogo NÃO está mais rodando

            # Transição entre telas conforme eventos
            if not self.tela_inicial.mudar_cena:  # Se NÃO é pra sair da tela inicial...
                #  -  `not`:  Significa "não"
                self.tela_inicial.evento(evento)  # ...a tela inicial CUIDA dos eventos
            elif not self.jogo.mudar_cena:  # Se NÃO é pra sair do jogo...
                self.jogo.abelha.mover(evento)  # ...a abelha SE MOVE no jogo
            else:  # Se é pra ir pra tela de fim de jogo...
                self.fim_de_jogo.evento(evento)  # ...a tela de fim de jogo CUIDA dos eventos

    def desenhar(self):  # Função pra DESENHAR a tela
        if not self.tela_inicial.mudar_cena:  # Se está na tela inicial...
            self.tela_inicial.desenhar(self.janela)  # ...desenha a tela inicial
        elif not self.jogo.mudar_cena:  # Se está no jogo...
            self.jogo.desenhar(self.janela)  # ...desenha o jogo
        else:  # Se está na tela de fim de jogo...
            self.fim_de_jogo.desenhar(self.janela)  # ...desenha a tela de fim de jogo

        pygame.display.update()  # Atualiza a tela do jogo (mostra as coisas novas)

    def atualizar(self):  # Função pra ATUALIZAR as coisas do jogo
        if self.tela_inicial.mudar_cena and not self.jogo.mudar_cena:  # Se é pra sair da tela inicial e NÃO é pra sair do jogo...
            #  -  `and`:  Significa "e"
            self.jogo.atualizar()  # ...atualiza o jogo
        self.relogio.tick(30)  # Controla a velocidade do jogo (30 "frames" por segundo)
        #  -  Isso faz o jogo rodar numa velocidade boa

# Execução principal
if __name__ == "__main__":  # Se este arquivo for o PRIMEIRO a rodar...
    #  -  `__name__`:  É o nome do arquivo atual
    #  -  Quando o arquivo é o primeiro a rodar, `__name__` é igual a "__main__"
    app = Principal()  # Cria uma "instância" da classe Principal (COMEÇA o jogo)
    while app.executando:  # Loop principal do jogo (ENQUANTO o jogo estiver rodando)
        app.eventos()  # Vê os eventos
        app.atualizar()  # Atualiza o jogo
        app.desenhar()  # Desenha a tela