from manim import *  #导入manim库
import math as m
config.verbosity = "WARNING" #设置警告等级,默认为"WARNING",可设置为"DEBUG","INFO","WARNING","ERROR","CRITICAL"

##define some functions brfore the class
##分别是 椭圆锥面、椭球面、单叶双曲面、双叶双曲面、椭圆抛物面、双曲抛物面

#Add an axis function,the axis is a 3D axis
def Add3DAxis(self,mov_num=0): #mov_num is the position of the axis
    axis = ThreeDAxes(         #Create a 3D axis
        x_length=7,            #The length of x axis
        y_length=7,            #The length of y axis
        z_length=7,            #The length of z axis
        x_range=[-8, 8],       #The range of x axis
        y_range=[-8, 8],       #The range of y axis
        z_range=[-8, 8],       #The range of z axis
        axis_config={"color": WHITE},            #The color of the axis,here is white
    ).set_opacity(0.5).shift(Z_AXIS*mov_num)     #Set the opacity of the axis and the position of the axis
    x_label = axis.get_x_axis_label("x").set_color(LIGHT_PINK)   #Set the color of the x label,here is light pink
    y_label = axis.get_y_axis_label("y").set_color(LIGHT_PINK)   #Set the color of the y label,here is light pink
    z_label = axis.get_z_axis_label("z").set_color(PINK)         #Set the color of the z label,here is pink
    self.play(DrawBorderThenFill(axis),Write(x_label),Write(y_label),Write(z_label))  #Draw the axis and write the labels

##椭圆锥面
def EllipticCone(self,mov_num=0):                 #mov_num is the position of the surface
    a1,b1 = ValueTracker(1),ValueTracker(1)       #a1 and b1 are the value trackers of a and b
    a1_label = Text("a=").to_edge(UL)             #a1_label is the label of a
    b1_label = Text("b=").next_to(a1_label,DOWN)  #b1_label is the label of b
    a1_num = always_redraw(lambda :               
        DecimalNumber(a1.get_value(),num_decimal_places=2).next_to(a1_label,RIGHT).set_color(LIGHT_PINK),
    )                                            #a1_num is the number of a,always redraw
    b1_num = always_redraw(lambda :
        DecimalNumber(b1.get_value(),num_decimal_places=2).next_to(b1_label,RIGHT).set_color(LIGHT_PINK),
    )                                            #b1_num is the number of b,always redraw
    suff = VGroup(a1_label,a1_num,b1_label,b1_num) #suff is the group of a1_label,a1_num,b1_label,b1_num
    box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5) #box1 is the rectangle of suff
    math = MathTex(r"\frac{x^2}{a^2}+\frac{y^2}{b^2}=z^2").set_color(LIGHT_PINK) #math is the formula of the elliptic cone
    illustration = Text("椭圆锥面",font="YEFONTQingSeQingShuTi").shift(UP*1.5) #illustration is the title of the elliptic cone
    box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5) #box2 is the rectangle of the illustration
    graph = always_redraw(lambda : Surface(      #graph is the surface of the elliptic cone
        lambda u,v: np.array([                   #The formula of the elliptic cone
            a1.get_value()*u*m.cos(v),           #x=a*cos(v)
            b1.get_value()*u*m.sin(v),           #y=b*sin(v)
            u                                    #z=u
        ]),
        u_range=[-3,3],v_range=[0,2*PI],         #The range of u and v
        checkerboard_colors={None,None},         #The color of the surface
        stroke_color=LIGHT_PINK,                 #The color of the stroke
        stroke_width=1,                          #The width of the stroke
        fill_opacity=0.5,                        #The opacity of the surface
        resolution=(18,18)                       #The resolution of the surface
    ).shift(Z_AXIS*mov_num))                     #The position of the surface
    self.play(Write(illustration),run_time=1.5)  #Write the illustration
    self.play(Create(box2))                      #Create the box2
    self.play(ReplacementTransform(box2,math))   #Replace the box2 with the math
    self.wait(1)                  
    self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1)) #Fade out the illustration,move the math to the edge of the right up, scale the math,create the suff and box1
    self.add_fixed_in_frame_mobjects(suff,box1,math) #Add the suff and box1 to the frame
    self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES) #Set the camera orientation
    Add3DAxis(self,mov_num)                                      #Add the 3D axis
    self.begin_ambient_camera_rotation(rate=0.3)                 #Begin the ambient camera rotation
    self.play(Create(graph))                                     #Create the graph
    self.move_camera(zoom=0.8)                                   #Move the camera
    self.play(Indicate(a1_label[0]))                             #Indicate the a1_label
    self.play(a1.animate.set_value(3),run_time=2)                #Change the value of a1
    self.play(a1.animate.set_value(1),run_time=1)                #Change the value of a1
    self.play(Indicate(b1_label[0]))                             #Indicate the b1_label
    self.play(b1.animate.set_value(3),run_time=2)                #Change the value of b1
    self.play(b1.animate.set_value(1),run_time=1)                #Change the value of b1
    self.stop_ambient_camera_rotation()                          #Stop the ambient camera rotation
    self.wait(0.5)
    self.clear()                                                 #Clear the screen
    self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES) #Set the camera orientation
    pass                                                         #End the function,the following functions are the same,如法炮制,没啥好说的^_^

