from manim import *

class GitWorkflow(Scene):
    def construct(self):
        # Title with adjusted position
        title = Text("Git Workflow Overview", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.move_to(UP * 2.5))  # Higher title to avoid overlap

        # Part 1: Working Directory -> Staging Area -> Local Repository -> Remote Server
        working_dir = Rectangle(width=1.8, height=0.9, color=WHITE, fill_opacity=0.2).shift(LEFT * 5)
        working_label = Text("Working Directory", font_size=22).next_to(working_dir, UP, buff=0.4)
        staging_area = Rectangle(width=1.8, height=0.9, color=WHITE, fill_opacity=0.2).shift(LEFT * 1.5)
        staging_label = Text("Staging Area", font_size=22).next_to(staging_area, UP, buff=0.4)
        local_repo = Rectangle(width=1.8, height=0.9, color=WHITE, fill_opacity=0.2).shift(RIGHT * 2)
        local_label = Text("Local Repository", font_size=22).next_to(local_repo, UP, buff=0.4)
        remote_server = Circle(radius=0.4, color=WHITE, fill_opacity=0.2).shift(RIGHT * 5)
        remote_label = Text("Remote Server", font_size=22).next_to(remote_server, UP, buff=0.4)

        self.play(
            Create(working_dir), Write(working_label),
            Create(staging_area), Write(staging_label),
            Create(local_repo), Write(local_label),
            Create(remote_server), Write(remote_label)
        )
        self.wait(1)

        file = Rectangle(width=0.7, height=0.35, color=RED, fill_opacity=0.5).move_to(working_dir.get_center())
        file_label = Text("main.py", font_size=14, color=WHITE).move_to(file.get_center())
        file_group = VGroup(file, file_label)
        self.play(FadeIn(file_group))

        arrow_add = Arrow(working_dir.get_right(), staging_area.get_left(), color=YELLOW, buff=0.4)
        label_add = Text("git add", font_size=18, color=YELLOW).next_to(arrow_add, UP, buff=0.3)
        self.play(Create(arrow_add), Write(label_add))
        self.play(file_group.animate.move_to(staging_area.get_center()))
        self.wait(1)
        self.play(FadeOut(arrow_add), FadeOut(label_add))

        arrow_commit = Arrow(staging_area.get_right(), local_repo.get_left(), color=YELLOW, buff=0.4)
        label_commit = Text("git commit", font_size=18, color=YELLOW).next_to(arrow_commit, UP, buff=0.3)
        self.play(Create(arrow_commit), Write(label_commit))
        self.play(file_group.animate.move_to(local_repo.get_center()))
        self.wait(1)
        self.play(FadeOut(arrow_commit), FadeOut(label_commit))

        arrow_push = Arrow(local_repo.get_right(), remote_server.get_left(), color=YELLOW, buff=0.4)
        label_push = Text("git push", font_size=18, color=YELLOW).next_to(arrow_push, UP, buff=0.3)
        self.play(Create(arrow_push), Write(label_push))
        self.play(file_group.animate.move_to(remote_server.get_center()))
        self.wait(1)
        self.play(FadeOut(arrow_push), FadeOut(label_push))

        self.play(FadeOut(working_dir, working_label, staging_area, staging_label,
                          local_repo, local_label, remote_server, remote_label, file_group))
        self.wait(1)

        # Part 2: git pull and git clone
        remote_server = Circle(radius=0.4, color=WHITE, fill_opacity=0.2).shift(UP * 1 + RIGHT * 2)
        remote_label = Text("Remote Server", font_size=22).next_to(remote_server, UP, buff=0.4)
        local_repo = Rectangle(width=1.8, height=0.9, color=WHITE, fill_opacity=0.2).shift(UP * 1 + LEFT * 2)
        local_label = Text("Local Repository", font_size=22).next_to(local_repo, UP, buff=0.4)
        self.play(Create(remote_server), Write(remote_label), Create(local_repo), Write(local_label))

        file_group = VGroup(
            Rectangle(width=0.7, height=0.35, color=RED, fill_opacity=0.5).move_to(remote_server.get_center()),
            Text("main.py", font_size=14, color=WHITE).move_to(remote_server.get_center())
        )
        self.play(FadeIn(file_group))
        arrow_pull = Arrow(remote_server.get_left(), local_repo.get_right(), color=YELLOW, buff=0.4)
        label_pull = Text("git pull", font_size=18, color=YELLOW).next_to(arrow_pull, UP, buff=0.4)
        self.play(Create(arrow_pull), Write(label_pull))
        self.play(file_group.animate.move_to(local_repo.get_center()))
        self.wait(1)
        self.play(FadeOut(arrow_pull), FadeOut(label_pull))

        new_local_repo = Rectangle(width=1.8, height=0.9, color=WHITE, fill_opacity=0.2).shift(DOWN * 1)
        new_local_label = Text("New Local Repository", font_size=22).next_to(new_local_repo, UP, buff=0.4)
        self.play(Create(new_local_repo), Write(new_local_label))
        arrow_clone = Arrow(remote_server.get_bottom(), new_local_repo.get_top(), color=YELLOW, buff=0.4)
        label_clone = Text("git clone", font_size=18, color=YELLOW).next_to(arrow_clone, RIGHT, buff=0.4)
        self.play(Create(arrow_clone), Write(label_clone))
        new_file_group = VGroup(
            Rectangle(width=0.7, height=0.35, color=RED, fill_opacity=0.5).move_to(remote_server.get_center()),
            Text("main.py", font_size=14, color=WHITE).move_to(remote_server.get_center())
        )
        self.play(FadeIn(new_file_group))
        self.play(new_file_group.animate.move_to(new_local_repo.get_center()))
       	self.wait(1)
        self.clear()

	# Title for merge scene
        title = Text("Git Merge Process", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.move_to(UP * 2.5))

        # Local Repository
        local_repo = Rectangle(width=3, height=1.5, color=WHITE, fill_opacity=0.2).shift(DOWN * 0.5)
        local_label = Text("Local Repository", font_size=22).next_to(local_repo, UP, buff=0.4)
        self.play(Create(local_repo), Write(local_label))

        # Initial branches with version history
        feature_branch = VGroup(
            Rectangle(width=0.7, height=0.35, color=GREEN, fill_opacity=0.5).move_to(local_repo.get_center() + LEFT * 1),
            Text("feature", font_size=14, color=WHITE).move_to(local_repo.get_center() + LEFT * 1)
        )
        main_branch = VGroup(
            Rectangle(width=0.7, height=0.35, color=BLUE, fill_opacity=0.5).move_to(local_repo.get_center() + RIGHT * 1),
            Text("main", font_size=14, color=WHITE).move_to(local_repo.get_center() + RIGHT * 1)
        )
        # Version history (commit points)
        feature_commits = VGroup(
            Dot(color=GREEN).move_to(local_repo.get_center() + LEFT * 1.5 + UP * 0.3),
            Dot(color=GREEN).move_to(local_repo.get_center() + LEFT * 1.2 + DOWN * 0.3)
        )
        main_commits = VGroup(
            Dot(color=BLUE).move_to(local_repo.get_center() + RIGHT * 1.5 + UP * 0.3),
            Dot(color=BLUE).move_to(local_repo.get_center() + RIGHT * 1.2 + DOWN * 0.3)
        )
        self.play(FadeIn(feature_branch, main_branch, feature_commits, main_commits))
        self.wait(0.5)  # Frame 1: Show branches and commits

        # Highlight feature branch and its history
        self.play(feature_branch.animate.set_fill(GREEN, opacity=1.0), main_branch.animate.set_fill(BLUE, opacity=0.5),
                  feature_commits.animate.set_color(GREEN).set_opacity(1.0), main_commits.animate.set_opacity(0.5))
        self.wait(0.5)  # Frame 2: Highlight feature branch

        # Highlight main branch and its history
        self.play(feature_branch.animate.set_fill(GREEN, opacity=0.5), main_branch.animate.set_fill(BLUE, opacity=1.0),
                  feature_commits.animate.set_opacity(0.5), main_commits.animate.set_color(BLUE).set_opacity(1.0))
        self.wait(0.5)  # Frame 3: Highlight main branch

        # Merge process
        merge_label = Text("git merge", font_size=18, color=YELLOW).next_to(local_repo, DOWN, buff=0.4)
        self.play(Write(merge_label))
        merged_file = VGroup(
            Rectangle(width=0.7, height=0.35, color=RED, fill_opacity=0.5).move_to(local_repo.get_center()),
            Text("main.py", font_size=14, color=WHITE).move_to(local_repo.get_center())
        )
        self.play(feature_branch.animate.move_to(local_repo.get_center()), main_branch.animate.move_to(local_repo.get_center()),
                  FadeOut(feature_commits, main_commits))
        self.play(FadeIn(merged_file))
        self.wait(1)


if __name__ == "__main__":
    config.media_dir = "./media"
    config.output_file = "git_workflow.mp4"
    GitWorkflow().render()