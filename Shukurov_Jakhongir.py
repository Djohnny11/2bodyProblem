from vpython import *
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class GravitationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the width and height input boxes
        m1_label = QLabel("Масса тело 1:")
        self.m1_input = QLineEdit()
       
        m2_label = QLabel("Масса тело 2:")
        self.m2_input = QLineEdit()
        
        v_label = QLabel("Начальная скорость:")
        self.v_input = QLineEdit()
       
        rdist_label = QLabel("Расстояние между телами:")
        self.rdist_input = QLineEdit()
        
        radius1_label = QLabel("Радиус тело 1:")
        self.radius1_input = QLineEdit()
        
        radius2_label = QLabel("Радиус тело 2:")
        self.radius2_input = QLineEdit()

       

        # Create the "Start" button
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.startSimulation)

        # Create the vertical layout and add the widgets to it
        layout = QVBoxLayout()

        layout.addWidget(m1_label)
        layout.addWidget(self.m1_input)

        layout.addWidget(m2_label)
        layout.addWidget(self.m2_input)

        layout.addWidget(v_label)
        layout.addWidget(self.v_input)

        layout.addWidget(rdist_label)
        layout.addWidget(self.rdist_input)

        layout.addWidget(radius1_label)
        layout.addWidget(self.radius1_input)

        layout.addWidget(radius2_label)
        layout.addWidget(self.radius2_input)

        layout.addWidget(start_button)

        self.setLayout(layout)


    def startSimulation(self):
        G=6.67e-11

        m1_string=self.m1_input.text()         
        m1=float(m1_string)                      
        
        m2_string = self.m2_input.text()
        m2 = float(m2_string)

        v_string = self.v_input.text()
        v = float(v_string)

        rdist_string = self.rdist_input.text()
        rdist = float(rdist_string)

        radius1_string = self.radius1_input.text()
        radius1 = float(radius1_string)

        radius2_string = self.radius2_input.text()
        radius2 = float(radius2_string)


        M=m1+m2
        x1=-(m2/M)*rdist
        x2=(m1/M)*rdist

        star1=sphere(pos=vector(x1,0,0), radius=radius1, color=color.green, make_trail=True)
        star2=sphere(pos=vector(x2,0,0),radius=radius2, color=color.white, make_trail=True, trail_color=color.yellow)
        # Rcom=(star1.pos*m1+star2.pos*m2)/M
        r = star2.pos - star1.pos



        time.sleep(1)





        v1circle=sqrt(G*m2*mag(star1.pos)/mag(r)**2+v)
        # v1circle=sqrt(G*m1/rdist)


        star1.v=vector(0,v1circle,0)
        star1.p=m1*star1.v
        star2.p=-star1.p


        t=0
        dt=100
        time.sleep(1)
        while t<1e20:
            rate(10000)
            r=star2.pos-star1.pos
            F2=-G*m1*m2*norm(r)/mag(r)**2
            star2.p=star2.p+F2*dt
            star1.p=star1.p-F2*dt
            star1.pos=star1.pos+star1.p*dt/m1
            star2.pos=star2.pos+star2.p*dt/m2
            t=t+dt


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GravitationGUI()
    ex.show()
    sys.exit(app.exec_())



        # для земли и луны
        #m1=6e24
        # m2=7e22
        #v=10 траектория круг
        #rdist=384467000
        # radius1=6371000
        # radius2=1737100
        