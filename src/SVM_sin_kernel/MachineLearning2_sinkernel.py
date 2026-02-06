from manim import *
from matplotlib.pyplot import axes
import numpy as np

class MachineLearning2(Scene):
    def construct(self):

        # ------------- Escena 1 (Hard SVMs) -------------

        # Crear Sistema Coordenado
        axes = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_tip": True}
        ).add_coordinates()

        # Definir Puntos de Datos Rojos y Azules
        points_a = [
            [-2, 1, 0], [-1.5, 2, 0], [-1, 0.5, 0], [-2, -1, 0]
        ]
        points_b = [
            [1, -1, 0], [2, -2, 0], [1.5, 0.5, 0], [0.5, -1.5, 0]
        ]

        dots_a = VGroup(*[Dot(point=p, color=RED) for p in points_a])
        dots_b = VGroup(*[Dot(point=p, color=BLUE) for p in points_b])

        # Definir la Línea de Decisión
        line = Line(
            start=axes.c2p(-2.5, -2.5), 
            end=axes.c2p(2.5, 2.5), 
            color=YELLOW
        )
        line_label = MathTex("w \cdot x + b = 0").next_to(line, UR, buff=0.1)

        # Mostrar Ejes
        self.play(Create(axes))
        self.wait(0.5)
        
        # Mostrar puntos de datos
        self.play(FadeIn(dots_a), FadeIn(dots_b))
        self.play(dots_a.animate.set_glow(0.5), dots_b.animate.set_glow(0.5))
        self.wait(1.5)

        # Mostrar línea de decisión
        self.play(Create(line))
        self.play(Write(line_label))
        self.wait(2)
    
        # Funcion para resaltar puntos
        def create_glowing_dot(point, color=RED):
            dot = Dot(point=point, color=color, radius=0.08)
            
            glow = Dot(
                point=point, 
                color=color, 
                radius=0.2, 
                fill_opacity=0.3,
                stroke_width=0
            )
            
            return VGroup(glow, dot)

        # Resaltar puntos de cada clase
        dots_a_glow = VGroup(*[create_glowing_dot(p, RED) for p in points_a])

        self.play(FadeIn(dots_a_glow))

        dots_b_glow = VGroup(*[create_glowing_dot(p, BLUE) for p in points_b])

        self.play(FadeOut(dots_a_glow))
        self.play(FadeIn(dots_b_glow))
        self.play(FadeOut(dots_b_glow))
        self.wait(1)

        # Definir margenes
        margin_plus = DashedLine(
            start=axes.c2p(-3.0, -2.0), 
            end=axes.c2p(2.0, 3.0), 
            color=WHITE,
            dash_length=0.2
        ).set_opacity(0.5)

        margin_minus = DashedLine(
            start=axes.c2p(-2.0, -3.0), 
            end=axes.c2p(3.0, 2.0), 
            color=WHITE,
            dash_length=0.2
        ).set_opacity(0.5)

        # Definir ecuaciones de los margenes
        label_plus = MathTex("w \cdot x + b = 1", font_size=30)
        label_plus.next_to(margin_plus, UR, buff=0.1).set_color(RED)

        label_minus = MathTex("w \cdot x + b = -1", font_size=30)
        label_minus.next_to(margin_minus, UR, buff=0.1).set_color(BLUE)

        # Mostrar los margenes y sus ecuaciones
        self.play(Create(margin_plus), Create(margin_minus))
        self.play(Write(label_plus), Write(label_minus))
        self.wait(4)

        self.play(FadeOut(line), FadeOut(line_label))

        # Crear el brace para la distancia entre margenes
        brace = BraceBetweenPoints(
            axes.c2p(-np.sqrt(1)/2, np.sqrt(1)/2),
            axes.c2p(np.sqrt(1)/2, -np.sqrt(1)/2),
            buff=0.1
        )

        # Agregar "2d"
        brace_label = brace.get_tex("2d")

        self.play(Create(brace), Write(brace_label))
        self.wait(3)
        self.play(Unwrite(brace_label))

        # Agregar "2/w"
        brace_label = brace.get_tex(r"\frac{2}{\|w\|}")

        self.play(Write(brace_label))
        self.wait(2.5)

        # ------------- Escena 2 (Primal Formulation) -------------

        # Limpiar Escena
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # Mostrar Primal Formulation
        primal_obj = MathTex(
            r"\text{Primal Formulation: } \min_{w, b} \frac{1}{2} \|w\|^2",
            font_size=42
        )

        # Mostrar la Condición
        condition = MathTex(
            r"\text{subject to: } y_i(w \cdot x_i + b) \ge 1, \quad \forall i",
            font_size=36
        )

        primal_obj.to_edge(UP, buff=1.5)
        condition.next_to(primal_obj, DOWN, buff=1)

        # Animacion
        self.play(Write(primal_obj))
        self.wait(1)        
        self.play(FadeIn(condition, shift=UP))
        self.wait(2.5)

        # ------------- Escena 3 (Dual Formulation) -------------

        # Limpiar Escena
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # Mostrar Dual Formulation
        dual_obj = MathTex(
            r"\text{Dual Formulation: } \max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i,j=1}^n y_i y_j \alpha_i \alpha_j \space", # Index 0
            r"(x_i \cdot x_j)", # Index 1
            font_size=42
        )

        # Mostrar la Condición
        condition = MathTex(
            r"\text{subject to: } \alpha_i \ge 0, \quad \forall i",
            font_size=36
        )

        dual_obj.to_edge(UP, buff=1.5)
        condition.next_to(dual_obj, DOWN, buff=1)

        # Animacion
        self.play(Write(dual_obj))
        self.wait(1.5)  
        self.play(FadeIn(condition, shift=UP))
        self.wait(2)

        # ------------- Escena 4 (Soft SVM) -------------

        # Limpiar Escena
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # Define the new, wider positions (further from the center)
        # The original was (-3, -2) to (2, 3). Let's move them further out.
        new_margin_plus_start = axes.c2p(-3, -1.5) 
        new_margin_plus_end   = axes.c2p(1.5, 3)

        new_margin_minus_start = axes.c2p(-1.5, -3)
        new_margin_minus_end   = axes.c2p(3, 1.5)

        dot_inside_coord = [[1, 1.5, 0]]
        dot_inside = VGroup(*[Dot(point=axes.c2p(*p), color=BLUE) for p in dot_inside_coord])
        dot_inside_glow = VGroup(*[create_glowing_dot(axes.c2p(*p), BLUE) for p in dot_inside_coord])

        # Mostrar Ejes
        self.play(Create(axes))
        self.wait(0.5)
        
        # Mostrar puntos de datos
        self.play(FadeIn(dots_a), FadeIn(dots_b))
        self.play(dots_a.animate.set_glow(0.5), dots_b.animate.set_glow(0.5))
        self.wait(0.5)

        # Mostrar línea de decisión
        self.play(Create(margin_plus), Create(margin_minus))
        self.wait(1)

        # Mostrar Margenes creciendo
        self.play(
            margin_plus.animate.put_start_and_end_on(new_margin_plus_start, new_margin_plus_end),
            margin_minus.animate.put_start_and_end_on(new_margin_minus_start, new_margin_minus_end),
            run_time=2,
            rate_func=smooth
        )
        self.wait(3)

        # Mostrar línea de decisión
        self.play(Create(line))
        self.wait(1.5)
        self.play(FadeIn(dot_inside), FadeIn(dot_inside_glow))
        self.wait(5)


        # ------------- Escena 5 (Hyperparameter C) -------------

        # Limpiar Escena
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # Mostrar Dual Formulation
        dual_obj = MathTex(
            r"\text{Dual Formulation: } \max_{\alpha} \sum_{i=1}^n \alpha_i - \frac{1}{2} \sum_{i,j=1}^n y_i y_j \alpha_i \alpha_j \space", # Index 0
            r"(x_i \cdot x_j)", # Index 1
            font_size=42
        )

        # Mostrar la Condición
        condition = MathTex(
            r"\text{subject to: } 0 \le \alpha_i \le",
            r"C",
            r", \quad \forall i",
            font_size=36
        )

        dual_obj.to_edge(UP, buff=1.5)
        condition.next_to(dual_obj, DOWN, buff=1)

        # Animacion
        self.play(Write(dual_obj))
        self.wait(1)
        self.play(FadeIn(condition, shift=UP))
        self.wait(2.5)

        # Resaltar el hyperparametro C
        framebox = SurroundingRectangle(condition[1], buff=0.05, color=YELLOW)
        self.play(Create(framebox))
        self.wait(1.5)
        self.play(FadeOut(framebox))
        self.wait(3)

        # Resaltar el término del producto punto (intro a kernels)
        framebox = SurroundingRectangle(dual_obj[1], buff=0.05, color=YELLOW)
        self.play(Create(framebox))
        self.wait(4)