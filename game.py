from obj import Objeto, Abelha, Texto  # Pega as classes do arquivo obj.py
import random  # Pega o módulo random pra gerar números aleatórios

# Classe principal do jogo
class Jogo:  # Classe pra CONTROLAR o jogo

    def __init__(self):  # Construtor da classe Jogo
        # Fundos animados
        self.fundo1 = Objeto("arquivos/bg.png", 0, 0)  # Cria o primeiro fundo
        self.fundo2 = Objeto("arquivos/bg.png", 0, -640)  # Cria o segundo fundo (em cima do primeiro)
        #  -  Esses fundos vão se mexer pra dar a impressão que a abelha tá voando

        # Obstáculos e recompensas
        self.aranha = Objeto("arquivos/spider1.png", random.randrange(0, 320), -50)  # Cria uma aranha em lugar aleatório
        #  -  `random.randrange(0, 320)`:  Gera um número aleatório entre 0 e 319 (posição da aranha)
        self.flor = Objeto("arquivos/flower1.png", random.randrange(0, 320), 200)  # Cria uma flor em lugar aleatório
        self.abelha = Abelha("arquivos/bee1.png", 150, 600)  # Cria a abelha

        self.mudar_cena = False  # Começa dizendo que NÃO é pra mudar de tela (fim de jogo)

        # Textos
        self.pontuacao = Texto(120, "0")  # Cria o texto pra mostrar a pontuação
        self.vidas = Texto(60, "3")  # Cria o texto pra mostrar a vida

    def desenhar(self, janela):  # Função pra DESENHAR os elementos do jogo na tela
        #  -  `janela`:  Onde os elementos vão aparecer (a tela do jogo)
        self.fundo1.desenhar(janela)  # Desenha o primeiro fundo
        self.fundo2.desenhar(janela)  # Desenha o segundo fundo
        self.abelha.desenhar(janela)  # Desenha a abelha
        self.aranha.desenhar(janela)  # Desenha a aranha
        self.flor.desenhar(janela)  # Desenha a flor
        self.pontuacao.desenhar(janela, 160, 50)  # Desenha a pontuação
        #  -  160 e 50 são as coordenadas (x, y) onde o texto vai aparecer
        self.vidas.desenhar(janela, 50, 50)  # Desenha a vida
        #  -  50 e 50 são as coordenadas (x, y) onde o texto vai aparecer

    def atualizar(self):  # Função pra ATUALIZAR as coisas do jogo (movimento, colisão...)
        self.mover_fundo()  # Move os fundos
        self.aranha.animar("spider", 8, 5)  # Anima a aranha
        self.flor.animar("flower", 8, 3)  # Anima a flor
        self.abelha.animar("bee", 2, 5)  # Anima a abelha
        self.mover_aranha()  # Move a aranha
        self.mover_flor()  # Move a flor
        self.abelha.colisao(self.aranha.grupo, "Aranha")  # Vê se a abelha bateu na aranha
        self.abelha.colisao(self.flor.grupo, "Flor")  # Vê se a abelha bateu na flor
        self.verificar_fim_de_jogo()  # Vê se o jogo acabou
        self.pontuacao.atualizar_texto(str(self.abelha.pontos))  # Atualiza o texto da pontuação
        #  -  `str(self.abelha.pontos)`:  Transforma a pontuação (que é um número) em texto
        self.vidas.atualizar_texto(str(self.abelha.vida))  # Atualiza o texto da vida

    def mover_fundo(self):  # Função pra MOVER os fundos (fazer eles rolarem)
        self.fundo1.sprite.rect[1] += 10  # Move o primeiro fundo pra baixo
        #  -  `+=`:  Soma 10 na posição atual
        self.fundo2.sprite.rect[1] += 10  # Move o segundo fundo pra baixo

        if self.fundo1.sprite.rect[1] > 640:  # Se o primeiro fundo saiu da tela...
            self.fundo1.sprite.rect[1] = 0  # ...volta ele pro topo

        if self.fundo2.sprite.rect[1] > 0:  # Se o segundo fundo está saindo da tela...
            self.fundo2.sprite.rect[1] = -640  # ...coloca ele em cima do primeiro

    def mover_aranha(self):  # Função pra MOVER a aranha
        self.aranha.sprite.rect[1] += 11  # Move a aranha pra baixo

        if self.aranha.sprite.rect[1] > 640:  # Se a aranha saiu da tela...
            self.aranha.sprite.kill()  # ...remove a aranha
            self.aranha = Objeto("arquivos/spider1.png", random.randrange(0, 320), -50)  # ...cria uma aranha nova

    def mover_flor(self):  # Função pra MOVER a flor
        self.flor.sprite.rect[1] += 8  # Move a flor pra baixo

        if self.flor.sprite.rect[1] > 640:  # Se a flor saiu da tela...
            self.flor.sprite.kill()  # ...remove a flor
            self.flor = Objeto("arquivos/flower1.png", random.randrange(0, 320), -100)  # ...cria uma flor nova

    def verificar_fim_de_jogo(self):  # Função pra VERIFICAR se o jogo acabou
        if self.abelha.vida <= 0:  # Se a vida da abelha acabou...
            #  -  `<=`:  Menor ou igual a
            self.mudar_cena = True  # ...então é pra mudar de tela (ir pra tela de fim de jogo)