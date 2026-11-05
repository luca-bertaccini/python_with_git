class RegistroVoti:
    def __init__(self):
        self.voti = []
        
    def aggiungi_voto(self, voto):
        if not 0 < voto <= 10:
            raise ValueError("Voto non valido")
        self.voti.append(voto)
        
    def media(self):
        if len(self.voti) == 0:
            raise ValueError("Il registro è vuoto")
        
        return sum(self.voti) / len(self.voti)
    
    def esito(self):
        if media(self) >= 6:
            return "Promosso"
        
        return "Bocciato"
        