##椭圆抛物面
def EllipticParaboloid(self,mov_num=0):
        a2,b2 = ValueTracker(1),ValueTracker(1)
        a2_label = Text("a=").to_edge(UL)
        b2_label = Text("b=").next_to(a2_label,DOWN)
        a2_num = always_redraw(lambda :
            DecimalNumber(a2.get_value(),num_decimal_places=2).next_to(a2_label,RIGHT).set_color(LIGHT_PINK),
        )
        b2_num = always_redraw(lambda :
            DecimalNumber(b2.get_value(),num_decimal_places=2).next_to(b2_label,RIGHT).set_color(LIGHT_PINK),
        )
        suff = VGroup(a2_label,a2_num,b2_label,b2_num)
        box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
        math = MathTex(r"\frac{x^2}{a^2}+\frac{y^2}{b^2}=z").set_color(LIGHT_PINK)
        illustration = Text("椭圆抛物面",font="YEFONTQingSeQingShuTi").shift(UP*1.5)
        box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
        graph = always_redraw(lambda : Surface(
            lambda u,v: np.array([
                a2.get_value()*u*m.cos(v),     #x=a*cos(v)
                b2.get_value()*u*m.sin(v),     #y=b*sin(v)
                u**2                           #z=u^2
            ]),
            u_range=[-2,2],v_range=[0,2*PI],
            checkerboard_colors={None,None},
            stroke_color=LIGHT_PINK,
            stroke_width=1,
            fill_opacity=0.5,
            resolution=(18,18)
        ).shift(Z_AXIS*mov_num))
        self.play(Write(illustration),run_time=1.5)
        self.play(Create(box2))
        self.play(ReplacementTransform(box2,math))
        self.wait(1)
        self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1))
        self.add_fixed_in_frame_mobjects(suff,box1,math)
        self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES)
        Add3DAxis(self,mov_num)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(graph))
        self.play(Indicate(a2_label[0]))
        self.play(a2.animate.set_value(3),run_time=2)
        self.play(a2.animate.set_value(1),run_time=1)
        self.play(Indicate(b2_label[0]))
        self.play(b2.animate.set_value(3),run_time=2)
        self.play(b2.animate.set_value(1),run_time=1)
        self.stop_ambient_camera_rotation()
        self.wait(0.5)
        self.clear()
        self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES)
        pass

##椭球面
def Ellipsoid(self,mov_num=0):
    a3,b3,c3 = ValueTracker(1),ValueTracker(1),ValueTracker(1)
    a3_label = Text("a=").to_edge(UL)
    b3_label = Text("b=").next_to(a3_label,DOWN)
    c3_label = Text("c=").next_to(b3_label,DOWN)
    a3_num = always_redraw(lambda :
        DecimalNumber(a3.get_value(),num_decimal_places=2).next_to(a3_label,RIGHT).set_color(LIGHT_PINK),
    )
    b3_num = always_redraw(lambda :
        DecimalNumber(b3.get_value(),num_decimal_places=2).next_to(b3_label,RIGHT).set_color(LIGHT_PINK),
    )
    c3_num = always_redraw(lambda :
        DecimalNumber(c3.get_value(),num_decimal_places=2).next_to(c3_label,RIGHT).set_color(LIGHT_PINK),
    )
    suff = VGroup(a3_label,a3_num,b3_label,b3_num,c3_label,c3_num)
    box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    math = MathTex(r"\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1").set_color(LIGHT_PINK)
    illustration = Text("椭球面",font="YEFONTQingSeQingShuTi").shift(UP*1.5)
    box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    graph = always_redraw(lambda : Surface(
        lambda u,v: np.array([
            a3.get_value()*m.cos(u)*m.sin(v),  #x=a*cos(u)*sin(v)
            b3.get_value()*m.sin(u)*m.sin(v),  #y=b*sin(u)*sin(v)
            c3.get_value()*m.cos(v)            #z=c*cos(v)
        ]),
        u_range=[0,2*PI],v_range=[0,PI],
        checkerboard_colors={None,None},
        stroke_color=LIGHT_PINK,
        stroke_width=1,
        fill_opacity=0.5,
        resolution=(18,18)
    ).shift(Z_AXIS*mov_num))
    self.play(Write(illustration),run_time=1.5)
    self.play(Create(box2))
    self.play(ReplacementTransform(box2,math))
    self.wait(1)
    self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1))
    self.add_fixed_in_frame_mobjects(suff,box1,math)
    self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES)
    Add3DAxis(self,mov_num)
    self.begin_ambient_camera_rotation(rate=0.3)
    self.play(Create(graph))
    self.play(Indicate(a3_label[0]))
    self.play(a3.animate.set_value(3),run_time=2)
    self.play(a3.animate.set_value(1),run_time=1)
    self.play(Indicate(b3_label[0]))
    self.play(b3.animate.set_value(3),run_time=2)
    self.play(b3.animate.set_value(1),run_time=1)
    self.play(Indicate(c3_label[0]))
    self.play(c3.animate.set_value(3),run_time=2)
    self.play(c3.animate.set_value(1),run_time=1)
    self.stop_ambient_camera_rotation()
    self.wait(0.5)
    self.clear()
    self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES)
    pass

