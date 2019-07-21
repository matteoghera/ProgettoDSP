import main.Tools

class EnigmaMachine:

    def __init__(self, riflettore, rotoreSinistro, rotoreCentrale, rotoreDestro, alfabeto, plugboard):
        self.riflettore=riflettore
        self.rotoreSinistro=rotoreSinistro
        self.rotoreCentrale=rotoreCentrale
        self.rotoreDestro=rotoreDestro
        self.alfabeto=alfabeto
        self.plugboard=plugboard

    def impostaEnigma(self, elementoRiflettore, elementoSinistro, elementoCentrale, elementoDestro):
        self.riflettore.impostaPosizione(elementoRiflettore)
        self.rotoreSinistro.impostaPosizione(elementoSinistro)
        self.rotoreCentrale.impostaPosizione(elementoCentrale)
        self.rotoreDestro.impostaPosizione(elementoDestro)

    def esegui(self, messaggio):
        messageChars=list(messaggio)
        result=[]
        for e in messageChars:
            posizioneIniziale=main.Tools.search(self.alfabeto, e)
            posizioneIniziale=self.plugboard[posizioneIniziale]
            posizioneFinale=self.calcolaPosizione(posizioneIniziale)
            posizioneFinale=self.plugboard[posizioneFinale]
            result.append(self.alfabeto[posizioneFinale])
        result="".join(str(x) for x in result)
        return result

    def calcolaPosizione(self, posizioneIniziale):
        posizione=self.rotoreDestro.posizioneSinistra(posizioneIniziale)
        posizione=self.rotoreCentrale.posizioneSinistra(posizione)
        posizione=self.rotoreSinistro.posizioneSinistra(posizione)
        posizione=self.riflettore.posizioneSinistra(posizione)

        #ritorno indietro
        posizione=self.rotoreSinistro.posizioneDestra(posizione)
        posizione=self.rotoreCentrale.posizioneDestra(posizione)
        posizione = self.rotoreDestro.posizioneDestra(posizione)
        self.rotoreDestro.muovi()
        return posizione
