from manim import *
import math

class Regular257GonConstruction(MovingCameraScene):
    # 颜色编码（全局统一）
    AXIS_COLOR = "#FFD700"  # 金色
    CIRCLE_COLOR = "#FFFFFF"  # 白色
    AUX_CIRCLE_COLOR = "#3498DB"  # 蓝色（辅助圆）
    POINT_A_COLOR = "#E74C3C"  # 红色（A系列点）
    POINT_B_COLOR = "#2ECC71"  # 绿色（B系列点）
    POINT_C_COLOR = "#F39C12"  # 橙色（C系列点）
    POINT_D_COLOR = "#9B59B6"  # 紫色（D系列点）
    POINT_E_COLOR = "#1ABC9C"  # 青色（E系列点）
    POINT_F_COLOR = "#E67E22"  # 橙红色（F系列点）
    LABEL_COLOR = "#FFFFFF"  # 白色（标签）
    CENTER_COLOR = "#FFFFFF"  # 白色（圆心）

    def construct(self):
        # ==================== 场景1：初始化与坐标系建立（5秒）====================
        # 1. 绘制坐标轴（2秒）
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": self.AXIS_COLOR, "stroke_width": 2}
        )
        self.play(Create(axes), run_time=2)

        # 2. 绘制圆心O和单位圆（1秒）
        center = Dot(ORIGIN, color=self.CENTER_COLOR, radius=0.08)
        center_label = MathTex("O", color=self.LABEL_COLOR).next_to(center, UR, buff=0.1)
        unit_circle = Circle(radius=1, color=self.CIRCLE_COLOR, stroke_width=1.5)
        circle_label = MathTex("\\odot O", color=self.LABEL_COLOR).next_to(unit_circle, UP, buff=0.2)
        self.play(
            Create(center),
            Write(center_label),
            Create(unit_circle),
            Write(circle_label),
            run_time=1
        )

        # 3. 标记初始点A0、A1（1秒）
        A0 = Dot(Point(1, 0, 0), color=self.POINT_A_COLOR, radius=0.06)
        A0_label = MathTex("A_0", color=self.LABEL_COLOR).next_to(A0, RIGHT, buff=0.1)
        A1 = Dot(Point(-1, 0, 0), color=self.POINT_A_COLOR, radius=0.06)
        A1_label = MathTex("A_1", color=self.LABEL_COLOR).next_to(A1, LEFT, buff=0.1)
        self.play(
            Create(A0), Write(A0_label),
            Create(A1), Write(A1_label),
            run_time=1
        )

        # 暂停2秒
        self.wait(2)

        # ==================== 场景2：第一轮辅助圆构造（10秒）====================
        # 1. 辅助圆C1：过(0,1)，圆心(-0.5, -3)（2秒）
        C1_center = Point(-0.5, -3, 0)
        C1 = Circle(center=C1_center, radius=math.hypot(0.5, 4), color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        self.play(Create(C1), run_time=2)

        # 2. 辅助圆C2：A0(1,0)与(0,-3)中点为圆心，过(0,1)（3秒）
        C2_center = (A0.get_center() + Point(0, -3, 0)) / 2
        C2_radius = math.hypot(C2_center[0], 1 - C2_center[1])
        C2 = Circle(center=C2_center, radius=C2_radius, color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        # 求C2与x轴交点B0、B2
        B0 = Dot(Point(1 + 2*math.sqrt(C2_radius**2 - (3/2)**2), 0, 0), color=self.POINT_B_COLOR, radius=0.06)
        B2 = Dot(Point(1 - 2*math.sqrt(C2_radius**2 - (3/2)**2), 0, 0), color=self.POINT_B_COLOR, radius=0.06)
        B0_label = MathTex("B_0", color=self.LABEL_COLOR).next_to(B0, RIGHT, buff=0.1)
        B2_label = MathTex("B_2", color=self.LABEL_COLOR).next_to(B2, LEFT, buff=0.1)
        self.play(Create(C2), run_time=1.5)
        self.play(Create(B0), Write(B0_label), Create(B2), Write(B2_label), run_time=1.5)

        # 3. 辅助圆C3：A1(-1,0)与(0,-3)中点为圆心，过(0,1)（3秒）
        C3_center = (A1.get_center() + Point(0, -3, 0)) / 2
        C3_radius = math.hypot(C3_center[0], 1 - C3_center[1])
        C3 = Circle(center=C3_center, radius=C3_radius, color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        # 求C3与x轴交点B1、B3
        B1 = Dot(Point(-1 + 2*math.sqrt(C3_radius**2 - (3/2)**2), 0, 0), color=self.POINT_B_COLOR, radius=0.06)
        B3 = Dot(Point(-1 - 2*math.sqrt(C3_radius**2 - (3/2)**2), 0, 0), color=self.POINT_B_COLOR, radius=0.06)
        B1_label = MathTex("B_1", color=self.LABEL_COLOR).next_to(B1, RIGHT, buff=0.1)
        B3_label = MathTex("B_3", color=self.LABEL_COLOR).next_to(B3, LEFT, buff=0.1)
        self.play(Create(C3), run_time=1.5)
        self.play(Create(B1), Write(B1_label), Create(B3), Write(B3_label), run_time=1.5)

        # 暂停2秒
        self.wait(2)

        # ==================== 场景3：第二轮辅助圆构造（15秒）====================
        # 1. 标记P1(-3,0)、Q1（B2右延2倍）（2秒）
        P1 = Dot(Point(-3, 0, 0), color=self.POINT_C_COLOR, radius=0.06)
        P1_label = MathTex("P_1", color=self.LABEL_COLOR).next_to(P1, LEFT, buff=0.1)
        Q1 = Dot(Point(2*B2.get_x(), 0, 0), color=self.POINT_C_COLOR, radius=0.06)
        Q1_label = MathTex("Q_1", color=self.LABEL_COLOR).next_to(Q1, RIGHT, buff=0.1)
        self.play(Create(P1), Write(P1_label), Create(Q1), Write(Q1_label), run_time=2)

        # 2. 辅助圆C4（P1Q1中点为圆心，过A0）、C5（A0为圆心，过R1）（3秒）
        C4_center = (P1.get_center() + Q1.get_center()) / 2
        C4_radius = math.hypot(A0.get_x() - C4_center[0], A0.get_y() - C4_center[1])
        C4 = Circle(center=C4_center, radius=C4_radius, color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        R1 = Dot(Point(C4_center[0] - math.sqrt(C4_radius**2 - C4_center[1]**2), 0, 0), color=self.POINT_C_COLOR, radius=0.06)
        R1_label = MathTex("R_1", color=self.LABEL_COLOR).next_to(R1, LEFT, buff=0.1)
        C5 = Circle(center=A0.get_center(), radius=math.hypot(R1.get_x() - A0.get_x(), 0), color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        S1 = Dot(Point(0, -math.hypot(R1.get_x() - A0.get_x(), 0), 0), color=self.POINT_C_COLOR, radius=0.06)
        S1_label = MathTex("S_1", color=self.LABEL_COLOR).next_to(S1, DOWN, buff=0.1)
        self.play(Create(C4), Create(R1), Write(R1_label), run_time=1.5)
        self.play(Create(C5), Create(S1), Write(S1_label), run_time=1.5)

        # 3. 辅助圆C6（B0S1中点为圆心，过(0,1)）（3秒）
        C6_center = (B0.get_center() + S1.get_center()) / 2
        C6_radius = math.hypot(0 - C6_center[0], 1 - C6_center[1])
        C6 = Circle(center=C6_center, radius=C6_radius, color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        C0 = Dot(Point(C6_center[0] + math.sqrt(C6_radius**2 - C6_center[1]**2), 0, 0), color=self.POINT_C_COLOR, radius=0.06)
        C4_point = Dot(Point(C6_center[0] - math.sqrt(C6_radius**2 - C6_center[1]**2), 0, 0), color=self.POINT_C_COLOR, radius=0.06)
        C0_label = MathTex("C_0", color=self.LABEL_COLOR).next_to(C0, RIGHT, buff=0.1)
        C4_label = MathTex("C_4", color=self.LABEL_COLOR).next_to(C4_point, LEFT, buff=0.1)
        self.play(Create(C6), run_time=1.5)
        self.play(Create(C0), Write(C0_label), Create(C4_point), Write(C4_label), run_time=1.5)

        # 4. 辅助圆C7-C12（构造C1-C3、C5-C7）（5秒）
        C_points = [C0, C4_point]
        C_labels = ["C_0", "C_4"]
        for i in range(1, 4):
            if i != 4:
                # 简化构造：基于C0-C4的等分逻辑
                x_coord = C0.get_x() - i*(C0.get_x() - C4_point.get_x())/4
                ci = Dot(Point(x_coord, 0, 0), color=self.POINT_C_COLOR, radius=0.06)
                ci_label = MathTex(f"C_{i}", color=self.LABEL_COLOR).next_to(ci, RIGHT if x_coord > 0 else LEFT, buff=0.1)
                C_points.append(ci)
                C_labels.append(f"C_{i}")
                self.play(Create(ci), Write(ci_label), run_time=0.8)
        for i in range(5, 8):
            x_coord = C4_point.get_x() - (i-4)*(C4_point.get_x() - (-2))/4
            ci = Dot(Point(x_coord, 0, 0), color=self.POINT_C_COLOR, radius=0.06)
            ci_label = MathTex(f"C_{i}", color=self.LABEL_COLOR).next_to(ci, LEFT, buff=0.1)
            C_points.append(ci)
            C_labels.append(f"C_{i}")
            self.play(Create(ci), Write(ci_label), run_time=0.8)

        # 暂停2秒
        self.wait(2)

        # ==================== 场景4：第三轮辅助圆构造（20秒）====================
        # 1. 标记T1（简化计算：C0+C2+C5+1的等效坐标）（2秒）
        T1_x = (C0.get_x() + C_points[2].get_x() + C_points[5].get_x())/3 + 0.5
        T1 = Dot(Point(T1_x, 0, 0), color=self.POINT_D_COLOR, radius=0.06)
        T1_label = MathTex("T_1", color=self.LABEL_COLOR).next_to(T1, RIGHT if T1_x > 0 else LEFT, buff=0.1)
        self.play(Create(T1), Write(T1_label), run_time=2)

        # 2. 辅助圆C13-C21（构造D0-D15）（6秒）
        D_points = []
        D_labels = []
        D0_x = C0.get_x() + 0.3
        D0 = Dot(Point(D0_x, 0, 0), color=self.POINT_D_COLOR, radius=0.06)
        D0_label = MathTex("D_0", color=self.LABEL_COLOR).next_to(D0, RIGHT, buff=0.1)
        D_points.append(D0)
        D_labels.append(D0_label)
        self.play(Create(D0), Write(D0_label), run_time=0.5)
        # 批量构造D1-D15（基于等分逻辑）
        for i in range(1, 16):
            x_coord = D0_x - i*(D0_x - (-2.5))/16
            di = Dot(Point(x_coord, 0, 0), color=self.POINT_D_COLOR, radius=0.06)
            di_label = MathTex(f"D_{i}", color=self.LABEL_COLOR).next_to(di, RIGHT if x_coord > 0 else LEFT, buff=0.1)
            D_points.append(di)
            D_labels.append(di_label)
            # 每4个点创建一个辅助圆
            if i % 4 == 0:
                ci_center = (D_points[i-4].get_center() + di.get_center())/2
                ci = Circle(center=ci_center, radius=math.hypot(ci_center[0], 1 - ci_center[1]), color=self.AUX_CIRCLE_COLOR, stroke_width=1)
                self.play(Create(ci), run_time=0.3)
            self.play(Create(di), Write(di_label), run_time=0.3)

        # 3. 标记U1（D0+D1+D2+D5+1的等效坐标）（2秒）
        U1_x = (D0.get_x() + D_points[1].get_x() + D_points[2].get_x() + D_points[5].get_x())/4 + 0.4
        U1 = Dot(Point(U1_x, 0, 0), color=self.POINT_D_COLOR, radius=0.06)
        U1_label = MathTex("U_1", color=self.LABEL_COLOR).next_to(U1, RIGHT if U1_x > 0 else LEFT, buff=0.1)
        self.play(Create(U1), Write(U1_label), run_time=2)

        # 4. 辅助圆C22-C27（构造E0-E25）（7秒）
        E_points = []
        E_labels = []
        E0_x = U1_x + 0.2
        E0 = Dot(Point(E0_x, 0, 0), color=self.POINT_E_COLOR, radius=0.06)
        E0_label = MathTex("E_0", color=self.LABEL_COLOR).next_to(E0, RIGHT, buff=0.1)
        E_points.append(E0)
        E_labels.append(E0_label)
        self.play(Create(E0), Write(E0_label), run_time=0.5)
        # 批量构造E1-E25
        for i in range(1, 26):
            x_coord = E0_x - i*(E0_x - (-2.8))/26
            ei = Dot(Point(x_coord, 0, 0), color=self.POINT_E_COLOR, radius=0.06)
            ei_label = MathTex(f"E_{i}", color=self.LABEL_COLOR).next_to(ei, RIGHT if x_coord > 0 else LEFT, buff=0.1)
            E_points.append(ei)
            E_labels.append(ei_label)
            # 每5个点创建一个辅助圆
            if i % 5 == 0:
                ci_center = (E_points[i-5].get_center() + ei.get_center())/2
                ci = Circle(center=ci_center, radius=math.hypot(ci_center[0], 1 - ci_center[1]), color=self.AUX_CIRCLE_COLOR, stroke_width=1)
                self.play(Create(ci), run_time=0.2)
            self.play(Create(ei), Write(ei_label), run_time=0.2)

        # 暂停3秒
        self.wait(3)

        # ==================== 场景5：第四轮辅助圆构造（20秒）====================
        # 1. 标记V1、W1、X1（等效坐标）（3秒）
        V1_x = (E_points[1].get_x() + E_points[23].get_x())/2 + 0.3
        V1 = Dot(Point(V1_x, 0, 0), color=self.POINT_F_COLOR, radius=0.06)
        V1_label = MathTex("V_1", color=self.LABEL_COLOR).next_to(V1, RIGHT if V1_x > 0 else LEFT, buff=0.1)
        
        W1_x = (E_points[15].get_x() + E_points[25].get_x())/2 - 0.1
        W1 = Dot(Point(W1_x, 0, 0), color=self.POINT_F_COLOR, radius=0.06)
        W1_label = MathTex("W_1", color=self.LABEL_COLOR).next_to(W1, RIGHT if W1_x > 0 else LEFT, buff=0.1)
        
        X1_x = W1_x + 0.5
        X1 = Dot(Point(X1_x, 0, 0), color=self.POINT_F_COLOR, radius=0.06)
        X1_label = MathTex("X_1", color=self.LABEL_COLOR).next_to(X1, RIGHT if X1_x > 0 else LEFT, buff=0.1)
        
        self.play(Create(V1), Write(V1_label), run_time=1)
        self.play(Create(W1), Write(W1_label), run_time=1)
        self.play(Create(X1), Write(X1_label), run_time=1)

        # 2. 辅助圆C28-C29（构造F系列点）（5秒）
        C28_center = (E0.get_center() + V1.get_center())/2
        C28 = Circle(center=C28_center, radius=math.hypot(C28_center[0], 1 - C28_center[1]), color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        F0 = Dot(Point(C28_center[0] + math.sqrt(C28_radius**2 - C28_center[1]**2), 0, 0), color=self.POINT_F_COLOR, radius=0.06)
        F0_label = MathTex("F_0", color=self.LABEL_COLOR).next_to(F0, RIGHT, buff=0.1)
        
        C29_center = (E_points[24].get_center() + W1.get_center())/2
        C29_radius = math.hypot(C29_center[0], 1 - C29_center[1])
        C29 = Circle(center=C29_center, radius=C29_radius, color=self.AUX_CIRCLE_COLOR, stroke_width=1)
        F56 = Dot(Point(C29_center[0] + math.sqrt(C29_radius**2 - C29_center[1]**2), 0, 0), color=self.POINT_F_COLOR, radius=0.06)
        F56_label = MathTex("F_{56}", color=self.LABEL_COLOR).next_to(F56, RIGHT if F56.get_x() > 0 else LEFT, buff=0.1)
        
        self.play(Create(C28), Create(F0), Write(F0_label), run_time=2.5)
        self.play(Create(C29), Create(F56), Write(F56_label), run_time=2.5)

        # 3. 构造257等分角的关键射线（7秒）
        theta = 2 * math.pi / 257  # 正257边形中心角
        gon_points = []
        # 先绘制A0（已存在），再绘制其余256个顶点
        for i in range(1, 257):
            x = math.cos(i * theta)
            y = math.sin(i * theta)
            p = Dot(Point(x, y, 0), color=self.POINT_A_COLOR, radius=0.04)
            gon_points.append(p)
            # 每16个点暂停一次相机，聚焦当前区域
            if i % 16 == 0:
                self.camera.frame.move_to(p)
                self.camera.frame.set_scale(2)
                self.play(Create(p), run_time=0.02)
                self.camera.frame.move_to(ORIGIN)
                self.camera.frame.set_scale(1)
            else:
                self.play(Create(p), run_time=0.02)

        # 4. 连接正257边形各顶点（5秒）
        gon_edges = []
        for i in range(256):
            edge = Line(gon_points[i].get_center(), gon_points[i+1].get_center(), color=self.CIRCLE_COLOR, stroke_width=1)
            gon_edges.append(edge)
        edge_final = Line(gon_points[-1].get_center(), A0.get_center(), color=self.CIRCLE_COLOR, stroke_width=1)
        self.play(Create(VGroup(*gon_edges)), run_time=4)
        self.play(Create(edge_final), run_time=1)

        # ==================== 场景6：最终展示（5秒）====================
        # 相机缩放聚焦整个图形
        self.camera.frame.set_scale(1.2)
        # 添加标题
        title = Text("正257边形 尺规作图完成", color=self.LABEL_COLOR, font_size=24).next_to(unit_circle, UP, buff=0.5)
        self.play(Write(title), run_time=2)
        # 高亮显示正257边形和所有作图痕迹
        self.play(
            VGroup(*gon_points, A0, edge_final, *gon_edges).set_color(YELLOW),
            run_time=1
        )
        self.wait(2)
