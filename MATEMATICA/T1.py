from manim import *

class Exercicio37(Scene):
    def construct(self):

        titulo = Text("Exercicio 37 - Bandeira do Brasil", font_size=36)
        self.play(Write(titulo))
        self.wait(1)

        self.play(titulo.animate.to_edge(UP))

        # RETANGULO
        retangulo = Rectangle(
            width=6,
            height=4.2,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.5
        )

        # LOSANGO
        losango = Polygon(
            [0, 1.6, 0],
            [2.5, 0, 0],
            [0, -1.6, 0],
            [-2.5, 0, 0],
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.7
        )

        # CIRCULO
        circulo = Circle(
            radius=0.9,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.8
        )

        bandeira = VGroup(retangulo, losango, circulo)
        bandeira.shift(LEFT * 3)

        self.play(DrawBorderThenFill(retangulo))
        self.play(DrawBorderThenFill(losango))
        self.play(DrawBorderThenFill(circulo))

        self.wait(2)

        # AREA DO RETANGULO
        conta1 = Text(
            "Aret = 2 x 1,40 = 2,8 m²",
            font_size=28
        )

        conta1.to_edge(RIGHT).shift(UP * 2)

        self.play(Write(conta1))
        self.wait(2)

        # DIAGONAIS DO LOSANGO
        conta2 = Text(
            "D = 2 - 0,34 = 1,66 m",
            font_size=28
        )

        conta3 = Text(
            "d = 1,40 - 0,34 = 1,06 m",
            font_size=28
        )

        grupo1 = VGroup(conta2, conta3).arrange(DOWN)

        grupo1.next_to(conta1, DOWN)

        self.play(Write(grupo1))
        self.wait(2)

        # AREA LOSANGO
        conta4 = Text(
            "Alosango = (D x d) / 2",
            font_size=28
        )

        conta5 = Text(
            "Alosango = (1,66 x 1,06) / 2",
            font_size=28
        )

        conta6 = Text(
            "Alosango = 0,8798 m²",
            font_size=28
        )

        grupo2 = VGroup(conta4, conta5, conta6).arrange(DOWN)

        grupo2.next_to(grupo1, DOWN)

        self.play(Write(grupo2))
        self.wait(3)

        # AREA VERDE
        conta7 = Text(
            "Averde = 2,8 - 0,8798",
            font_size=28
        )

        conta8 = Text(
            "Averde = 1,92 m²",
            font_size=28
        )

        grupo3 = VGroup(conta7, conta8).arrange(DOWN)

        grupo3.next_to(grupo2, DOWN)

        self.play(Write(grupo3))
        self.wait(3)

        # LIMPA
        self.play(
            FadeOut(conta1),
            FadeOut(grupo1),
            FadeOut(grupo2),
            FadeOut(grupo3)
        )

        # AREA CIRCULO
        conta9 = Text(
            "Acirculo = pi x r²",
            font_size=28
        )

        conta10 = Text(
            "Acirculo = (22/7) x (0,35)²",
            font_size=28
        )

        conta11 = Text(
            "Acirculo = 0,385 m²",
            font_size=28
        )

        grupo4 = VGroup(conta9, conta10, conta11).arrange(DOWN)

        grupo4.to_edge(RIGHT).shift(UP)

        self.play(Write(grupo4))
        self.wait(3)

        # AREA AMARELA
        conta12 = Text(
            "Aamarela = 0,8798 - 0,385",
            font_size=28
        )

        conta13 = Text(
            "Aamarela = 0,4948 m²",
            font_size=28
        )

        grupo5 = VGroup(conta12, conta13).arrange(DOWN)

        grupo5.next_to(grupo4, DOWN)

        self.play(Write(grupo5))
        self.wait(3)

        # PORCENTAGEM
        conta14 = Text(
            "P = (0,4948 / 2,8) x 100",
            font_size=28
        )

        conta15 = Text(
            "P = 17,67%",
            font_size=28
        )

        resultado = Text(
            "17,67%",
            font_size=34,
            color=YELLOW
        )

        grupo6 = VGroup(conta14, conta15, resultado).arrange(DOWN)

        grupo6.next_to(grupo5, DOWN)

        self.play(Write(grupo6))
        self.wait(5)
