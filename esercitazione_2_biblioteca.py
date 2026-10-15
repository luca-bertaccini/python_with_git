class Libro:
    def __init__(self, autore, titolo, anno, editore, pagine):
        self.autore = autore
        self.titolo = titolo
        self.anno = anno
        self.editore = editore
        self.pagine = pagine
        
    def reading_time(self):
        if self.pagine < 100:
            return "2 ore"
        if self.pagine < 200:
            return "5 ore"
        return "più di 5 ore"
    
    def __str__(self):
        return f"{self.autore} {self.titolo} {self.pagine} pagine"