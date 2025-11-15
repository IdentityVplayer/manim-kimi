from manim import *

class Regular257GonConstructible(MovingCameraScene):
    def construct(self):
        # ========== 颜色配置 ==========
        col_257 = "#FF5252"      # 亮红
        col_fermat = "#FFD54F"   # 琥珀
        col_tool = "#FFB74D"     # 橙色
        col_geo = "#64B5F6"      # 浅蓝
        col_success = "#81C784"  # 绿色
        col_text = "#EEEEEE"     # 白灰

        # ========== 第1幕：定理引入 ==========
        # 标题
        title = Text("正257边形可尺规作图", font_size=40, color=col_text)
        title.to_edge(UP, buff=0.5)
        
        # 费马素数公式
        theorem = MathTex(
            "n = p = 2^{2^k} + 1 \\quad (\\text{费马素数})",
            tex_to_color_map={"2^{2^k}": col_fermat, "+1": col_257}
        )
        theorem.next_to(title, DOWN, buff=0.6)
        
        # 257的具体表示
        eq_257 = MathTex(
            "257 = 2^{2^3} + 1 = 2^8 + 1",
            tex_to_color_map={"257": col_257, "2^{2^3}": col_fermat, "2^8": col_fermat, "+1": col_257}
        )
        eq_257.next_to(theorem, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(theorem), run_time=2)
        self.wait(1)
        self.play(Write(eq_257), run_time=2)
        self.wait(1)
        
        # 相机聚焦
        self.play(self.camera.frame.animate.scale(1.2).shift(DOWN*0.3), run_time=2)
        
        # ========== 第2幕：尺规操作演示 ==========
        self.play(FadeOut(VGroup(title, theorem, eq_257)), run_time=1)
        
        # 左移相机
        self.play(self.camera.frame.animate.shift(LEFT*4).scale(1/1.2), run_time=1.5)
        
        # 尺规图标
        ruler = Rectangle(width=3, height=0.1, color=col_tool, fill_opacity=0.3)
        ruler.move_to(LEFT*4 + UP*2)
        ruler_label = Text("直尺", font_size=24, color=col_tool).next_to(ruler, UP, buff=0.2)
        
        compass_arm1 = Line(LEFT*4 + DOWN*0.5, LEFT*3.5 + DOWN*1.5, color=col_tool, stroke_width=6)
        compass_arm2 = Line(LEFT*4 + DOWN*0.5, LEFT*4.5 + DOWN*1.5, color=col_tool, stroke_width=6)
        compass_arc = Arc(radius=0.3, arc_center=LEFT*4 + DOWN*0.5, start_angle=-75*DEGREES, angle=150*DEGREES, color=col_tool, stroke_width=4)
        compass = VGroup(compass_arm1, compass_arm2, compass_arc)
        compass_label = Text("圆规", font_size=24, color=col_tool).next_to(compass, DOWN, buff=0.2)
        
        tools = VGroup(ruler, ruler_label, compass, compass_label)
        
        # 右侧操作区域
        center = RIGHT*2 + UP*0.5
        O = Dot(center, color=col_geo)
        O_label = Text("O", font_size=24, color=col_text).next_to(O, UL, buff=0.1)
        
        # 操作1：画圆
        circle = Circle(radius=1.5, color=col_geo).move_to(center)
        step1 = Text("画圆", font_size=24, color=col_text).next_to(circle, DOWN, buff=0.5)
        
        self.play(FadeIn(tools), run_time=1)
        self.play(Create(circle), FadeIn(O), FadeIn(O_label), Write(step1), run_time=2)
        
        # 操作2：标记交点
        A = Dot(center + LEFT*1.5, color=col_success)
        B = Dot(center + RIGHT*1.5, color=col_success)
        A_label = Text("A", font_size=24, color=col_text).next_to(A, LEFT, buff=0.1)
        B_label = Text("B", font_size=24, color=col_text).next_to(B, RIGHT, buff=0.1)
        step2 = Text("标记交点", font_size=24, color=col_text).next_to(circle, DOWN, buff=0.5)
        
        self.wait(0.5)
        self.play(FadeOut(step1), FadeIn(VGroup(A, B, A_label, B_label)), Write(step2), run_time=2)
        
        # 操作3：角平分
        C = Dot(center + UP*1.5, color=col_success)
        C_label = Text("C", font_size=24, color=col_text).next_to(C, UP, buff=0.1)
        bisector = Line(center, C, color=col_geo)
        step3 = Text("角平分", font_size=24, color=col_text).next_to(circle, DOWN, buff=0.5)
        
        self.wait(0.5)
        self.play(FadeOut(step2), Create(bisector), FadeIn(C), FadeIn(C_label), Write(step3), run_time=2)
        
        # ========== 第3幕：角度分割原理 ==========
        self.play(FadeOut(VGroup(tools, circle, O, O_label, A, B, C, A_label, B_label, C_label, bisector, step3)), run_time=1)
        self.play(self.camera.frame.animate.move_to(ORIGIN).scale(1.5), run_time=1.5)
        
        # 单位圆
        unit_circle = Circle(radius=2, color=col_geo)
        self.play(Create(unit_circle), run_time=1.5)
        
        # 初始半径
        radius = Line(ORIGIN, RIGHT*2, color=col_text)
        zero_label = Text("0°", font_size=24, color=col_text).next_to(RIGHT*2, RIGHT, buff=0.2)
        self.play(Create(radius), FadeIn(zero_label), run_time=1)
        
        # 目标文字
        goal = Text("圆周角 360° 需分成 257 等份", font_size=30, color=col_text)
        goal.next_to(unit_circle, UP, buff=0.8)
        self.play(Write(goal), run_time=1.5)
        
        # 重复平分示意
        angles = VGroup()
        for i in range(3):
            angle = MathTex(f"\\frac{{360°}}{{{2**i}}}", color=col_fermat, font_size=32)
            angle.next_to(unit_circle, DOWN, buff=0.5 + i*0.3)
            angles.add(angle)
            
            if i > 0:
                arrow = Arrow(angles[i-1].get_bottom(), angle.get_top(), color=col_geo, buff=0.1)
                self.play(GrowArrow(arrow), run_time=0.5)
            
            self.play(Write(angle), run_time=1)
        
        # 最终结果
        final_angle = MathTex("\\frac{360°}{257} \\approx 1.40078°", color=col_257, font_size=34)
        final_angle.next_to(angles, DOWN, buff=0.5)
        arrow_final = Arrow(angles[-1].get_bottom(), final_angle.get_top(), color=col_geo, buff=0.1)
        
        self.play(GrowArrow(arrow_final), run_time=0.5)
        self.play(Write(final_angle), run_time=1.5)
        self.wait(1)
        
        # ========== 第4幕：实际困难提示 ==========
        self.play(FadeOut(VGroup(unit_circle, radius, zero_label, goal, angles, final_angle, arrow_final)), run_time=1)
        self.play(self.camera.frame.animate.shift(DOWN*3).scale(1.2/1.5), run_time=1.5)
        
        # 警告文字
        warning = Text("实际作图需重复 256 次角平分操作", font_size=32, color=col_tool)
        warning.move_to(UP*2)
        
        # 进度条
        bar_bg = Rectangle(width=6, height=0.3, color=col_text, stroke_width=2)
        bar_fill = Rectangle(width=0, height=0.3, color=col_success, fill_opacity=0.8, stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT)
        progress_label = Text("0/256", font_size=28, color=col_text).next_to(bar_bg, UP, buff=0.3)
        
        self.play(Write(warning), run_time=1.5)
        self.play(FadeIn(bar_bg), FadeIn(bar_fill), FadeIn(progress_label), run_time=1)
        
        # 动画计数
        for i in range(1, 257):
            new_width = 6 * (i / 256)
            new_label = Text(f"{i}/256", font_size=28, color=col_text).next_to(bar_bg, UP, buff=0.3)
            
            if i % 8 == 0:  # 每8次更新一次，避免卡顿
                self.play(
                    bar_fill.animate.set_width(new_width, stretch=True),
                    Transform(progress_label, new_label),
                    run_time=0.05
                )
        
        self.wait(0.5)
        
        # 历史提示
        history = Text("人类历史上从未完整手绘过正257边形", font_size=28, color=col_tool)
        history.next_to(bar_bg, DOWN, buff=0.8)
        self.play(Write(history), run_time=2)
        self.wait(1)
        
        # ========== 第5幕：理论可行性总结 ==========
        self.play(FadeOut(VGroup(warning, bar_bg, bar_fill, progress_label, history)), run_time=1)
        self.play(self.camera.frame.animate.shift(UP*3).scale(1.3/1.2), run_time=1.5)
        
        # 三个关键结论
        formula = MathTex("257 = 2^{2^3} + 1", color=col_fermat, font_size=40)
        theorem = MathTex("257 \\text{ 是费马素数}", color=col_success, font_size=40)
        conclusion = MathTex("\\therefore \\text{正257边形可尺规作图}", color=col_success, font_size=40)
        
        conclusions = VGroup(formula, theorem, conclusion).arrange(DOWN, buff=0.8)
        conclusions.shift(UP*0.5)
        
        for i, c in enumerate(conclusions):
            self.play(Write(c), run_time=1.5)
            if i < len(conclusions) - 1:
                self.wait(0.5)
        
        # 引用
        citation = Text("—— 高斯《算术研究》1801", font_size=24, color=col_text)
        citation.next_to(conclusion, DOWN, buff=0.5).shift(RIGHT*1.5)
        self.play(FadeIn(citation), run_time=1.5)
        self.wait(1)
        
        # ========== 第6幕：最终几何示意 ==========
        self.play(FadeOut(VGroup(conclusions, citation)), run_time=1)
        self.play(self.camera.frame.animate.scale(2.0).rotate(10*DEGREES), run_time=2)
        
        # 稀疏示意正257边形（只画8条线表示）
        sparse_polygon = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            line = Line(ORIGIN, RIGHT*3, color=col_geo, stroke_width=3).rotate(angle, about_point=ORIGIN)
            sparse_polygon.add(line)
        
        # 中心标注
        note = Text("示意图（非实际作图）", font_size=24, color=col_text)
        note.next_to(ORIGIN, DOWN, buff=1.5)
        
        # 最终结论
        final_text = Text("正257边形理论上可构造", font_size=36, color=col_success)
        final_text.to_edge(UP, buff=0.8)
        
        self.play(Create(sparse_polygon), run_time=2)
        self.play(FadeIn(note), Write(final_text), run_time=1.5)
        self.wait(3)
        
        # 结束
        self.play(FadeOut(VGroup(sparse_polygon, note, final_text)), run_time=1)
        self.wait(0.5)
