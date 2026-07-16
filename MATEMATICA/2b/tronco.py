from manim import *


class TroncoPiramide(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Cores ────────────────────────────────────────────────────────
        TITULO_COR = "#6B0033"
        TEXTO_COR  = "#1a1a1a"
        DEST_COR   = "#B03A2E"
        LABEL_COR  = "#1A5276"
        VERDE      = "#145A32"
        LARANJA    = "#B9770E"
        ROXO       = "#5B2C6F"

        # ── Helpers reutilizáveis ───────────────────────────────────────
        def ST(s, cor=TEXTO_COR, sz=25):
            """Atalho para criar um Text já com cor/tamanho padrão."""
            return Text(s, color=cor, font_size=sz)

        def fade_all():
            """Some com tudo que está em cena no momento."""
            if self.mobjects:
                self.play(*[FadeOut(m) for m in self.mobjects])

        def titulo_secao(texto, tamanho=30):
            """Cria e escreve o título de uma seção, fixo no topo."""
            sec = Text(texto, font_size=tamanho, color=TITULO_COR).to_edge(UP)
            self.play(Write(sec))
            return sec

        def escrever_em_sequencia(itens, espera=0.3):
            for item in itens:
                self.play(Write(item))
                if espera > 0:
                    self.wait(espera)

        def caixa_formula(mobj, cor=DEST_COR, buff=0.16, corner_radius=0.09):
            """Cria e desenha o retângulo de destaque em volta de uma fórmula."""
            box = SurroundingRectangle(mobj, color=cor, buff=buff, corner_radius=corner_radius)
            self.play(Write(mobj), Create(box))
            return box

        def linha_separadora(ref, buff=0.28, direcao=DOWN):
            """Cria uma linha horizontal de separação, posicionada relativa a `ref`."""
            sep = Line(LEFT * 5.5, RIGHT * 5.5, color=TITULO_COR, stroke_width=1)
            sep.next_to(ref, direcao, buff=buff)
            self.play(Create(sep))
            return sep

        # ════════════════════════════════════════════════════════════════
        # CENA 0 – Título
        # ════════════════════════════════════════════════════════════════
        titulo = Text("Volume do Tronco de Pirâmide", font_size=46,
                       color=TITULO_COR, weight=BOLD)
        sub = Text("Dedução completa da fórmula – Matemática 4",
                    font_size=26, color=TEXTO_COR)
        VGroup(titulo, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ════════════════════════════════════════════════════════════════
        # CENA 1 – O que é um tronco de pirâmide
        # ════════════════════════════════════════════════════════════════
        sec1 = titulo_secao("1. O que é um Tronco de Pirâmide", 32)

        # Elevação 2D de uma pirâmide, cortada por um plano paralelo à base
        Vp = np.array([0.0, 2.3, 0])
        A  = np.array([-2.6, -2.0, 0])
        B  = np.array([2.6, -2.0, 0])

        def ponto_em(t, P0, P1):
            # ponto na aresta lateral a uma fração t da altura total (t=0 na base, t=1 no vértice)
            return P0 + t * (P1 - P0)

        t_corte = 0.45  # fração da altura, a partir da base, onde o plano corta
        Al = ponto_em(t_corte, A, Vp)
        Bl = ponto_em(t_corte, B, Vp)

        piramide_pequena = Polygon(Vp, Bl, Al, color=TITULO_COR, stroke_width=2.5)
        piramide_pequena.set_fill(LARANJA, opacity=0.35)

        tronco = Polygon(Al, Bl, B, A, color=TITULO_COR, stroke_width=2.5)
        tronco.set_fill("#AED6F1", opacity=0.45)

        eixo = DashedLine(Vp, (A + B) / 2, color=TEXTO_COR, stroke_width=1.5)

        lV  = Text("V", font_size=26, color=LABEL_COR).next_to(Vp, UP, buff=0.15)
        lA  = Text("A", font_size=24, color=LABEL_COR).next_to(A, DL, buff=0.12)
        lB  = Text("B", font_size=24, color=LABEL_COR).next_to(B, DR, buff=0.12)
        lAl = Text("A'", font_size=22, color=LABEL_COR).next_to(Al, LEFT, buff=0.12)
        lBl = Text("B'", font_size=22, color=LABEL_COR).next_to(Bl, RIGHT, buff=0.12)

        base_maior = Line(A + DOWN * 0.35, B + DOWN * 0.35, color=TEXTO_COR)
        lbl_base_maior = ST("base maior (ABCDEF)", TEXTO_COR, 18).next_to(base_maior, DOWN, buff=0.10)

        base_menor = Line(Al + UP * 0.30, Bl + UP * 0.30, color=TEXTO_COR)
        lbl_base_menor = ST("secção A'B'C'D'E'F' (base menor)", TEXTO_COR, 16).next_to(base_menor, UP, buff=0.08)

        diagrama = VGroup(tronco, piramide_pequena, eixo, lV, lA, lB, lAl, lBl)

        self.play(Create(tronco))
        self.play(Write(lA), Write(lB), Write(lAl), Write(lBl))
        self.wait(0.5)
        self.play(Create(piramide_pequena), Write(lV))
        self.play(Create(eixo))
        self.wait(1)

        texto1 = ST("O plano β, paralelo à base, separa a pirâmide em duas partes:",
                    TEXTO_COR, 22).to_edge(DOWN, buff=1.3)
        texto2 = VGroup(
            ST("• uma pirâmide menor (semelhante à original)", LARANJA, 20),
            ST("• o tronco de pirâmide (a parte que fica com as duas bases)", LABEL_COR, 20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(texto1, DOWN, buff=0.22)

        self.play(Write(texto1))
        escrever_em_sequencia(texto2, espera=0)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 2 – Elementos e semelhança
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec2 = titulo_secao("2. Elementos e Semelhança de Pirâmides", 30)

        # Redesenha o diagrama, agora menor e à esquerda, com cotas
        escala = 0.62
        grupo_fig = VGroup(tronco.copy(), piramide_pequena.copy(), eixo.copy(),
                           lV.copy(), lA.copy(), lB.copy(), lAl.copy(), lBl.copy())
        grupo_fig.scale(escala).to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)

        self.play(FadeIn(grupo_fig))

        legenda = VGroup(
            ST("S_B = área da base maior", TEXTO_COR, 21),
            ST("S_b = área da base menor (secção)", TEXTO_COR, 21),
            ST("h = altura da pirâmide toda (V até a base maior)", TEXTO_COR, 21),
            ST("d = altura da pirâmide menor (V até a secção)", TEXTO_COR, 21),
            ST("k = h − d  →  altura do tronco", DEST_COR, 22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        legenda.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.1)

        escrever_em_sequencia(legenda, espera=0.30)
        self.wait(1)

        sep = Line(LEFT * 5.5, RIGHT * 5.5, color=TITULO_COR,
                   stroke_width=1).to_edge(DOWN, buff=1.2)
        self.play(Create(sep))

        semel = ST("Como as pirâmides são semelhantes, a razão de semelhança d/h vale:",
                   LABEL_COR, 20).next_to(sep, DOWN, buff=0.20)
        self.play(Write(semel))

        razao = ST("S_b / S_B = (d/h)²      e também      A'B'/AB = d/h",
                   TEXTO_COR, 22).next_to(semel, DOWN, buff=0.22)
        self.play(Write(razao))
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 3 – Volume do tronco = diferença de volumes
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec3 = titulo_secao("3. Volume do tronco = pirâmide grande − pirâmide pequena", 27)

        passos3 = VGroup(
            ST("V_tronco = V_(pirâmide VABCDEF) − V_(pirâmide VA'B'C'D'E'F')", TEXTO_COR, 24),
            ST("V_(pirâmide grande) = (1/3) · S_B · h", TEXTO_COR, 24),
            ST("V_(pirâmide pequena) = (1/3) · S_b · d", TEXTO_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        passos3.next_to(sec3, DOWN, buff=0.5)

        escrever_em_sequencia(passos3, espera=0.45)
        self.wait(0.6)

        sep3 = linha_separadora(passos3, buff=0.32)

        formula1 = ST("V_tronco = (1/3) · (S_B · h − S_b · d)      (1)", DEST_COR, 26)
        formula1.next_to(sep3, DOWN, buff=0.3)
        caixa_formula(formula1)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 4 – Isolando d em função de k
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec4 = titulo_secao("4. Encontrando a altura d da pirâmide menor", 30)

        lembrete4 = ST("Da semelhança:   S_b / S_B = (d/h)²   ⇒   d/h = √S_b / √S_B",
                       LABEL_COR, 23)
        lembrete4.next_to(sec4, DOWN, buff=0.4)
        box_l4 = SurroundingRectangle(lembrete4, color=LABEL_COR, buff=0.14, corner_radius=0.08)
        self.play(FadeIn(lembrete4), Create(box_l4))
        self.wait(0.5)

        sep4 = linha_separadora(lembrete4, buff=0.30)

        passos4 = VGroup(
            ST("Como h = d + k, substituímos h por (d + k):", TEXTO_COR, 22),
            ST("d · √S_B = (d + k) · √S_b", TEXTO_COR, 24),
            ST("d · √S_B = d · √S_b + k · √S_b", TEXTO_COR, 24),
            ST("d · (√S_B − √S_b) = k · √S_b", TEXTO_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos4.next_to(sep4, DOWN, buff=0.28)

        escrever_em_sequencia(passos4, espera=0.42)
        self.wait(0.6)

        formula2 = ST("d = k · √S_b / (√S_B − √S_b)      (2)", DEST_COR, 25)
        formula2.next_to(passos4, DOWN, buff=0.32)
        caixa_formula(formula2)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 5 – Encontrando h em função de k
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec5 = titulo_secao("5. Encontrando a altura h da pirâmide maior", 30)

        passos5 = VGroup(
            ST("Da mesma forma, escrevendo d = h − k e substituindo em (2):", TEXTO_COR, 21),
            ST("h − k = k√S_b / (√S_B − √S_b)", TEXTO_COR, 24),
            ST("h = k√S_b / (√S_B − √S_b) + k", TEXTO_COR, 24),
            ST("h = [k√S_b + k√S_B − k√S_b] / (√S_B − √S_b)", TEXTO_COR, 23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos5.next_to(sec5, DOWN, buff=0.45)

        escrever_em_sequencia(passos5, espera=0.42)
        self.wait(0.5)

        formula3 = ST("h = k · √S_B / (√S_B − √S_b)      (3)", DEST_COR, 25)
        formula3.next_to(passos5, DOWN, buff=0.35)
        caixa_formula(formula3)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 6 – Substituindo (2) e (3) em (1)
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec6 = titulo_secao("6. Substituindo (2) e (3) em (1)", 30)

        passos6 = VGroup(
            ST("V_tronco = (1/3) [ S_B · h  −  S_b · d ]", TEXTO_COR, 24),
            ST("V_tronco = (1/3) [ S_B · (k√S_B)/(√S_B−√S_b)  −  S_b · (k√S_b)/(√S_B−√S_b) ]", TEXTO_COR, 20),
            ST("V_tronco = (k/3) · [ (√S_B)³ − (√S_b)³ ] / (√S_B − √S_b)", DEST_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        passos6.next_to(sec6, DOWN, buff=0.5)

        escrever_em_sequencia(passos6, espera=0.5)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 7 – Diferença de cubos
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec7 = titulo_secao("7. Fatorando com a diferença de dois cubos", 28)

        identidade = ST("x³ − y³ = (x − y) · (x² + xy + y²)", LABEL_COR, 26)
        identidade.next_to(sec7, DOWN, buff=0.4)
        box_id = SurroundingRectangle(identidade, color=LABEL_COR, buff=0.16, corner_radius=0.09)
        self.play(Write(identidade), Create(box_id))
        self.wait(0.6)

        aplicando = ST("Com x = √S_B  e  y = √S_b :", TEXTO_COR, 22)
        aplicando.next_to(identidade, DOWN, buff=0.45)
        self.play(Write(aplicando))

        fat = VGroup(
            ST("(√S_B)³ − (√S_b)³  =", TEXTO_COR, 24),
            ST("  [√S_B − √S_b] · [ (√S_B)² + √S_B·√S_b + (√S_b)² ]", TEXTO_COR, 22),
            ST("  =  [√S_B − √S_b] · [ S_B + √(S_B · S_b) + S_b ]", DEST_COR, 23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        fat.next_to(aplicando, DOWN, buff=0.3)

        escrever_em_sequencia(fat, espera=0.45)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 8 – Simplificando: cancela (√S_B − √S_b)
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec8 = titulo_secao("8. Cancelando o fator comum (√S_B − √S_b)", 28)

        passo8a = ST("V_tronco = (k/3) · [ (√S_B − √S_b) · (S_B + √(S_B S_b) + S_b) ] / (√S_B − √S_b)",
                     TEXTO_COR, 21)
        passo8a.next_to(sec8, DOWN, buff=0.5)
        self.play(Write(passo8a))
        self.wait(0.8)

        passo8b = ST("Os fatores (√S_B − √S_b) se cancelam:", LABEL_COR, 22)
        passo8b.next_to(passo8a, DOWN, buff=0.4)
        self.play(Write(passo8b))
        self.wait(1.5)

        formula_final = Text("V_tronco = (k/3) · [ S_B + √(S_B · S_b) + S_b ]",
                              font_size=32, color=VERDE, weight=BOLD)
        formula_final.next_to(passo8b, DOWN, buff=0.45)
        box_final = SurroundingRectangle(formula_final, color=VERDE, buff=0.25, corner_radius=0.12)
        self.play(Write(formula_final), Create(box_final))
        self.wait(2.5)

        legenda_final = ST("k = altura do tronco,  S_B = área da base maior,  S_b = área da base menor",
                           TEXTO_COR, 20)
        legenda_final.next_to(box_final, DOWN, buff=0.35)
        self.play(FadeIn(legenda_final))
        self.wait(2)