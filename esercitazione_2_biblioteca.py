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
    
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.libri = []
        
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        
    def cerca_per_titolo(self, titolo):
        for libro in libri:
            if libro.titolo == self.titolo:
                return libro
            
        return None
    
    def cerca_per_autore(self, autore):
        for libro in libri:
            if libro.autore == self.autore:
                return libro
            
        return None
    
    def conta_libri(self):
        return len(self.libri)
    
    