class Studente:
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
        
    def classificazione(self):
        if 14 <= self.età <= 16:
            return "Biennio"
        if 17 <= self.età <= 19:
            return "Triennio"
        
        return "Nessuno dei due"
    
    def __str__(self):
        return f"{self.nome} {self.cognome} età: {self.età} ({self.residenza})"
    
class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []
        
    def aggiungi_studente(self, studente):
        return self.studenti.append(self.studente)
    
    def cerca_per_cognome(self, cognome):
        for studente in self.studenti:
            if studente.cognome == self.cognome:
                return studente
        return None
    
    def cerca_per_età(self, età):
        for studente in self.studenti:
            if studente.età == self.età:
                return studente
        return None
    
    def conteggio(self):
        return len(self.studenti)
    
    
    