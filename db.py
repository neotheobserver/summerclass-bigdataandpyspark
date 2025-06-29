from manim import *

class DatabaseConcepts(Scene):
    def construct(self):
        title = Text("Relational Database Concepts", font_size=42).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)
        self.clear()

        acid_props = [
            ("Atomicity: transactions are all-or-nothing", YELLOW, UP * 3),
            ("Consistency: ensures valid state transitions", GREEN, UP * 1.5),
            ("Isolation: concurrent transactions do not interfere", BLUE, DOWN * 1.5),
            ("Durability: committed data persists", RED, DOWN * 3)
        ]
        
        for text, color, pos in acid_props:
            box = Rectangle(width=9, height=1, color=color).shift(pos)
            label = Text(text, font_size=26).move_to(box)
            self.play(Create(box), Write(label))
            self.wait(1)

        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        pk_text = Text("Primary Key: uniquely identifies records", font_size=28).shift(UP * 2)
        pk_box = Rectangle(width=8, height=1, color=YELLOW).move_to(pk_text)
        self.play(Create(pk_box), Write(pk_text))
        self.wait(1.5)

        fk_text = Text("Foreign Key: references primary key in another table", font_size=28)
        fk_box = Rectangle(width=10, height=1, color=ORANGE).move_to(fk_text)
        self.play(Create(fk_box), Write(fk_text))
        self.wait(1.5)

        index_text = Text("Index: speeds up data retrieval", font_size=28).shift(DOWN * 2)
        index_box = Rectangle(width=7, height=1, color=GREEN).move_to(index_text)
        self.play(Create(index_box), Write(index_text))
        self.wait(2)

if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "high_quality"}):
        scene = DatabaseConcepts()
        scene.render()

