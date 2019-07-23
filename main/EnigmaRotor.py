import main.Tools

class EnigmaRotor:

    def __init__(self, entrata, uscita, rotore_succ=None, flag=True):
        self.entrata=entrata.copy()
        self.uscita=uscita.copy()
        self.numeroSpostamenti=0
        self.flag=flag
        self.rotore_succ=rotore_succ

    #Imposta il rotore sull'elemento specificato: l'elemento comparirà in cima al vettore
    def impostaPosizione(self, elemento):
        self.numeroSpostamenti=0
        while(not(self.entrata[0].__eq__(elemento))):
            self.sposta()

    #Data la posizione nel vettore 'entrata', si cerca la lettera corrispondente nel vettore 'uscita' e si restituisce
    #la sua posizione
    def posizioneSinistra(self, posizione):
        return main.Tools.search(self.uscita, self.entrata[posizione])

    #Data la posizione nel vettore 'uscita', si cerca la lettera corrispondente nel vettore 'entrata' e si restituisce
    #la sua posizione
    def posizioneDestra(self, posizione):
        return main.Tools.search(self.entrata, self.uscita[posizione])

    #Sposta di una posizione gli elementi dei vettori
    def muovi(self):
        if self.flag==True:
            self.numeroSpostamenti=self.numeroSpostamenti+1
            self.sposta()
            if self.numeroSpostamenti>26 and not(self.rotore_succ is None):
                self.rotore_succ.muovi()
                self.numeroSpostamenti=0

    def sposta(self):
        elementoEntrata = self.entrata.pop(0)
        elementoUscita = self.uscita.pop(0)
        self.entrata.append(elementoEntrata)
        self.uscita.append(elementoUscita)

    def getEntrata(self):
        return self.entrata

    def getUscita(self):
        return self.uscita

    def __str__(self):
        return '{'+str(self.entrata)+', '+str(self.uscita)+'}'
