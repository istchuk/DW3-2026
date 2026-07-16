from manim import *
import numpy as np

# Cria a cena principal
class HeronVisual(Scene):

    # Método principal da animação
    def construct(self):

        # =====================================================
        # CORES
        # =====================================================

        # Define a cor de fundo da cena
        self.camera.background_color = "#f5f5f5"

        # Variáveis de cores
        AZUL = "#1E3A5F"
        VERDE = "#2E7D32"
        LARANJA = "#D97706"
        VERMELHO = "#C0392B"
        PRETO = "#222222"

        # =====================================================
        # TÍTULO
        # =====================================================

        # Título principal
        titulo = Text(
            "Dedução da Fórmula de Heron",
            font_size=40,
            color=AZUL
        )

        # Subtítulo
        subtitulo = Text(
            "Área de qualquer triângulo",
            font_size=26,
            color=PRETO
        )

        # Agrupa título e subtítulo
        grupo_titulo = VGroup(
            titulo,
            subtitulo
        ).arrange(DOWN)

        # Mostra o título
        self.play(Write(titulo))

        # Mostra o subtítulo
        self.play(FadeIn(subtitulo))

        # Espera 2 segundos
        self.wait(2)

        # Move o grupo para o topo
        self.play(
            grupo_titulo.animate.scale(0.7).to_edge(UP)
        )

        # =====================================================
        # TRIÂNGULO
        # =====================================================

        # Coordenadas dos vértices
        A = np.array([0, 2.2, 0])
        B = np.array([-3, -1.5, 0])
        C = np.array([3, -1.5, 0])

        # Cria os lados do triângulo
        ab = Line(A, B, color=AZUL)
        bc = Line(B, C, color=AZUL)
        ca = Line(C, A, color=AZUL)

        # Cria o polígono do triângulo
        triangulo = Polygon(
            A, B, C,
            color=AZUL,
            fill_opacity=0.15
        )

        # Desenha os lados
        self.play(Create(ab))
        self.play(Create(bc))
        self.play(Create(ca))

        # Preenche o triângulo
        self.play(FadeIn(triangulo))

        # =====================================================
        # ALTURA
        # =====================================================

        # Ponto da altura
        H = np.array([0, -1.5, 0])

        # Linha tracejada da altura
        altura = DashedLine(
            A,
            H,
            color=VERMELHO
        )

        # Mostra a altura
        self.play(Create(altura))

        # =====================================================
        # LABELS
        # =====================================================

        # Nome dos lados do triângulo
        la = Text(
            "a",
            color=PRETO
        ).move_to([0, -2, 0])

        lb = Text(
            "b",
            color=PRETO
        ).move_to([1.8, 0.3, 0])

        lc = Text(
            "c",
            color=PRETO
        ).move_to([-1.8, 0.3, 0])

        # Nome dos segmentos da base
        lx = Text(
            "x",
            color=LARANJA
        ).move_to([-1.5, -1.1, 0])

        lax = Text(
            "a - x",
            color=LARANJA
        ).move_to([1.5, -1.1, 0])

        # Nome da altura
        lh = Text(
            "h",
            color=VERMELHO
        ).move_to([0.3, 0.3, 0])

        # Mostra os lados
        self.play(
            Write(la),
            Write(lb),
            Write(lc)
        )

        # Mostra os segmentos e altura
        self.play(
            Write(lx),
            Write(lax),
            Write(lh)
        )

        # Espera
        self.wait(2)

        # =====================================================
        # MOVE A FIGURA PARA A ESQUERDA
        # =====================================================

        # Agrupa todos os elementos do triângulo
        figura = VGroup(
            triangulo,
            ab,
            bc,
            ca,
            altura,
            la,
            lb,
            lc,
            lx,
            lax,
            lh
        )

        # Move a figura para a esquerda
        self.play(
            figura.animate.scale(0.8).to_edge(LEFT)
        )

        # =====================================================
        # PITÁGORAS
        # =====================================================

        # Novo título da seção
        secao = Text(
            "Aplicando Pitágoras",
            font_size=30,
            color=AZUL
        )

        # Posiciona no topo
        secao.to_edge(UP)

        # Troca o título
        self.play(
            Transform(titulo, secao),
            FadeOut(subtitulo)
        )

        # Equações de Pitágoras
        eq1 = Text(
            "c² = h² + x²",
            font_size=28,
            color=PRETO
        )

        eq2 = Text(
            "h² = c² - x²",
            font_size=28,
            color=VERMELHO
        )

        eq3 = Text(
            "b² = h² + (a - x)²",
            font_size=28,
            color=PRETO
        )

        # Agrupa as equações
        grupo_eq = VGroup(
            eq1,
            eq2,
            eq3
        ).arrange(DOWN, buff=0.5)

        # Move para a direita
        grupo_eq.to_edge(RIGHT)

        # Mostra as equações
        self.play(Write(eq1))
        self.wait(1)

        self.play(Write(eq2))
        self.wait(1)

        self.play(Write(eq3))
        self.wait(2)

        # =====================================================
        # ISOLANDO X
        # =====================================================

        # Remove as equações anteriores
        self.play(FadeOut(grupo_eq))

        # Novo título
        secao2 = Text(
            "Isolando x",
            font_size=30,
            color=AZUL
        )

        secao2.to_edge(UP)

        # Troca o título
        self.play(
            Transform(titulo, secao2)
        )

        # Passos algébricos
        c1 = Text(
            "b² = c² - x² + (a - x)²",
            font_size=26,
            color=AZUL
        )

        c2 = Text(
            "b² = c² + a² - 2ax",
            font_size=26,
            color=AZUL
        )

        c3 = Text(
            "2ax = a² - b² + c²",
            font_size=26,
            color=AZUL
        )

        c4 = Text(
            "x = (a² - b² + c²) / 2a",
            font_size=28,
            color=LARANJA
        )

        # Agrupa os cálculos
        grupo_calc = VGroup(
            c1,
            c2,
            c3,
            c4
        ).arrange(DOWN, buff=0.5)

        # Move para a direita
        grupo_calc.move_to([2.5, 0, 0])

        # Mostra cada cálculo
        for item in grupo_calc:
            self.play(Write(item))
            self.wait(1)

        self.wait(2)

        # =====================================================
        # ÁREA
        # =====================================================

        # Remove cálculos anteriores
        self.play(FadeOut(grupo_calc))

        # Novo título
        secao3 = Text(
            "Calculando a área",
            font_size=30,
            color=AZUL
        )

        secao3.to_edge(UP)

        # Troca o título
        self.play(
            Transform(titulo, secao3)
        )

        # Fórmulas da área
        a1 = Text(
            "A = (a · h) / 2",
            font_size=28,
            color=AZUL
        )

        a2 = Text(
            "A² = (a² · h²) / 4",
            font_size=28,
            color=AZUL
        )

        a3 = Text(
            "A² = [4a²c² - (a² - b² + c²)²] / 16",
            font_size=24,
            color=AZUL
        )

        # Agrupa as fórmulas
        grupo_area = VGroup(
            a1,
            a2,
            a3
        ).arrange(DOWN, buff=0.6)

        # Posiciona na direita
        grupo_area.move_to([2.5, 0, 0])

        # Mostra as fórmulas
        for item in grupo_area:
            self.play(Write(item))
            self.wait(1)

        self.wait(2)

        # =====================================================
        # FÓRMULA FINAL
        # =====================================================

        # Remove elementos anteriores
        self.play(FadeOut(grupo_area))
        self.play(FadeOut(figura))

        # Novo título
        secao4 = Text(
            "Fórmula de Heron",
            font_size=36,
            color=AZUL
        )

        secao4.to_edge(UP)

        # Troca o título
        self.play(
            Transform(titulo, secao4)
        )

        # Fórmula final
        formula = Text(
            "A = √[ p(p-a)(p-b)(p-c) ]",
            font_size=34,
            color=VERDE
        )

        # Caixa ao redor da fórmula
        caixa = SurroundingRectangle(
            formula,
            color=VERDE,
            buff=0.3
        )

        # Semiperímetro
        semi = Text(
            "p = (a + b + c) / 2",
            font_size=28,
            color=LARANJA
        )

        # Posiciona abaixo da fórmula
        semi.next_to(formula, DOWN, buff=0.8)

        # Mostra fórmula
        self.play(Write(formula))

        # Mostra caixa
        self.play(Create(caixa))

        self.wait(1)

        # Mostra semiperímetro
        self.play(Write(semi))

        self.wait(3)

        # =====================================================
        # EXEMPLO
        # =====================================================

        # Remove fórmula anterior
        self.play(
            FadeOut(formula),
            FadeOut(caixa),
            FadeOut(semi)
        )

        # Novo título
        secao5 = Text(
            "Exemplo",
            font_size=36,
            color=AZUL
        )

        secao5.to_edge(UP)

        # Troca o título
        self.play(
            Transform(titulo, secao5)
        )

        # Valores do triângulo
        ex1 = Text(
            "a = 13   b = 14   c = 15",
            font_size=28,
            color=AZUL
        )

        # Cálculo do semiperímetro
        ex2 = Text(
            "p = (13 + 14 + 15) / 2",
            font_size=28,
            color=AZUL
        )

        # Resultado do semiperímetro
        ex3 = Text(
            "p = 21",
            font_size=28,
            color=LARANJA
        )

        # Aplicação na fórmula
        ex4 = Text(
            "A = √[21 · 8 · 7 · 6]",
            font_size=28,
            color=AZUL
        )

        # Resultado final
        ex5 = Text(
            "A = 84",
            font_size=36,
            color=VERDE
        )

        # Agrupa os exemplos
        grupo_ex = VGroup(
            ex1,
            ex2,
            ex3,
            ex4,
            ex5
        ).arrange(DOWN, buff=0.5)

        # Mostra cada linha
        for item in grupo_ex:
            self.play(Write(item))
            self.wait(1)

        # Espera final
        self.wait(4)