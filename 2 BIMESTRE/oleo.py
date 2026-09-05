from manim import *

class ConeOleoAgua(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Cores ────────────────────────────────────────────────────────
        TITULO_COR = "#6B0033"
        TEXTO_COR  = "#1a1a1a"
        DEST_COR   = "#B03A2E"
        LABEL_COR  = "#1A5276"
        VERDE      = "#145A32"
        AGUA_COR   = "#2E86C1"
        OLEO_COR   = "#F1C40F"

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

        def escrever_em_sequencia(itens, espera=0.25):
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

        # Helper: pontos de um cone com vértice para baixo.
        # Vp = vértice (embaixo); topo em Vp + h_vis*UP; raio visual Rw no topo.
        def cone_pontos(Vp, h_vis, Rw, t):
            """Retorna (esquerda, direita) da seção horizontal a uma fração t (0=vértice,1=topo)."""
            y = Vp + t * h_vis * UP
            return y + LEFT * (Rw * t), y + RIGHT * (Rw * t)

        # ════════════════════════════════════════════════════════════════
        # CENA 0 – Título
        # ════════════════════════════════════════════════════════════════
        titulo = Text("Cone com Água e Óleo", font_size=46,
                       color=TITULO_COR, weight=BOLD)
        sub = Text("(EsPCEx – 2012)  —  Geometria Espacial",
                    font_size=26, color=TEXTO_COR)
        VGroup(titulo, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ════════════════════════════════════════════════════════════════
        # CENA 1 – Enunciado e diagrama inicial
        # ════════════════════════════════════════════════════════════════
        sec1 = titulo_secao("1. Enunciado e Situação Inicial", 30)

        enun = VGroup(
            ST("Recipiente cônico (vértice para baixo), raio da base R e altura h,", TEXTO_COR, 20),
            ST("completamente cheio de água (embaixo) e óleo (em cima).", TEXTO_COR, 20),
            ST("A interface entre os líquidos está inicialmente na metade de h.", TEXTO_COR, 20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        enun.next_to(sec1, DOWN, buff=0.30).to_edge(LEFT, buff=0.6)
        escrever_em_sequencia(enun, espera=0)
        self.wait(1)

        # Diagrama: cone vértice para baixo
        Vp = np.array([-3.0, -2.3, 0])
        H_VIS = 4.0
        RW = 1.7

        esq_topo, dir_topo = cone_pontos(Vp, H_VIS, RW, 1.0)
        esq_meio, dir_meio = cone_pontos(Vp, H_VIS, RW, 0.5)

        contorno = Polygon(Vp, dir_topo, esq_topo, color=TEXTO_COR, stroke_width=2.5)

        regiao_agua = Polygon(Vp, dir_meio, esq_meio, color=AGUA_COR, stroke_width=0)
        regiao_agua.set_fill(AGUA_COR, opacity=0.55)

        regiao_oleo = Polygon(esq_meio, dir_meio, dir_topo, esq_topo, color=OLEO_COR, stroke_width=0)
        regiao_oleo.set_fill(OLEO_COR, opacity=0.55)

        linha_interface = Line(esq_meio, dir_meio, color=TEXTO_COR, stroke_width=2)
        eixo = DashedLine(Vp, (esq_topo + dir_topo) / 2, color=TEXTO_COR, stroke_width=1.3)

        lbl_V  = ST("V", LABEL_COR, 20).next_to(Vp, DOWN, buff=0.12)
        lbl_R  = ST("R", LABEL_COR, 20).next_to(dir_topo, RIGHT, buff=0.10)
        lbl_h  = ST("h", LABEL_COR, 20).next_to(eixo, RIGHT, buff=0.65).shift(UP * 1.6)
        lbl_h2 = ST("h/2", LABEL_COR, 18).next_to(eixo, LEFT, buff=0.35).shift(DOWN * 0.55)
        lbl_agua = ST("água", "#FFFFFF", 18).move_to(Vp + UP * 0.55)
        lbl_oleo = ST("óleo", "#5D4E00", 18).move_to((esq_meio + dir_meio + esq_topo + dir_topo) / 4 + UP * 0.1)

        # linha de cota vertical de altura total h (ao lado direito do cone)
        cota_v = DoubleArrow(Vp + RIGHT * 2.4, np.array([Vp[0] + 2.4, Vp[1] + H_VIS, 0]),
                             buff=0, color=LABEL_COR, tip_length=0.14, stroke_width=1.5)

        self.play(Create(contorno))
        self.play(FadeIn(regiao_agua))
        self.play(FadeIn(regiao_oleo))
        self.play(Create(linha_interface))
        self.play(Create(eixo), Create(cota_v))
        self.play(Write(lbl_V), Write(lbl_R), Write(lbl_h), Write(lbl_h2))
        self.play(Write(lbl_agua), Write(lbl_oleo))
        self.wait(2)

        diagrama1 = VGroup(contorno, regiao_agua, regiao_oleo, linha_interface, eixo,
                           lbl_V, lbl_R, lbl_h, lbl_h2, lbl_agua, lbl_oleo, cota_v)

        pergunta = ST("Abrindo a torneira no vértice, a água escoa toda antes do óleo.",
                     DEST_COR, 19).to_edge(DOWN, buff=0.5)
        self.play(Write(pergunta))
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 2 – Volume total e volume de água
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec2 = titulo_secao("2. Volume total e Volume de Água", 30)

        # Reaproveita diagrama, menor, à esquerda
        diagrama2 = diagrama1.copy().scale(0.62).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        self.play(FadeIn(diagrama2))

        passos2 = VGroup(
            ST("Volume total do cone:", LABEL_COR, 22),
            ST("  V = (1/3) π R² h", TEXTO_COR, 23),
            ST("Por semelhança, na altura h/2 o raio da água é R/2:", LABEL_COR, 22),
            ST("  V_água = (1/3) π (R/2)² (h/2)", TEXTO_COR, 23),
            ST("  V_água = (1/3) π R² h / 8  =  V / 8", DEST_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos2.to_edge(RIGHT, buff=0.5).shift(UP * 0.2)

        escrever_em_sequencia(passos2, espera=0.42)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 3 – Volume de óleo
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec3 = titulo_secao("3. Volume de Óleo", 32)

        passos3 = VGroup(
            ST("O óleo ocupa o restante do cone:", TEXTO_COR, 24),
            ST("V_óleo = V − V_água", TEXTO_COR, 25),
            ST("V_óleo = V − V/8", TEXTO_COR, 25),
            ST("V_óleo = (7/8) · V", TEXTO_COR, 25),
            ST("V_óleo = (7/8) · (1/3) π R² h", DEST_COR, 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        passos3.next_to(sec3, DOWN, buff=0.5)

        escrever_em_sequencia(passos3, espera=0.45)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 4 – Depois de escoar toda a água
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec4 = titulo_secao("4. Depois que toda a água escoa", 30)

        explica4 = VGroup(
            ST("A torneira fica no vértice. A água (mais densa) escoa primeiro;", TEXTO_COR, 20),
            ST("o óleo, que não escoou, desce e ocupa o fundo do recipiente,", TEXTO_COR, 20),
            ST("formando um novo cone (de vértice V) com o MESMO volume de óleo.", TEXTO_COR, 20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        explica4.next_to(sec4, DOWN, buff=0.30).to_edge(LEFT, buff=0.6)
        escrever_em_sequencia(explica4, espera=0)
        self.wait(1)

        # Diagrama "depois": cone com óleo só até a altura x
        Vp2 = np.array([2.3, -2.3, 0])
        t_x = 0.75  # ilustrativo (o valor real é ∛7/2 ≈ 0.956, aqui só ilustrativo)
        esq_topo2, dir_topo2 = cone_pontos(Vp2, H_VIS, RW, 1.0)
        esq_x, dir_x = cone_pontos(Vp2, H_VIS, RW, t_x)

        contorno2 = Polygon(Vp2, dir_topo2, esq_topo2, color=TEXTO_COR, stroke_width=2, fill_opacity=0)
        contorno2.set_stroke(opacity=0.5)
        regiao_oleo2 = Polygon(Vp2, dir_x, esq_x, color=OLEO_COR, stroke_width=0)
        regiao_oleo2.set_fill(OLEO_COR, opacity=0.55)
        linha_x = Line(esq_x, dir_x, color=TEXTO_COR, stroke_width=2)
        contorno_topo = Line(esq_topo2, dir_topo2, color=TEXTO_COR, stroke_width=1.5)
        lados = VGroup(Line(Vp2, esq_topo2, color=TEXTO_COR, stroke_width=2),
                       Line(Vp2, dir_topo2, color=TEXTO_COR, stroke_width=2))

        lbl_x = ST("x", DEST_COR, 20).next_to(linha_x, RIGHT, buff=0.55).shift(LEFT * 0.3)
        lbl_r_novo = ST("r", LABEL_COR, 18).move_to((Vp2 + dir_x) / 2 + DOWN * 0.25)
        lbl_oleo2 = ST("óleo", "#5D4E00", 18).move_to(Vp2 + UP * (H_VIS * t_x * 0.5))

        diagrama_dps = VGroup(lados, contorno_topo, regiao_oleo2, linha_x, lbl_x, lbl_oleo2)
        self.play(Create(lados), Create(contorno_topo))
        self.play(FadeIn(regiao_oleo2), Create(linha_x))
        self.play(Write(lbl_x), Write(lbl_oleo2))
        self.wait(1.5)

        equacao4 = ST("V_óleo (novo cone) = V_óleo (original)", DEST_COR, 22)
        equacao4.to_edge(DOWN, buff=0.6)
        self.play(Write(equacao4))
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 5 – Montando e resolvendo a equação
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec5 = titulo_secao("5. Montando a equação para a altura x", 30)

        passos5 = VGroup(
            ST("Por semelhança de triângulos, o raio do novo cone é:", TEXTO_COR, 21),
            ST("  r/x = R/h   ⇒   r = R·x/h", TEXTO_COR, 22),
            ST("Volume do novo cone de óleo:", TEXTO_COR, 21),
            ST("  V_óleo' = (1/3) π r² x = (1/3) π (Rx/h)² x", TEXTO_COR, 22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        passos5.next_to(sec5, DOWN, buff=0.42)

        escrever_em_sequencia(passos5, espera=0.4)
        self.wait(0.6)

        sep5 = linha_separadora(passos5, buff=0.3)

        igualdade = ST("Igualando ao volume original de óleo:", LABEL_COR, 21)
        igualdade.next_to(sep5, DOWN, buff=0.22)
        self.play(Write(igualdade))

        passos5b = VGroup(
            ST("(1/3) π (R²/h²) x³  =  (7/8) · (1/3) π R² h", TEXTO_COR, 23),
            ST("x³ / h²  =  (7/8) h", TEXTO_COR, 23),
            ST("x³  =  (7/8) h³", DEST_COR, 25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos5b.next_to(igualdade, DOWN, buff=0.26)

        escrever_em_sequencia(passos5b, espera=0.45)
        self.wait(2)

        # ════════════════════════════════════════════════════════════════
        # CENA 6 – Resultado final
        # ════════════════════════════════════════════════════════════════
        fade_all()

        sec6 = titulo_secao("6. Isolando x — resultado final", 30)

        passos6 = VGroup(
            ST("x³ = (7/8) h³", TEXTO_COR, 25),
            ST("x = ∛(7/8) · h", TEXTO_COR, 25),
            ST("x = ∛7 / ∛8 · h", TEXTO_COR, 25),
            ST("x = ∛7 / 2 · h     (pois ∛8 = 2)", DEST_COR, 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        passos6.next_to(sec6, DOWN, buff=0.5)

        escrever_em_sequencia(passos6, espera=0.45)
        self.wait(1)

        resultado = Text("x = (∛7 / 2) · h", font_size=40, color=VERDE, weight=BOLD)
        resultado.next_to(passos6, DOWN, buff=0.5)
        box_res = SurroundingRectangle(resultado, color=VERDE, buff=0.25, corner_radius=0.12)
        box_res.move_to(resultado)
        self.play(Write(resultado), Create(box_res))
        self.wait(1.5)

        alternativa = ST("Alternativa (a):  x = (∛7 / 2) h  ✓", DEST_COR, 22)
        alternativa.next_to(box_res, DOWN, buff=0.35)
        self.play(FadeIn(alternativa))
        self.wait(3)