from manim import *

class DistributedComputingVideo(Scene):
    def construct(self):
        # Clear the scene initially
        self.clear()

        # Title
        title = Text("Distributed & Cloud Computing with PySpark", font_size=32, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Section 1: Distributed Computing
        dist_title = Text("What is Distributed Computing?", font_size=30, color=BLUE).to_edge(UP)
        dist_text = Text(
            "Distributed computing splits large tasks\nacross multiple computers for faster processing.",
            font_size=22
        ).move_to(UP * 1.5)
        dist_note = Text(
            "Handles big data by parallelizing computations.",
            font_size=22
        ).move_to(DOWN * 1.5)
        self.play(Write(dist_title), Write(dist_text))
        self.wait(2)
        self.play(Write(dist_note))
        # Visualize nodes
        nodes = VGroup(*[
            Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(RIGHT * (i - 1) * 2)
            for i in range(3)
        ]).move_to(DOWN * 0.3)
        node_labels = VGroup(*[
            Text(f"Node {i+1}", font_size=20).next_to(nodes[i], DOWN, buff=0.2)
            for i in range(3)
        ])
        self.play(Create(nodes), Write(node_labels))
        self.wait(2)
        self.play(FadeOut(dist_title), FadeOut(dist_text), FadeOut(dist_note), FadeOut(nodes), FadeOut(node_labels))
        self.clear()

        # Section 2: Cloud Computing
        cloud_title = Text("What is Cloud Computing?", font_size=30, color=BLUE).to_edge(UP)
        cloud_text = Text(
            "Cloud computing provides on-demand resources\nlike servers and storage over the internet.",
            font_size=22
        ).move_to(UP * 1.5)
        cloud_note = Text(
            "Enables scalable, flexible infrastructure.",
            font_size=22
        ).move_to(DOWN * 2)
        self.play(Write(cloud_title), Write(cloud_text))
        self.wait(2)
        self.play(Write(cloud_note))
        # Visualize cloud servers
        cloud = Rectangle(width=4, height=2, color=WHITE, fill_opacity=0.2).move_to(DOWN * 0.5)
        cloud_label = Text("Cloud Infrastructure", font_size=20).move_to(cloud.get_center())
        self.play(Create(cloud), Write(cloud_label))
        self.wait(2)
        self.play(FadeOut(cloud_title), FadeOut(cloud_text), FadeOut(cloud_note), FadeOut(cloud), FadeOut(cloud_label))
        self.clear()

        # Section 3: Distributed and Cloud Computing Synergy
        synergy_title = Text("How Cloud Supports Distributed Computing", font_size=30, color=BLUE).to_edge(UP)
        synergy_text = Text(
            "Cloud provides elastic resources for distributed systems,\nenabling dynamic scaling and fault tolerance.",
            font_size=22
        ).move_to(UP * 1.5)
        synergy_note = Text(
            "Example: Spin up more nodes for heavy workloads.",
            font_size=22
        ).move_to(DOWN * 1.5)
        self.play(Write(synergy_title), Write(synergy_text))
        self.wait(2)
        self.play(Write(synergy_note))
        # Visualize scaling
        nodes = VGroup(*[
            Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(RIGHT * (i - 1) * 2)
            for i in range(2)
        ]).move_to(DOWN * 0.5)
        self.play(Create(nodes))
        new_node = Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(RIGHT * 2)
        self.play(Create(new_node))
        self.wait(2)
        self.play(FadeOut(synergy_title), FadeOut(synergy_text), FadeOut(synergy_note), FadeOut(nodes), FadeOut(new_node))
        self.clear()

        # Section 4: PySpark Architecture
        arch_title = Text("PySpark Architecture", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(arch_title))
        # Driver node
        driver = Circle(radius=0.4, color=GREEN, fill_opacity=0.5).move_to(LEFT * 4)
        driver_label = Text("Driver", font_size=20).next_to(driver, DOWN, buff=0.2)
        self.play(Create(driver), Write(driver_label))
        self.wait(1)
        # Worker nodes
        workers = VGroup(*[
            Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(RIGHT * 2 + UP * (i - 1) * 1.5)
            for i in range(3)
        ])
        worker_labels = VGroup(*[
            Text(f"Worker {i+1}", font_size=20).next_to(workers[i], DOWN, buff=0.2)
            for i in range(3)
        ])
        self.play(Create(workers), Write(worker_labels))
        self.wait(1)
        # Arrows
        arrows = VGroup(*[
            Arrow(driver.get_right(), workers[i].get_left(), buff=0.2)
            for i in range(3)
        ])
        self.play(Create(arrows))
        arch_note = Text(
            "Driver coordinates tasks,\nworkers process data in parallel.",
            font_size=22
        ).move_to(DOWN * 2.5)
        self.play(Write(arch_note))
        self.wait(2)
        self.play(FadeOut(driver), FadeOut(driver_label), FadeOut(workers), FadeOut(worker_labels), FadeOut(arrows), FadeOut(arch_note), FadeOut(arch_title))
        self.clear()

        # Section 5: Data Partitioning in PySpark
        part_title = Text("Data Partitioning in PySpark", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(part_title))
        # Data block
        data_block = Rectangle(width=5, height=0.8, color=WHITE, fill_opacity=0.2).move_to(UP * 1)
        data_label = Text("Big Dataset", font_size=20).move_to(data_block.get_center())
        self.play(Create(data_block), Write(data_label))
        self.wait(1)
        # Split into partitions
        partitions = VGroup(*[
            Rectangle(width=1.25, height=0.8, color=YELLOW, fill_opacity=0.2).move_to(LEFT * (3 - 1.5 * i))
            for i in range(4)
        ])
        part_labels = VGroup(*[
            Text(f"Partition {i+1}", font_size=18).move_to(partitions[i].get_center())
            for i in range(4)
        ])
        self.play(
            Transform(data_block, partitions),
            Transform(data_label, part_labels)
        )
        part_note = Text(
            "Data splits into partitions,\nprocessed by workers in parallel.",
            font_size=22
        ).move_to(DOWN * 2.5)
        self.play(Write(part_note))
        self.wait(2)
        self.play(FadeOut(partitions), FadeOut(part_labels), FadeOut(part_note), FadeOut(part_title))
        self.clear()

        # Section 6: PySpark Computation Example
        comp_title = Text("PySpark Computation Example", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(comp_title))
        # Code snippet
        code = Code(
            code_string="""
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()
df = spark.read.csv("data.csv")
result = df.groupBy("category").count()
result.show()
            """,
            language="python"
        ).scale(0.8).move_to(UP * 1)
        self.play(Create(code))
        self.wait(1)
        # Workers processing
        workers = VGroup(*[
            Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(RIGHT * 2 + UP * (i - 1) * 1.5)
            for i in range(3)
        ])
        worker_labels = VGroup(*[
            Text(f"Worker {i+1}", font_size=20).next_to(workers[i], DOWN, buff=0.2)
            for i in range(3)
        ])
        self.play(Create(workers), Write(worker_labels))
        comp_note = Text(
            "Workers compute groupBy in parallel,\nresults aggregated by driver.",
            font_size=22
        ).move_to(DOWN * 2.7)
        self.play(Write(comp_note))
        self.wait(2)
        self.play(FadeOut(code), FadeOut(workers), FadeOut(worker_labels), FadeOut(comp_note), FadeOut(comp_title))
        self.clear()

        # Section 7: Conclusion
        concl_title = Text("Why Learn PySpark?", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(concl_title))
        concl_text = Text(
            "PySpark combines in-memory and distribute computing\nfor fast, scalable big data processing.",
            font_size=22
        ).move_to(UP * 1.5)
        self.play(Write(concl_text))
        self.wait(2)
        self.play(FadeOut(concl_title), FadeOut(concl_text))
        self.clear()

        # End
        end = Text("Thank you!", font_size=36, color=BLUE)
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))

if __name__ == "__main__":
    from manim import config
    config.media_dir = "./media"
    config.output_file = "distributed_computing.mp4"
    DistributedComputingVideo().render()
