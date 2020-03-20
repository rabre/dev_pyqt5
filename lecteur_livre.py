import sqlite3

def requete():
    con = sqlite3.connect("testa.db")
    cur = con.cursor()
    #table=cur.execute("SELECT lecteur.nom,lire.ref FROM lecteur INNER JOIN lire ON lire.ID = lecteur.ID ") #Joindre deux table
    table=cur.execute("SELECT lecteur.nom,livre.titre FROM ((lire INNER JOIN lecteur ON lire.ID = lecteur.ID )INNER JOIN livre ON lire.ref=livre.ref )")# Mjooindre 3 Table
    for y in table:
        print(y)
    con.commit()
    con.close()

#Appel de la fonction
requete()
