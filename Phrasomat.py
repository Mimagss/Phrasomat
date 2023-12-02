import random 

class Phrasomat:
    def __init__(self) -> None:
        self.listeEins = ["verlässliche","erfolgsorientierte", "webbasierte", "allumfassende", "clevere","kundenorientierte", "pfadkritische", "dynamische", "konkurrenzlose","verteilte", "zielgerichtete"];
        self.listeZwei = ["gepowerte", "haftende","TG11.4-mäßige", "Mehrwert-", "zentrierte", "geclusterte", "proaktive", "Out-Of-The-Box-","positionierte", "vernetzte", "fokussierte", "kraftvolle","geordnete", "geteilte", "kooperative", "Multi-Tier-", "Frontend-", "Enterprise-"];
        self.listeDrei = ["Schicht", "Endstufe", "Lösung", "Architektur", "Kernkompetenz", "Strategie", "Koopereation", "Ausrichtung", "Räumlichkeit", "Vision", "Dimension", "Mission"];
        
        self.einsLänge = 0
        self.zweiLänge = 0 
        self.dreiLänge = 0
    
    def lenght(self):
        self.einsLänge = len(self.listeEins)-1
        self.zweiLänge = len(self.listeZwei)-1  
        self.dreiLänge = len(self.listeDrei)-1
        return self.einsLänge,self.zweiLänge,self.dreiLänge
    
    def würfle(self):
        self.wortEins = random.randint(0,self.einsLänge)
        self.wortZwei = random.randint(0,self.zweiLänge)
        self.wortDrei = random.randint(0,self.dreiLänge)

        self.phrase = self.listeEins[self.wortEins] +" "+ self.listeDrei[self.wortZwei] +" "+ self.listeDrei[self.wortDrei]
        return "Was wir brauchen ist eine " + self.phrase

Satz1= Phrasomat()
Satz1.lenght()
satz = Satz1.würfle()
print(satz)
