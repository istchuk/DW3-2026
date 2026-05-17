from manim import *

class Bandeira(Scene):
    def construct(self):

        # =========================================================
        # TÍTULO
        # =========================================================

        # Cria o texto do título
        titulo = Text(
            "Exercicio 37 - Bandeira do Brasil",
            font_size=36
        )

        # Anima a escrita do título
        self.play(Write(titulo))

        # Pausa de 1 segundo
        self.wait(1)

        # Move o título para a parte superior da tela
        self.play(titulo.animate.to_edge(UP))

        # =========================================================
        # RETÂNGULO VERDE
        # =========================================================

        # Cria o retângulo da bandeira
        retangulo = Rectangle(
            width=6,              # largura
            height=4.2,           # altura
            color=GREEN,          # cor da borda
            fill_color=GREEN,     # cor de preenchimento
            fill_opacity=0.5      # transparência
        )

        # =========================================================
        # LOSANGO AMARELO
        # =========================================================

        # Cria o losango usando pontos
        losango = Polygon(
            [0, 1.6, 0],
            [2.5, 0, 0],
            [0, -1.6, 0],
            [-2.5, 0, 0],
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.7
        )

        # =========================================================
        # CÍRCULO AZUL
        # =========================================================

        # Cria o círculo central
        circulo = Circle(
            radius=0.9,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.8
        )

        # =========================================================
        # AGRUPA OS ELEMENTOS DA BANDEIRA
        # =========================================================

        # Junta os três elementos em um grupo
        bandeira = VGroup(retangulo, losango, circulo)

        # Move a bandeira para a esquerda
        bandeira.shift(LEFT * 3)

        # =========================================================
        # ANIMAÇÕES DA BANDEIRA
        # =========================================================

        # Desenha o retângulo
        self.play(DrawBorderThenFill(retangulo))

        # Desenha o losango
        self.play(DrawBorderThenFill(losango))

        # Desenha o círculo
        self.play(DrawBorderThenFill(circulo))

        # Espera 2 segundos
        self.wait(2)

        # =========================================================
        # ÁREA DO RETÂNGULO
        # =========================================================

        # Texto do cálculo da área do retângulo
        conta1 = Text(
            "Aret = 2 x 1,40 = 2,8 m²",
            font_size=28
        )

        # Posiciona o texto à direita e acima
        conta1.to_edge(RIGHT).shift(UP * 2)

        # Mostra o cálculo
        self.play(Write(conta1))

        # Espera
        self.wait(2)

        # =========================================================
        # DIAGONAIS DO LOSANGO
        # =========================================================

        # Diagonal maior
        conta2 = Text(
            "D = 2 - 0,34 = 1,66 m",
            font_size=28
        )

        # Diagonal menor
        conta3 = Text(
            "d = 1,40 - 0,34 = 1,06 m",
            font_size=28
        )

        # Organiza os textos verticalmente
        grupo1 = VGroup(conta2, conta3).arrange(DOWN)

        # Coloca abaixo da conta anterior
        grupo1.next_to(conta1, DOWN)

        # Mostra os textos
        self.play(Write(grupo1))

        # Espera
        self.wait(2)

        # =========================================================
        # ÁREA DO LOSANGO
        # =========================================================

        # Fórmula da área do losango
        conta4 = Text(
            "Alosango = (D x d) / 2",
            font_size=28
        )

        # Substituição dos valores
        conta5 = Text(
            "Alosango = (1,66 x 1,06) / 2",
            font_size=28
        )

        # Resultado da área
        conta6 = Text(
            "Alosango = 0,8798 m²",
            font_size=28
        )

        # Organiza os textos
        grupo2 = VGroup(conta4, conta5, conta6).arrange(DOWN)

        # Posiciona abaixo do grupo anterior
        grupo2.next_to(grupo1, DOWN)

        # Mostra os cálculos
        self.play(Write(grupo2))

        # Espera
        self.wait(3)

        # =========================================================
        # ÁREA VERDE
        # =========================================================

        # Subtração da área do losango
        conta7 = Text(
            "Averde = 2,8 - 0,8798",
            font_size=28
        )

        # Resultado final da área verde
        conta8 = Text(
            "Averde = 1,92 m²",
            font_size=28
        )

        # Organiza os textos
        grupo3 = VGroup(conta7, conta8).arrange(DOWN)

        # Posiciona abaixo
        grupo3.next_to(grupo2, DOWN)

        # Mostra os cálculos
        self.play(Write(grupo3))

        # Espera
        self.wait(3)

        # =========================================================
        # LIMPA OS CÁLCULOS ANTERIORES
        # =========================================================

        self.play(
            FadeOut(conta1),
            FadeOut(grupo1),
            FadeOut(grupo2),
            FadeOut(grupo3)
        )

        # =========================================================
        # ÁREA DO CÍRCULO
        # =========================================================

        # Fórmula da área do círculo
        conta9 = Text(
            "Acirculo = pi x r²",
            font_size=28
        )

        # Substituição dos valores
        conta10 = Text(
            "Acirculo = (22/7) x (0,35)²",
            font_size=28
        )

        # Resultado
        conta11 = Text(
            "Acirculo = 0,385 m²",
            font_size=28
        )

        # Organiza os textos
        grupo4 = VGroup(conta9, conta10, conta11).arrange(DOWN)

        # Posiciona na direita
        grupo4.to_edge(RIGHT).shift(UP)

        # Mostra os cálculos
        self.play(Write(grupo4))

        # Espera
        self.wait(3)

        # =========================================================
        # ÁREA AMARELA
        # =========================================================

        # Subtração da área do círculo
        conta12 = Text(
            "Aamarela = 0,8798 - 0,385",
            font_size=28
        )

        # Resultado final
        conta13 = Text(
            "Aamarela = 0,4948 m²",
            font_size=28
        )

        # Organiza os textos
        grupo5 = VGroup(conta12, conta13).arrange(DOWN)

        # Posiciona abaixo
        grupo5.next_to(grupo4, DOWN)

        # Mostra os cálculos
        self.play(Write(grupo5))

        # Espera
        self.wait(3)

        # =========================================================
        # PORCENTAGEM DA ÁREA AMARELA
        # =========================================================

        # Fórmula da porcentagem
        conta14 = Text(
            "P = (0,4948 / 2,8) x 100",
            font_size=28
        )

        # Resultado da porcentagem
        conta15 = Text(
            "P = 17,67%",
            font_size=28
        )

        # Resultado em destaque
        resultado = Text(
            "17,67%",
            font_size=34,
            color=YELLOW
        )

        # Organiza os textos
        grupo6 = VGroup(conta14, conta15, resultado).arrange(DOWN)

        # Posiciona abaixo
        grupo6.next_to(grupo5, DOWN)

        # Mostra os cálculos
        self.play(Write(grupo6))

        # Espera final
        self.wait(5)