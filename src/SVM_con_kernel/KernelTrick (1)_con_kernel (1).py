from manim import *
import numpy as np

class KernelTrickFull(ThreeDScene):
    def construct(self):
        # Configuro el fondo oscuro para que los colores neón resalten más
        self.camera.background_color = "#0a0a1a"
        
        self.introduccion()
        self.wait(1)
        self.problema_xor()
        self.wait(1)
        self.feature_expansion()
        self.wait(1)
        self.kernel_trick_explicacion()
        self.wait(1)
        self.ejemplo_rbf()
        self.wait(1)

    # --------------------------------------------------
    # Sección de introducción
    # --------------------------------------------------
    def introduccion(self):
        title = Text(
            "El Kernel Trick: Un método del ML",
            font_size=48,
            gradient=(BLUE, PURPLE)
        ).to_edge(UP)
        
        # Uso MarkupText para poder colorear palabras específicas dentro del string
        subtitle = MarkupText(
            'Cómo convertir problemas <span foreground="#FC6255">no lineales</span> en <span foreground="#83C167">lineales</span>\nsin pagar el <span foreground="#FFFF00">costo computacional</span>',
            font_size=32
        ).next_to(title, DOWN, buff=1)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    # --------------------------------------------------
    # El problema XOR (Datos no separables linealmente)
    # --------------------------------------------------
    def problema_xor(self):
        # Inicio con la cámara en 2D estándar
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        
        title = Text(
            "Problema: Imposibilidad de separar con una línea recta",
            font_size=36,
            color=RED
        ).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        axes_2d = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        ).shift(DOWN * 0.5)
        
        # Genero puntos aleatorios alrededor de 4 centros para simular XOR
        np.random.seed(42)
        red_points = [
            [np.random.normal(1.5, 0.3), np.random.normal(1.5, 0.3), 0] for _ in range(4)
        ] + [
            [np.random.normal(-1.5, 0.3), np.random.normal(-1.5, 0.3), 0] for _ in range(4)
        ]
        
        blue_points = [
            [np.random.normal(-1.5, 0.3), np.random.normal(1.5, 0.3), 0] for _ in range(4)
        ] + [
            [np.random.normal(1.5, 0.3), np.random.normal(-1.5, 0.3), 0] for _ in range(4)
        ]
        
        red_dots = VGroup(*[Dot(point, color=RED, radius=0.08) for point in red_points])
        blue_dots = VGroup(*[Dot(point, color=BLUE, radius=0.08) for point in blue_points])
        
        line = Line(axes_2d.c2p(-3, 3), axes_2d.c2p(3), color=YELLOW, stroke_width=3)
        fail_text = Text("¡IMPOSIBLE!", color=RED, font_size=30).next_to(line, UP)
        
        self.play(Create(axes_2d), run_time=1)
        # Animo la aparición de puntos con un pequeño retraso entre grupos
        self.play(LaggedStart(
            FadeIn(red_dots),
            FadeIn(blue_dots),
            lag_ratio=0.3
        ), run_time=2)
        self.play(Create(line), Write(fail_text))
        self.wait(1.5)
        self.play(FadeOut(line), FadeOut(fail_text))
        
        insight = Text(
            "Insight: En 3D podemos separarlos con un plano",
            font_size=30,
            color=YELLOW
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(insight)
        self.play(Write(insight))
        self.wait(1)
        
        # Aquí roto la cámara y elimino los elementos 2D para pasar al espacio de características
        self.move_camera(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            run_time=2,
            added_anims=[
                FadeOut(insight),
                FadeOut(axes_2d),
                FadeOut(title)
            ]
        )
        
        # Configuro los ejes tridimensionales
        axes_3d = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-2.5, 2.5],
            x_length=6,
            y_length=6,
            z_length=5,
            axis_config={"color": WHITE}
        )
        self.play(Create(axes_3d))
        
        # Defino la función de mapeo manual: z = x*y
        def kernel_map(point):
            x, y, _ = point
            return np.array([x, y, 0.8 * x * y])
        
        transform_text = Text(
            "Mapeo: (x, y) → (x, y, x·y)",
            font_size=28,
            color=TEAL
        ).to_edge(UP)
        self.add_fixed_in_frame_mobjects(transform_text)
        self.play(Write(transform_text))
        
        # Elevo los puntos aplicando la función de mapeo
        self.play(
            red_dots.animate.apply_function(kernel_map).set_color(RED),
            blue_dots.animate.apply_function(kernel_map).set_color(BLUE),
            run_time=2,
            rate_func=smooth
        )
        
        # Creo el hiperplano separador en z=0
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_color=GREEN,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        # Estos textos se quedan fijos en la pantalla mientras la cámara rota
        plane_label = Text(
            "Plano de separación: z = 0",
            font_size=24,
            color=GREEN
        ).to_edge(DOWN + RIGHT, buff=0.8)
        self.add_fixed_in_frame_mobjects(plane_label)
        
        check_text = Text(
            "✓ Rojos: x·y > 0 (arriba)\n✓ Azules: x·y < 0 (abajo)",
            font_size=26,
            t2c={"✓ Rojos": RED, "✓ Azules": BLUE}
        ).to_edge(DOWN + LEFT, buff=0.8)
        self.add_fixed_in_frame_mobjects(check_text)
        
        self.play(
            Create(plane),
            Write(plane_label),
            Write(check_text),
            run_time=1.5
        )
        
        # Roto suavemente la cámara para apreciar la profundidad
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # Limpio toda la escena antes de la siguiente sección
        self.play(
            FadeOut(red_dots),
            FadeOut(blue_dots),
            FadeOut(plane),
            FadeOut(axes_3d),
            FadeOut(transform_text),
            FadeOut(plane_label),
            FadeOut(check_text)
        )
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1)

    # --------------------------------------------------
    # Explicación del Feature Expansion
    # --------------------------------------------------
    def feature_expansion(self):
        title = Text(
            "Feature Expansion Explícita: El Problema",
            font_size=42,
            color=RED
        ).to_edge(UP)
        self.play(Write(title))
        
        vec_x = MathTex(
            r"\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}",
            font_size=48
        ).shift(LEFT * 4 + UP * 0.5)
        
        arrow = Arrow(LEFT, RIGHT, color=YELLOW).next_to(vec_x, RIGHT, buff=0.5)
        
        phi_x = MathTex(
            r"\phi(\mathbf{x}) = \begin{bmatrix} "
            r"1 \\ \sqrt{2}x_1 \\ \sqrt{2}x_2 \\ "
            r"x_1^2 \\ \sqrt{2}x_1x_2 \\ x_2^2 "
            r"\end{bmatrix}",
            font_size=42
        ).next_to(arrow, RIGHT, buff=0.5)
        
        self.play(Write(vec_x))
        self.play(Create(arrow))
        self.play(Write(phi_x))
        
        dim_text = Text(
            "Dimensión: 6 (para d=2)",
            font_size=30,
            color=RED
        ).next_to(phi_x, DOWN, buff=0.8)
        self.play(Write(dim_text))
        
        general = MathTex(
            r"\text{Para } d \text{ dimensiones: } \binom{d+2}{2} = \frac{(d+2)(d+1)}{2}",
            font_size=36
        ).next_to(dim_text, DOWN, buff=0.8)
        self.play(Write(general))
        
        example = MathTex(
            r"d=100 \quad \Rightarrow \quad \text{dim}(\phi(\mathbf{x})) = 5151",
            font_size=40,
            color=YELLOW
        ).next_to(general, DOWN, buff=1)
        self.play(Write(example))
        
        cost = Text(
            "Costo: O(d²) operaciones por producto interno",
            font_size=34,
            color=RED
        ).next_to(example, DOWN, buff=1)
        self.play(Write(cost))
        self.wait(2)
        
        # Borro todo lo anterior de golpe para centrar la atención en la pregunta
        self.play(
            FadeOut(title),
            FadeOut(vec_x),
            FadeOut(arrow),
            FadeOut(phi_x),
            FadeOut(dim_text),
            FadeOut(general),
            FadeOut(example),
            FadeOut(cost),
            run_time=0.5
        )
        self.wait(0.2)
        
        # Pongo la pregunta en el centro para hacer la transición conceptual
        transition = Text(
            "¿Podemos evitar calcular φ(x) explícitamente?",
            font_size=40,
            color=TEAL,
            weight=BOLD
        ).move_to(ORIGIN)
        self.play(Write(transition))
        self.wait(2)
        
        self.play(FadeOut(transition))

    # --------------------------------------------------
    # Definición del Kernel Trick
    # --------------------------------------------------
    def kernel_trick_explicacion(self):
        title = Text(
            "El Kernel Trick: Computación Eficiente",
            font_size=42,
            color=GREEN
        ).to_edge(UP)
        self.play(Write(title))
        
        # Solo muestro la ecuación fundamental para no saturar
        kernel_eq = MathTex(
            r"K(x, z) = \phi(x)^T \phi(z)",
            font_size=48,
            color=YELLOW
        ).move_to(ORIGIN)
        
        self.play(Write(kernel_eq))
        self.wait(2)
        
        explanation = Text(
            "¡El kernel trick evita calcular φ(x) explícitamente!",
            font_size=36,
            color=TEAL
        ).next_to(kernel_eq, DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # Pongo un ejemplo simple con kernel polinomial
        example = MathTex(
            r"K(x, z) = (1 + xz)^2 = 1 + 2xz + (xz)^2",
            font_size=40,
            color=BLUE
        ).next_to(explanation, DOWN, buff=0.8)
        
        self.play(Write(example))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(kernel_eq),
            FadeOut(explanation),
            FadeOut(example)
        )

    # --------------------------------------------------
    # Kernel RBF (Gaussiano) y visualización
    # --------------------------------------------------
    def ejemplo_rbf(self):
        gamma = 0.8
        
        # Desglose matemático paso a paso
        
        # Muestro la fórmula inicial del kernel gaussiano
        rbf_formula = MathTex(
            r"K(x, z) = e^{-\gamma (x - z)^2}",
            font_size=40,
            color=YELLOW
        ).move_to(UP * 2.5)
        
        self.play(Write(rbf_formula))
        self.wait(2)
        
        # Expando el término cuadrático dentro del exponente
        expansion = MathTex(
            r"= e^{-\gamma (x^2 + z^2 - 2xz)}",
            font_size=40,
            color=TEAL
        ).next_to(rbf_formula, DOWN, buff=0.6)
        
        self.play(Write(expansion))
        self.wait(2)
        
        # Separo en términos individuales y resalto el término cruzado
        split = MathTex(
            r"= \underbrace{e^{-\gamma x^2}}_{\text{Solo x}} \cdot \underbrace{e^{-\gamma z^2}}_{\text{Solo z}} \cdot \underbrace{e^{2\gamma xz}}_{\text{Crucial}}",
            font_size=36,
            color=GREEN
        ).next_to(expansion, DOWN, buff=0.6)
        
        self.play(Write(split))
        self.wait(2.5)
        
        # Aplico la expansión de Taylor para mostrar que es una suma infinita
        taylor = MathTex(
            r"e^{2\gamma xz} = 1 + 2\gamma xz + \frac{(2\gamma xz)^2}{2!} + \frac{(2\gamma xz)^3}{3!} + \cdots",
            font_size=36,
            color=BLUE
        ).next_to(split, DOWN, buff=0.6)
        
        self.play(Write(taylor))
        self.wait(3)
        
        # Construyo visualmente los vectores de características infinitos
        vector1 = MathTex(
            r"\phi(x) = \left[1, \sqrt{2\gamma}\,x, \sqrt{\frac{(2\gamma)^2}{2!}}\,x^2, \cdots \right]",
            font_size=28,
            color=ORANGE
        ).next_to(taylor, DOWN, buff=0.8).shift(LEFT * 2)
        
        projection_text = Text(
            "φ(x) será la función de proyección",
            font_size=24,
            color=ORANGE
        ).next_to(vector1, DOWN, buff=0.2)
        
        vector2 = MathTex(
            r"\phi(z) = \left[1, \sqrt{2\gamma}\,z, \sqrt{\frac{(2\gamma)^2}{2!}}\,z^2, \cdots \right]",
            font_size=28,
            color=ORANGE
        ).next_to(vector1, RIGHT, buff=0.8)
        
        self.play(
            Write(vector1),
            Write(projection_text),
            Write(vector2),
            run_time=2
        )
        self.wait(3)
        
        conclusion = Text(
            "K(x, z) = φ(x)ᵀ φ(z)",
            font_size=32,
            color=TEAL
        ).next_to(vector2, DOWN, buff=1.0)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        # Limpio la parte matemática para pasar a la geometría
        self.play(
            FadeOut(rbf_formula),
            FadeOut(expansion),
            FadeOut(split),
            FadeOut(taylor),
            FadeOut(vector1),
            FadeOut(projection_text),
            FadeOut(vector2),
            FadeOut(conclusion),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Aquí empieza la visualización 3D de la "montaña" gaussiana
        title_vis = Text(
            "Visualización del Kernel RBF",
            font_size=36,
            color=BLUE
        ).to_edge(UP)
        
        axes_2d = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE}
        ).shift(DOWN * 0.5)
        
        self.play(Create(axes_2d))
        
        data_points = VGroup(
            Dot([-1.5, 1.5, 0], color=RED, radius=0.1),
            Dot([1.5, -1.5, 0], color=RED, radius=0.1),
            Dot([-1.5, -1.5, 0], color=BLUE, radius=0.1),
            Dot([1.5, 1.5, 0], color=BLUE, radius=0.1),
        )
        
        self.play(FadeIn(data_points))
        
        reference = Dot(ORIGIN, color=YELLOW, radius=0.15)
        reference_label = Text(
            "Punto de referencia",
            font_size=20,
            color=YELLOW
        ).next_to(reference, UP, buff=0.3)
        
        self.play(FadeIn(reference), Write(reference_label))
        
        # Creo círculos concéntricos para representar las curvas de nivel en 2D
        circles = VGroup()
        for i, r in enumerate(np.linspace(0.5, 2.5, 5)):
            circle = Circle(
                radius=r,
                color=BLUE,
                stroke_width=2,
                fill_opacity=0.15 - i*0.025,
                stroke_opacity=0.7 - i*0.1
            )
            circles.add(circle)
        
        # Hago la transición de 2D a 3D
        self.play(FadeOut(axes_2d), FadeOut(data_points), run_time=1)
        self.wait(0.5)
        
        self.move_camera(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            run_time=2
        )
        
        # Defino la superficie 3D basada en la función gaussiana
        def rbf_surface_func(u, v):
            distance_sq = u**2 + v**2
            z = np.exp(-gamma * distance_sq)
            return np.array([u, v, z])
        
        rbf_surface = Surface(
            rbf_surface_func,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_color=BLUE,
            fill_opacity=0.8,
            stroke_width=0.5,
            resolution=(30, 30)
        )
        
        axes_3d_rbf = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[0, 1.2],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": WHITE}
        )
        
        self.play(
            Create(axes_3d_rbf),
            Create(rbf_surface),
            run_time=2
        )
        
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # Añado textos explicativos fijos tras la rotación
        fixed_title = Text(
            "Visualización del Kernel RBF", 
            font_size=36,
            color=BLUE
        ).to_edge(UP)
        
        fixed_intensity = Text(
            "Similitud ↓ al aumentar la distancia",
            font_size=26,
            color=RED
        ).to_edge(DOWN, buff=0.8)
        
        fixed_rbf = Text(
            "RBF: Mide similitud mediante distancia euclidiana",
            font_size=24,
            color=TEAL
        ).next_to(fixed_intensity, DOWN, buff=0.3)
        
        self.add_fixed_in_frame_mobjects(fixed_title)
        self.add_fixed_in_frame_mobjects(fixed_intensity)
        self.add_fixed_in_frame_mobjects(fixed_rbf) 
        self.wait(3)
        
        self.play(
            FadeOut(axes_3d_rbf),
            FadeOut(rbf_surface),
            FadeOut(reference),
            FadeOut(reference_label),
            FadeOut(circles),
            FadeOut(fixed_title),
            FadeOut(fixed_intensity),
            FadeOut(fixed_rbf),
            run_time=1.5
        )