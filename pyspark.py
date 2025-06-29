from manim import *

class PySparkVisualDemo(Scene):
    def construct(self):
        # Title
        title = Text("PySpark Concepts", font_size=48).to_edge(UP)
        self.play(FadeIn(title))
        self.clear()
        
        # Transformations vs Actions
        t_box = Rectangle(width=4, height=2, color=TEAL).shift(LEFT * 3)
        a_box = Rectangle(width=4, height=2, color=ORANGE).shift(RIGHT * 3)
        t_text = Text("Transformations", font_size=24).move_to(t_box)
        a_text = Text("Actions", font_size=24).move_to(a_box)
        self.play(Create(t_box), Create(a_box), Write(t_text), Write(a_text))
        self.wait(1)
        arrow = Arrow(t_box.get_right(), a_box.get_left(), buff=0.2)
        self.play(Create(arrow))
        self.wait(1)
        
        # DAG Representation
        self.play(FadeOut(t_box, a_box, t_text, a_text, arrow))
        dag_title = Text("DAG (Directed Acyclic Graph)", font_size=32).shift(UP * 3)
        nodes = [Circle(radius=0.3, color=WHITE).shift(UP * 1.5),
                 Circle(radius=0.3, color=WHITE).shift(LEFT * 2),
                 Circle(radius=0.3, color=WHITE).shift(RIGHT * 2),
                 Circle(radius=0.3, color=WHITE).shift(DOWN * 1.5)]
        edges = [Arrow(nodes[0].get_center(), nodes[1].get_center()),
                 Arrow(nodes[0].get_center(), nodes[2].get_center()),
                 Arrow(nodes[1].get_center(), nodes[3].get_center()),
                 Arrow(nodes[2].get_center(), nodes[3].get_center())]
        self.play(Write(dag_title), *[Create(n) for n in nodes], *[Create(e) for e in edges])
        self.wait(2)
        self.play(FadeOut(dag_title, *nodes, *edges))

        # Partitioning & Shuffle
        part_text = Text("Shuffle", font_size=32).shift(UP * 3)
        self.play(Write(part_text))

        # Show partitions in executors
        partitions = VGroup()
        for i in range(4):
            p = Rectangle(width=1, height=0.5, color=BLUE).shift(LEFT * 4 + DOWN * (i - 1.5))
            partitions.add(p)
        self.play(*[Create(p) for p in partitions])

        # Explain data movement (shuffle)
        shuffle_boxes = VGroup()
        for i in range(4):
            s = Rectangle(width=1, height=0.5, color=RED).shift(RIGHT * 4 + DOWN * (i - 1.5))
            shuffle_boxes.add(s)
        arrows = VGroup()
        for p, s in zip(partitions, shuffle_boxes):
            arrows.add(Arrow(p.get_right(), s.get_left(), buff=0.1))
        
        self.play(*[Create(a) for a in arrows], *[Create(s) for s in shuffle_boxes])

        shuffle_label = Text("Data shuffled across partitions for operations like join, groupBy", font_size=20).shift(DOWN * 3)
        self.play(Write(shuffle_label))
        self.wait(3)

        # Clean up
        self.play(FadeOut(part_text, partitions, shuffle_boxes, arrows, shuffle_label))
        self.wait(1)

        # Column vs Row Formats
        # self.play(FadeOut(part_text, part1, part2, part3, shuffle_box, *arrows))
        format_text = Text("File Formats: Column vs Row", font_size=32).shift(UP * 3)
        col_box = Rectangle(width=3, height=2, color=GREEN).shift(LEFT * 3)
        row_box = Rectangle(width=3, height=2, color=PURPLE).shift(RIGHT * 3)
        col_label = Text("Parquet\n(Column)", font_size=20).move_to(col_box)
        row_label = Text("CSV\n(Row)", font_size=20).move_to(row_box)
        self.play(Write(format_text), Create(col_box), Create(row_box), Write(col_label), Write(row_label))
        self.wait(2)

        # Outro
        outro = Text("End of PySpark Concepts", font_size=32)
        self.play(FadeOut(format_text, col_box, row_box, col_label, row_label), Write(outro))
        self.wait(2)

if __name__ == "__main__":
    from manim import config, tempconfig
    with tempconfig({"quality": "high_quality"}):
        scene = PySparkVisualDemo()
        scene.render()


