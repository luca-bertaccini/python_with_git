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