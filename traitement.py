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
import matplotlib.pyplot as plt
import pymysql

class Fenetre3(QMainWindow):
    def __init__(self):
        super(Fenetre3, self).__init__()
        self.setWindowTitle("Gestion de Bibliotheque")
        self.resize(400,500)
        self.setWindowIcon(QIcon("book.ico"))
        self.setStyleSheet("QWidget{background:#e6ecff}")

        #creation responsive
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        #lancement plot
        self.lance_plot()
        self.toolbar = NavigationToolbar(self.canvas,self.canvas)


         # Tablewidget
        self.table1 = QTableWidget(self.centralWidget)
        self.table1.setRowCount(2)
        self.table1.setColumnCount(2)
        #definir le nom de la colonne
        self.table1.setHorizontalHeaderLabels(['NOM','TITRE'])

        #bouton
        #self.btn1 = QPushButton("INSERER",self.centralWidget)
        #style css bouton




        #Layout
        qhboxlayout = QHBoxLayout()




        qvboxlayout = QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)


        qvboxlayout.addWidget(self.table1)
        qvboxlayout.addWidget(self.canvas)
        qvboxlayout.addWidget(self.toolbar)
        #qvboxlayout.addWidget(self.btn1)
        # appel Click
        #self.btn1.clicked.connect(self.click)
        #Appel affichage tableau
        self.requete_affichage()

    #requete affichage
    def requete_affichage(self):
        con = sqlite3.connect("biblio.db")
        res = con.execute("SELECT lecteur.nom,livre.titre FROM ((lire INNER JOIN lecteur ON lire.ID = lecteur.ID )INNER JOIN livre ON lire.ref=livre.ref )")
        self.table1.setRowCount(0)
        for y1, y2 in enumerate(res):
            self.table1.insertRow(y1)
            for x1, x2 in enumerate(y2):
                self.table1.setItem(y1, x1, QTableWidgetItem(str(x2)))
        con.close()
    def lance_plot(self):
        self.canvas=Graphe()
        self.show()

class Graphe(FigureCanvas):
    def __init__(self,parent=None):
        self.fig = Figure()
        self.plt = self.fig.subplots()
        self.fig = plt.Figure()

        FigureCanvas.__init__(self,self.fig)

        self.setParent(parent)
        self.requete_graphe()

    def requete_graphe(self):
        x = []
        y = []
        with sqlite3.connect("testa.db") as con:
            cur = con.cursor()
            cur.execute("SELECT id,count(*) FROM lire GROUP BY (id)")
            for lecteur,livre in cur.fetchall():
                x.append(lecteur)
                y.append(livre)
        self.plt=self.fig.add_subplot(111,projection='3d')
        a = x
        b = y

        self.plt.plot(x,y,label="Nombre de lecture de livre",alpha = 0.8,
                      color='blue',linestyle='dotted',linewidth=4,
                      marker='o',markersize=10,markerfacecolor='aqua',
                      markeredgecolor = 'red')
        self.plt.legend()




