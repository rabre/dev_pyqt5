#Projet de Gedtion de Bibliotheque versus Lecteur
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import numpy as np
from lecteur import *
from livre import *
from traitement import *
from lire import *

import matplotlib.pyplot as plt


#Creation de la classe pour Interface
class Fenetre(QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.window = QWidget()
        self.window.setWindowTitle("Gestion de Bibliotheque")
        self.window.resize(200,300)
        self.window.setWindowIcon(QIcon("boky.ico"))
        self.window.setStyleSheet("QWidget{background:#e6ecff}")


        #creation responsive
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #CCreation de Bouton QPushboyuton
        self.btn1 = QPushButton("Ajout Lecteur",self.centralWidget)
        self.btn2 = QPushButton("Ajout Livre",self.centralWidget)
        self.btn4 = QPushButton("lire", self.centralWidget)
        self.btn3 = QPushButton("Traitement", self.centralWidget)

        #style css bouton

        self.btn1.setStyleSheet("QWidget{background:#00cccc;}")
        self.btn2.setStyleSheet("QWidget{background:#00cccc;}")
        self.btn4.setStyleSheet("QWidget{background:#00cccc;}")
        self.btn3.setStyleSheet("QWidget{background:#99b3ff;}")


        #Layout
        qhboxlayout = QHBoxLayout()
        qvboxlayout = QVBoxLayout(self.window)
        qvboxlayout.addLayout(qhboxlayout)

        #add centralwidget
        qvboxlayout.addWidget(self.btn1)
        qvboxlayout.addWidget(self.btn2)
        qvboxlayout.addWidget(self.btn4)
        qvboxlayout.addWidget(self.btn3)

        #
        qvboxlayout = QHBoxLayout(self.window)
        qvboxlayout.addLayout(qhboxlayout)
        #appele le click
        self.btn1.clicked.connect(self.click)
        self.btn2.clicked.connect(self.click_livre)
        self.btn4.clicked.connect(self.clck_lire)
        self.btn3.clicked.connect(self.click_traitement)

        self.window.show()

    #fonction click
    def click(self):
        self.appel1 =Fenetre1()
        #print("Ok Bouton")
    def click_livre(self):
        self.livre = Fenetre2()

    def clck_lire(self):
        self.lire = Fenetre4()

    def click_traitement(self):
        self.traitement =Fenetre3()



#Affichage de l'interface
app= QApplication.instance()

if not app:
    app = QApplication(sys.argv)

#Lancement de fonction/Classe
fenetre = Fenetre()
#fenetre.show()
app.exec_()
