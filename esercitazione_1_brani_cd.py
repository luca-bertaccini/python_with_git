class Brano:
    def __init__ (self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata
        
    @property
    def titolo(self):
        return self._titolo
    
    @titolo.setter
    def titolo(self, valore):
        if not valore:
            raise ValueError("Il titolo è vuoto")
        self._titolo = valore
        
    @property
    def autore(self):
        return self._autore
    
    @autore.setter
    def autore(self, valore):
        if not valore:
            raise ValueError("L'autore è vuoto")
        
    @property
    def durata(self):
        return self._durata
    
    @durata.setter
    def durata(self, valore):
        if not valore:
            raise ValueError("La durata è vuota")
        
    def short_song(self):
        return self.durata <= 120
    
    def __str__(self):
        return f"{self.titolo} {self.autore} {self.durata} secondi"
    
class CD:
    def __init__(self, titolo, autore, brani):
        self.titolo = titolo
        self.autore = autore
        self.brani = brani if brani is not None else []
        
    def aggiungi_brano(self, brano):
        self.brani.append(brano)
        
    @property
    def durata_totale(self):
        totale = 0
        for brano in self.brani:
            totale += brano.durata
        
        return totale
    
    def __str__(self):
        return f"{self.titolo} {self.autore} durata totale {durata_totale(self)} secondi"
    