##双曲抛物面
def HyperbolicParaboloid(self,mov_num=0):
    a4,b4 = ValueTracker(1),ValueTracker(1)
    a4_label = Text("a=").to_edge(UL)
    b4_label = Text("b=").next_to(a4_label,DOWN)
    a4_num = always_redraw(lambda :
        DecimalNumber(a4.get_value(),num_decimal_places=2).next_to(a4_label,RIGHT).set_color(LIGHT_PINK),
    )
    b4_num = always_redraw(lambda :
        DecimalNumber(b4.get_value(),num_decimal_places=2).next_to(b4_label,RIGHT).set_color(LIGHT_PINK),
    )
    suff = VGroup(a4_label,a4_num,b4_label,b4_num)
    box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    math = MathTex(r"\frac{x^2}{a^2}-\frac{y^2}{b^2}=z").set_color(LIGHT_PINK)
    illustration = Text("双曲抛物面",font="YEFONTQingSeQingShuTi").shift(UP*1.5)
    box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    graph = always_redraw(lambda : Surface(
        lambda u,v: np.array([
            u,                                          #x=u
            v,                                          #y=v
            a4.get_value()*u**2-b4.get_value()*v**2     #z=a*u^2-b*v^2
        ]),
        u_range=[-2,2],v_range=[-2,2],
        checkerboard_colors={None,None},
        stroke_color=LIGHT_PINK,
        stroke_width=1,
        fill_opacity=0.5,
        resolution=(18,18)
    ).shift(Z_AXIS*mov_num))
    self.play(Write(illustration),run_time=1.5)
    self.play(Create(box2))
    self.play(ReplacementTransform(box2,math))
    self.wait(1)
    self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1))
    self.add_fixed_in_frame_mobjects(suff,box1,math)
    self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES)
    Add3DAxis(self,mov_num)
    self.begin_ambient_camera_rotation(rate=0.3)
    self.play(Create(graph))
    self.play(Indicate(a4_label[0]))
    self.play(a4.animate.set_value(3),run_time=2)
    self.play(a4.animate.set_value(1),run_time=1)
    self.play(Indicate(b4_label[0]))
    self.play(b4.animate.set_value(3),run_time=2)
    self.play(b4.animate.set_value(1),run_time=1)
    self.stop_ambient_camera_rotation()
    self.wait(0.5)
    self.clear()
    self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES)
    pass

