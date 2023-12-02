import random 
from tkinter import *

Gui = Tk()
Gui.geometry("600x150")
Gui.title("Phrasomat")

class Phrasomat:
    def __init__(self) -> None:
        self.listeEins = ["verlässliche","erfolgsorientierte", "webbasierte", "allumfassende", "clevere","kundenorientierte", "pfadkritische", "dynamische", "konkurrenzlose","verteilte", "zielgerichtete"];
        self.listeZwei = ["gepowerte", "haftende","TG11.4-mäßige", "Mehrwert-", "zentrierte", "geclusterte", "proaktive", "Out-Of-The-Box-","positionierte", "vernetzte", "fokussierte", "kraftvolle","geordnete", "geteilte", "kooperative", "Multi-Tier-", "Frontend-", "Enterprise-"];
        self.listeDrei = ["Schicht", "Endstufe", "Lösung", "Architektur", "Kernkompetenz", "Strategie", "Koopereation", "Ausrichtung", "Räumlichkeit", "Vision", "Dimension", "Mission"];
        self.einsLänge = 0
        self.zweiLänge = 0 
        self.dreiLänge = 0

        self.satzBilden = Button(master=Gui, text="Ich bilde einen Satz", command=self.satzBilden)
        self.label1 = Label(master=Gui, text="Drücke: Ich bilde einen Satz um einen Satz zu bilden")

        self.satzBilden.place(x=25,y=25,width=550, height=50)
        self.label1.place(x=25,y=85,width=550, height=50)

    def run(self):
        Gui.mainloop()
    
    def lenght(self):
        self.einsLänge = len(self.listeEins)-1
        self.zweiLänge = len(self.listeZwei)-1  
        self.dreiLänge = len(self.listeDrei)-1
    
    def satzBilden(self):
        self.lenght()
        self.wortEins = random.randint(0,self.einsLänge)
        self.wortZwei = random.randint(0,self.zweiLänge)
        self.wortDrei = random.randint(0,self.dreiLänge)

        self.phrase = self.listeEins[self.wortEins] +" "+ self.listeDrei[self.wortZwei] +" "+ self.listeDrei[self.wortDrei]
        self.label1.configure(text="Was wir brauchen ist eine"+ " " + self.phrase)
        print("Was wir brauchen ist eine"+ " " + self.phrase)

Satz1= Phrasomat()
Satz1.run()
