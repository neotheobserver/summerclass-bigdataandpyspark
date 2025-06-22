from manim import *

class DataEngineeringVideo(Scene):
    def construct(self):
        # Clear the scene initially
        self.clear()

        # Title
        title = Text("Introduction to Data Engineering", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Section 1: Introduction to Data Engineering
        intro_title = Text("What is Data Engineering?", font_size=30, color=BLUE).to_edge(UP)
        intro_text = Text(
            "Collection and Processing of data\n\nData engineers build pipelines to collect,\ntransform, and store large-scale data.",
            font_size=22
        ).move_to(UP * 1.5)
        intro_note = Text(
            "Enables analytics, machine learning, and insights.",
            font_size=22
        ).move_to(DOWN * 1.5)
        self.play(Write(intro_title), Write(intro_text))
        self.wait(2)
        self.play(Write(intro_note))
        # Pipeline visualization
        pipeline = VGroup(
            Rectangle(width=2, height=0.8, color=WHITE, fill_opacity=0.2).move_to(LEFT * 4),
            Arrow(LEFT * 3, LEFT * 2, buff=0.2),
            Rectangle(width=2, height=0.8, color=YELLOW, fill_opacity=0.2).move_to(LEFT * 1),
            Arrow(LEFT * 0, RIGHT * 1, buff=0.2),
            Rectangle(width=2, height=0.8, color=GREEN, fill_opacity=0.2).move_to(RIGHT * 2)
        )
        pipeline_labels = VGroup(
            Text("Extract", font_size=18).move_to(LEFT * 4),
            Text("Transform", font_size=18).move_to(LEFT * 1),
            Text("Load", font_size=18).move_to(RIGHT * 2)
        )
        self.play(Create(pipeline), Write(pipeline_labels))
        self.wait(2)
        self.play(FadeOut(intro_title), FadeOut(intro_text), FadeOut(intro_note), FadeOut(pipeline), FadeOut(pipeline_labels))
        self.clear()

        # Section 2: Bash Shell in Data Engineering
        bash_title = Text("Bash Shell in Data Engineering", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(bash_title))
        bash_text = Text(
            "Bash scripts automate file handling\nand job scheduling in pipelines.",
            font_size=22
        ).move_to(UP * 1.5)
        self.play(Write(bash_text))
        self.wait(2)
        # Bash code snippet
        bash_code = Code(
            code_string="""
#!/bin/bash
for file in *.csv; do
    mv "$file" "processed/$file"
done
echo "Files moved!"
            """,
            language="bash"
        ).scale(0.8).move_to(UP * 0)
        self.play(Create(bash_code))
        bash_note = Text(
            "Automates moving CSV files to a processed directory.",
            font_size=22
        ).move_to(DOWN * 2.5)
        self.play(Write(bash_note))
        # File movement animation
        file = Rectangle(width=0.8, height=0.4, color=WHITE, fill_opacity=0.2).move_to(DOWN * 1)
        file_label = Text("data.csv", font_size=18).move_to(file.get_center())
        processed = Rectangle(width=1.2, height=0.6, color=GREEN, fill_opacity=0.2).move_to(DOWN * 1 + RIGHT * 3)
        processed_label = Text("processed/", font_size=18).move_to(processed.get_center())
        self.play(Create(file), Write(file_label), Create(processed), Write(processed_label))
        self.play(file.animate.move_to(processed.get_center()), file_label.animate.move_to(processed.get_center()))
        self.wait(2)
        self.play(FadeOut(bash_title), FadeOut(bash_text), FadeOut(bash_code), FadeOut(bash_note), FadeOut(file), FadeOut(file_label), FadeOut(processed), FadeOut(processed_label))
        self.clear()

        # Section 3: Python in Data Engineering
        python_title = Text("Python in Data Engineering", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(python_title))
        python_text = Text(
            "Python powers ETL pipelines with libraries\nlike pandas and PySpark.",
            font_size=22
        ).move_to(UP * 1.5)
        self.play(Write(python_text))
        self.wait(2)
        # Python code snippet
        python_code = Code(
            code_string="""
import pandas as pd
df = pd.read_csv("data.csv")
df["total"] = df["price"] * df["quantity"]
df.to_csv("transformed.csv")
            """,
            language="python"
        ).scale(0.8).move_to(UP * 0)
        self.play(Create(python_code))
        python_note = Text(
            "Transforms data by adding a 'total' column.",
            font_size=22
        ).move_to(DOWN * 2.5)
        self.play(Write(python_note))
        # Data transformation animation
        data_in = Rectangle(width=1.2, height=0.8, color=WHITE, fill_opacity=0.2).move_to(LEFT * 3 + DOWN * 1)
        data_in_label = Text("data.csv", font_size=18).move_to(data_in.get_center())
        data_out = Rectangle(width=1.2, height=0.8, color=YELLOW, fill_opacity=0.2).move_to(RIGHT * 3 + DOWN * 1)
        data_out_label = Text("transformed.csv", font_size=18).move_to(data_out.get_center())
        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, buff=0.2).move_to(DOWN * 1)
        transform_label = Text("Transform", font_size=18).move_to(DOWN * 0.2)
        self.play(Create(data_in), Write(data_in_label), Create(data_out), Write(data_out_label), Create(arrow), Write(transform_label))
        self.wait(2)
        self.play(FadeOut(python_title), FadeOut(python_text), FadeOut(python_code), FadeOut(python_note), FadeOut(data_in), FadeOut(data_in_label), FadeOut(data_out), FadeOut(data_out_label), FadeOut(arrow), FadeOut(transform_label))
        self.clear()

        # Section 4: Integration in Pipelines
        pipeline_title = Text("Bash and Python in Data Pipelines", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(pipeline_title))
        pipeline_text = Text(
            "Bash automates workflows,\nPython processes data in pipelines.",
            font_size=22
        ).move_to(UP * 1.5)
        self.play(Write(pipeline_text))
        self.wait(2)
        # Pipeline animation
        workflow = VGroup(
            Rectangle(width=1.5, height=0.8, color=BLUE, fill_opacity=0.2).move_to(LEFT * 4.5),  # Bash
            Arrow(LEFT * 3.75, LEFT * 3, buff=0.2),
            Rectangle(width=1.5, height=0.8, color=YELLOW, fill_opacity=0.2).move_to(LEFT * 2.25),  # Python
            Arrow(LEFT * 1.5, LEFT * 0.75, buff=0.2),
            Rectangle(width=1.5, height=0.8, color=GREEN, fill_opacity=0.2).move_to(0),  # Storage
            Arrow(RIGHT * 0.75, RIGHT * 1.5, buff=0.2),
            Rectangle(width=1.5, height=0.8, color=WHITE, fill_opacity=0.2).move_to(RIGHT * 2.25)  # Analytics
        )
        workflow_labels = VGroup(
            Text("Bash Script", font_size=18).move_to(LEFT * 4.5),
            Text("Python ETL", font_size=18).move_to(LEFT * 2.25),
            Text("Storage", font_size=18).move_to(0),
            Text("Analytics", font_size=18).move_to(RIGHT * 2.25)
        )
        self.play(Create(workflow), Write(workflow_labels))
        pipeline_note = Text(
            "Example: Bash moves files, Python transforms data.",
            font_size=22
        ).move_to(DOWN * 2.5)
        self.play(Write(pipeline_note))
        self.wait(2)
        self.play(FadeOut(pipeline_title), FadeOut(pipeline_text), FadeOut(workflow), FadeOut(workflow_labels), FadeOut(pipeline_note))
        self.clear()

        # End
        end = Text("Thank you!", font_size=36, color=BLUE)
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))

if __name__ == "__main__":
    from manim import config
    config.media_dir = "./media"
    config.output_file = "data_engineering.mp4"
    DataEngineeringVideo().render()