##单叶双曲面
def HyperboloidOfOneSheet(self,mov_num=0):
    a5,b5,c5 = ValueTracker(1),ValueTracker(1),ValueTracker(1)
    a5_label = Text("a=").to_edge(UL)
    b5_label = Text("b=").next_to(a5_label,DOWN)
    c5_label = Text("c=").next_to(b5_label,DOWN)
    a5_num = always_redraw(lambda :
        DecimalNumber(a5.get_value(),num_decimal_places=2).next_to(a5_label,RIGHT).set_color(LIGHT_PINK),
    )
    b5_num = always_redraw(lambda :
        DecimalNumber(b5.get_value(),num_decimal_places=2).next_to(b5_label,RIGHT).set_color(LIGHT_PINK),
    )
    c5_num = always_redraw(lambda :
        DecimalNumber(c5.get_value(),num_decimal_places=2).next_to(c5_label,RIGHT).set_color(LIGHT_PINK),
    )
    suff = VGroup(a5_label,a5_num,b5_label,b5_num,c5_label,c5_num)
    box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    math = MathTex(r"\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1").set_color(LIGHT_PINK)
    illustration = Text("单叶双曲面",font="YEFONTQingSeQingShuTi").shift(UP*1.5)
    box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    graph = always_redraw(lambda : Surface(
        lambda u,v: np.array([
            a5.get_value()*m.cosh(u)*m.cos(v),  #x=a*cosh(u)*cos(v)
            b5.get_value()*m.cosh(u)*m.sin(v),  #y=b*cosh(u)*sin(v)
            c5.get_value()*m.sinh(u)            #z=c*sinh(u)
        ]),
        u_range=[-2,2],v_range=[0,2*PI],
        checkerboard_colors={None,None},
        stroke_color=LIGHT_PINK,
        stroke_width=1,
        fill_opacity=0.5,
        resolution=(18,18)
    ).shift(Z_AXIS*mov_num))
    self.play(Write(illustration),run_time=1.5)
    self.play(Create(box2))
    self.play(ReplacementTransform(box2,math))
    self.wait(1)
    self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1))
    self.add_fixed_in_frame_mobjects(suff,box1,math)
    self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES)
    Add3DAxis(self,mov_num)
    self.begin_ambient_camera_rotation(rate=0.3)
    self.play(Create(graph))
    self.move_camera(zoom=0.8)
    self.play(Indicate(a5_label[0]))
    self.play(a5.animate.set_value(3),run_time=2)
    self.play(a5.animate.set_value(1),run_time=1)
    self.play(Indicate(b5_label[0]))
    self.play(b5.animate.set_value(3),run_time=2)
    self.play(b5.animate.set_value(1),run_time=1)
    self.play(Indicate(c5_label[0]))
    self.play(c5.animate.set_value(3),run_time=2)
    self.play(c5.animate.set_value(1),run_time=1)
    self.stop_ambient_camera_rotation()
    self.wait(0.5)
    self.clear()
    self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES)
    pass

