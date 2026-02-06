from manim import *
import numpy as np


class ClassificationRegressionDemo(Scene):
    def construct(self):
        self.intro()
        self.linear_score()
        self.binary_classification_problem()
        self.sigmoid_with_moving_z()
        self.decision_boundary()
        self.metrics()
        self.large_dataset()
        self.outro()

    # -----------------------------
    # Intro
    # -----------------------------
    def intro(self):
        title = Text("Regresión para Clasificación", font_size=48).to_edge(UP)
        subtitle = Text("Clasificación binaria con regresión logística", font_size=30)
        subtitle.next_to(title, DOWN)

        self.play(FadeIn(title))
        self.play(FadeIn(subtitle))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(subtitle))

    # -----------------------------
    # Paso 1: Score lineal
    # -----------------------------
    def linear_score(self):
        title = Text("Paso 1: Score lineal", font_size=40).to_edge(UP)
        formula = MathTex("z = w^T x + b", font_size=36)
        formula.next_to(title, DOWN)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        labels = axes.get_axis_labels(MathTex("x_1"), MathTex("x_2"))
        line = axes.plot(lambda x: 0.8 * x - 0.5, color=BLUE)

        self.play(FadeIn(title))
        self.play(Write(formula))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(line))
        self.wait(6)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(line),
        )

    # -----------------------------
    # Problema de clasificación binaria
    # -----------------------------
    def binary_classification_problem(self):
        title = Text("Problema de clasificación binaria", font_size=40).to_edge(UP)
        explanation = Text(
            "Queremos separar dos clases usando una frontera lineal", font_size=28
        ).next_to(title, DOWN)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        labels = axes.get_axis_labels(MathTex("x_1"), MathTex("x_2"))

        points = VGroup()
        for _ in range(40):
            x, y = np.random.uniform(-4, 4, 2)
            color = BLUE if y > -x else RED
            points.add(Dot(axes.c2p(x, y), radius=0.06, color=color))

        self.play(FadeIn(title))
        self.play(Write(explanation))
        self.play(Create(axes), FadeIn(labels))
        self.play(FadeIn(points))
        self.wait(8)
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(points),
        )

    # -----------------------------
    # Paso 2: Sigmoide con z animado
    # -----------------------------
    def sigmoid_with_moving_z(self):
        title = Text("Paso 2: Función sigmoide", font_size=40).to_edge(UP)
        formula = MathTex("\\sigma(z) = \\frac{1}{1 + e^{-z}}", font_size=36)
        formula.next_to(title, DOWN)

        axes = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 1, 0.2],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        labels = axes.get_axis_labels(MathTex("z"), MathTex("P(y=1|x)"))
        sigmoid = axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=GREEN)

        z_tracker = ValueTracker(-5)
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    z_tracker.get_value(), 1 / (1 + np.exp(-z_tracker.get_value()))
                ),
                color=RED,
            )
        )

        z_label = always_redraw(
            lambda: MathTex(f"z = {z_tracker.get_value():.2f}", font_size=28).next_to(
                dot, UP
            )
        )

        self.play(FadeIn(title))
        self.play(Write(formula))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(sigmoid))
        self.play(FadeIn(dot), FadeIn(z_label))
        self.play(z_tracker.animate.set_value(5), run_time=10, rate_func=linear)
        self.wait(4)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(sigmoid),
            FadeOut(dot),
            FadeOut(z_label),
        )

    # -----------------------------
    # Paso 3: Frontera de decisión
    # -----------------------------
    def decision_boundary(self):
        title = Text("Paso 3: Regla de decisión", font_size=40).to_edge(UP)
        rule = MathTex("\\sigma(z) > 0.5 \\Rightarrow Clase\ 1", font_size=34)
        rule.next_to(title, DOWN)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        labels = axes.get_axis_labels(MathTex("x_1"), MathTex("x_2"))
        boundary = axes.plot(lambda x: -x, color=YELLOW)

        self.play(FadeIn(title))
        self.play(Write(rule))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(boundary))
        self.wait(8)
        self.play(
            FadeOut(title),
            FadeOut(rule),
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(boundary),
        )

    # -----------------------------
    # Métricas
    # -----------------------------
    def metrics(self):
        title = Text("Evaluación del modelo", font_size=40).to_edge(UP)
        metrics = (
            VGroup(
                Text("Accuracy: proporción de aciertos", font_size=28),
                Text("Precision: calidad de positivos", font_size=28),
                Text("Recall: cobertura de positivos", font_size=28),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .shift(DOWN * 0.5)
        )

        self.play(FadeIn(title))
        self.play(FadeIn(metrics))
        self.wait(10)
        self.play(FadeOut(title), FadeOut(metrics))

    # -----------------------------
    # Dataset grande
    # -----------------------------
    def large_dataset(self):
        title = Text("Escalamiento a datasets grandes", font_size=40).to_edge(UP)
        explanation = Text(
            "El mismo modelo separa miles de observaciones", font_size=28
        ).next_to(title, DOWN)

        axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[-4, 4, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False},
        ).shift(DOWN * 0.5)

        boundary = axes.plot(lambda x: -x, color=YELLOW)

        points = VGroup()
        for _ in range(500):
            x, y = np.random.uniform(-4, 4, 2)
            color = BLUE if y > -x else RED
            points.add(Dot(axes.c2p(x, y), radius=0.025, color=color))

        self.play(FadeIn(title))
        self.play(Write(explanation))
        self.play(Create(axes))
        self.play(Create(boundary))
        self.play(FadeIn(points, lag_ratio=0.01))
        self.wait(10)
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(axes),
            FadeOut(boundary),
            FadeOut(points),
        )

    # -----------------------------
    # Outro
    # -----------------------------
    def outro(self):
        text = Text(
            "La regresión logística usa una regresión lineal\npara resolver problemas de clasificación",
            font_size=34,
            line_spacing=1.2,
        )
        self.play(FadeIn(text))
        self.wait(6)
        self.play(FadeOut(text))
