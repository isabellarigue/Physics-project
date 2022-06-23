from manim import *
import numpy as np

class Draw(ThreeDScene):
    def construct(self):
        eixos = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta= -60 * DEGREES)
        
        circulo = Circle()
        
        self.play(Create(eixos))
        self.wait()
        self.play(Create(circulo))

        particula = Sphere(np.array([0,0,3]), radius=0.1)
        self.play(Create(particula))

        linha_1 = Line(start=np.array([1, 0., 0.]), end=np.array([0., 0., 3.]), color=BLUE_E)
        self.play(Create(linha_1))

        arc = ArcBetweenPoints(np.array([2.7, 0, 0]), np.array([3 , 0.1 , 0]), color=RED)
        arc.move_to(np.array([0.05, 0, 2.7]))
        arc.rotate(PI/2)
        self.play(Create(arc))

class Eq(Scene):
    def construct(self):
        announcement = Text("Utilize apenas lei de Gauss para calcular" + "\n" + "o fluxo de campo elétrico sobre todo o plano xy.", font_size = 30)
        self.play(Write(announcement), run_time = 3)
        self.wait(2)
        eq1 = MathTex(r"\Phi = \oint{\vec E dA}")
        eq10 = MathTex(r"\Phi = \oint{\vec E dA} = 0")
        eq2 = MathTex(r"\Phi = \oint{\vec E dA} = \frac{Q_{int}}{\epsilon_0} ")
        eq3 = MathTex(r"\Phi = \frac{\frac{Q}{2}}{\epsilon_0} = ", r"\frac{Q}{2\epsilon_0}")
        eq4 = MathTex(r"\Phi = \frac{Q}{2\epsilon_0} \cdot \Big (1 -\frac{D}{\sqrt{D^2 + R^2}} \Big )")
        eq5 = MathTex(r"\Phi = \frac{Q}{2\epsilon_0} \cdot \Big (1 - 0 \Big )")
        eq6 = MathTex(r"\Phi = \frac{Q}{2\epsilon_0}")
        #self.add(eq1)
        self.play(announcement.animate.next_to(eq1, 3*UP, buff=0.5))
        self.play(Write(eq1), run_time=3)
        self.wait(2)
        self.play(TransformMatchingShapes(eq1, eq10))
        self.wait(2)
        self.play(TransformMatchingTex(eq10, eq2))
        self.wait(2)
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait(2)
        box1 = SurroundingRectangle(eq3[1], buff=0.1)
        self.play(Create(box1))
        self.wait(2)
        self.remove(box1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(2)
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait(2)
        self.play(TransformMatchingShapes(eq5, eq6))
        self.wait(2)