##双叶双曲面
def HyperboloidOfTwoSheets(self,mov_num=0):
    a6,b6,c6 = ValueTracker(1),ValueTracker(1),ValueTracker(1)
    a6_label = Text("a=").to_edge(UL)
    b6_label = Text("b=").next_to(a6_label,DOWN)
    c6_label = Text("c=").next_to(b6_label,DOWN)
    a6_num = always_redraw(lambda :
        DecimalNumber(a6.get_value(),num_decimal_places=2).next_to(a6_label,RIGHT).set_color(LIGHT_PINK),
    )
    b6_num = always_redraw(lambda :
        DecimalNumber(b6.get_value(),num_decimal_places=2).next_to(b6_label,RIGHT).set_color(LIGHT_PINK),
    )
    c6_num = always_redraw(lambda :
        DecimalNumber(c6.get_value(),num_decimal_places=2).next_to(c6_label,RIGHT).set_color(LIGHT_PINK),
    )
    suff = VGroup(a6_label,a6_num,b6_label,b6_num,c6_label,c6_num)
    box1 = SurroundingRectangle(suff,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    math = MathTex(r"\frac{x^2}{a^2}-\frac{y^2}{b^2}-\frac{z^2}{c^2}=1").set_color(LIGHT_PINK)
    illustration = Text("双叶双曲面",font="YEFONTQingSeQingShuTi").shift(UP*1.5)
    box2 = SurroundingRectangle(illustration,stroke_color=LIGHT_PINK,corner_radius=0).set_opacity(0.5)
    graph1 = always_redraw(lambda : Surface(
        lambda u,v: np.array([
            a6.get_value()*m.cosh(u),                #x=a*cosh(u)
            b6.get_value()*m.sinh(u)*m.sin(v),       #y=b*sinh(u)*sin(v)
            c6.get_value()*m.sinh(u)*m.cos(v)        #z=c*sinh(u)*cos(v)
        ]),
        u_range=[-2,2],v_range=[0,2*PI],
        checkerboard_colors={None,None},
        stroke_color=LIGHT_PINK,
        stroke_width=1,
        fill_opacity=0.5,
        resolution=(18,18)
    ).shift(Z_AXIS*mov_num))
    graph2 = always_redraw(lambda : Surface(
        lambda u,v: np.array([
            -a6.get_value()*m.cosh(u),
            b6.get_value()*m.sinh(u)*m.sin(v),
            c6.get_value()*m.sinh(u)*m.cos(v)
        ]),
        u_range=[-2,2],v_range=[0,2*PI],
        checkerboard_colors={None,None},
        stroke_color=LIGHT_PINK,
        stroke_width=1,
        fill_opacity=0.5,
        resolution=(18,18)
    ).shift(Z_AXIS*mov_num))
    self.play(Write(illustration),run_time=1.5)
    self.play(Create(box2))
    self.play(ReplacementTransform(box2,math))
    self.wait(1)
    self.play(FadeOut(illustration),math.animate.to_edge(UR).scale(0.7),Create(suff),Create(box1))
    self.add_fixed_in_frame_mobjects(suff,box1,math)
    self.set_camera_orientation(phi=75*DEGREES,theta=30*DEGREES)
    Add3DAxis(self,mov_num)
    self.begin_ambient_camera_rotation(rate=0.3)
    self.play(Create(graph1),Create(graph2))
    self.move_camera(zoom=0.8)
    self.play(Indicate(a6_label[0]))
    self.play(a6.animate.set_value(3),run_time=2)
    self.play(a6.animate.set_value(1),run_time=1)
    self.play(Indicate(b6_label[0]))
    self.play(b6.animate.set_value(3),run_time=2)
    self.play(b6.animate.set_value(1),run_time=1)
    self.play(Indicate(c6_label[0]))
    self.play(c6.animate.set_value(3),run_time=2)
    self.play(c6.animate.set_value(1),run_time=1)
    self.stop_ambient_camera_rotation()
    self.wait(0.5)
    self.clear()
    self.set_camera_orientation(phi=0*DEGREES,theta=-90*DEGREES)
    pass

##Write a Scnen for start
def StartScene(self):  
    start = Text("本视频将介绍几种常见的二次曲面",font="YEFONTQingSeQingShuTi").scale(0.8).shift(UP*2).set_color(LIGHT_PINK) 
    start2 = Text("椭圆锥面、椭球面",font="YEFONTQingSeQingShuTi").scale(0.8).next_to(start,DOWN)
    start3 = Text("椭圆抛物面、双曲抛物面",font="YEFONTQingSeQingShuTi").scale(0.8).next_to(start2,DOWN)
    start4 = Text("单叶双曲面、双叶双曲面",font="YEFONTQingSeQingShuTi").scale(0.8).next_to(start3,DOWN)
    self.play(Write(start),run_time=1.5)
    self.wait(0.5)
    self.play(Write(start2),Write(start3),Write(start4),run_time=1.5)
    self.wait(1.5)
    self.play(FadeOut(start),FadeOut(start2),FadeOut(start3),FadeOut(start4))
    pass

##Write a Scnen for end
def EndScene(self):
    a = ValueTracker(0)   
    plane = NumberPlane().set_opacity(0.3) 
    graph1 = always_redraw(lambda : plane.plot(
        lambda x: x**(2/3)+0.9*m.sqrt(3.3-x**2  if 3.3-x**2 >= 0 else 0)*m.sin(a.get_value()*PI*x), #左半心形震荡图像
        x_range=[0,1.8],
        color=LIGHT_PINK
    ))
    graph2 = always_redraw(lambda : plane.plot(
        lambda x: (-x)**(2/3)+0.9*m.sqrt(3.3-x**2  if 3.3-x**2 >= 0 else 0)*m.sin(a.get_value()*PI*(-x)), #右半心形震荡图像
        x_range=[-1.8,0],
        color=LIGHT_PINK
    ))
    end = Text("END",font="YEFONTQingSeQingShuTi").scale(1.5).set_color(LIGHT_PINK).next_to(ORIGIN,DOWN*5).set_opacity(0.7)
    self.play(DrawBorderThenFill(plane))
    #self.play(plane.animate.set_opacity(0.3))
    self.play(Create(graph1),Create(graph2))
    self.play(a.animate.set_value(5.5),run_time=3)
    self.play(Write(end))
    self.wait(1)


class Test(ThreeDScene):  #定义一个类，继承ThreeDScene，封装所有的图像函数
    def construct(self):
        StartScene(self)               #调用开始场景
        EllipticCone(self,0)           #调用椭圆锥面
        EllipticParaboloid(self,-2.2)  #调用椭圆抛物面，-2.2是位置
        Ellipsoid(self,0)              #调用椭球面
        HyperbolicParaboloid(self,0)   #调用双曲抛物面
        HyperboloidOfOneSheet(self,0)  #调用单叶双曲面
        HyperboloidOfTwoSheets(self,0) #调用双叶双曲面
        EndScene(self)                 #调用结束场景
        pass
