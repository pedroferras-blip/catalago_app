#Avaliacao:o que o usuario escreve sobre uma obra
class Avaliacao:
    def __init__(self, autor, nota, comentario= ""):
        if not  0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 a 10")

        self.autor = autor 
        self.nota = nota 
        self.comentario = comentario

    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10"
        if self.comentario:
            texto += f' - "{self.comentario}"'
        return texto


#obra: classe base, outrs herdam dela
class Obras:
    tipo = "Obra"# atribito de clase: cada sebclasse sobrescreve
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero =genero
        self.avaliacoes = []

    def adicional_avalicao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def media(self):
        if not self.avaliacoes:
            return 0.0
        total = sum(a.nota for a in self.avaliacoes)
        return total/len(self.avaliacoes)

    def detalhes(self):
        #informacoes especificas de capa tipo, as subclasses sobrescrevem
        return""
    def __str__(self):
        base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
        extra =self.detalhes()
        if extra:
            base += f" | {extra}"
        return f"{base} | media: {self.media():.1f}  ({len(self.avaliacoes)})"

        

def main():
    avaliacao = Avaliacao("Joel", 9,"otimo filme")
    print(avaliacao)
    obras = Obras ("Interestelar",2014,"Ficcao cientifica")
    print(obras)

    obras.adicional_avalicao(Avaliacao("ana",9))
    obras.adicional_avalicao(Avaliacao("bruno",10 ))
    print(obras)
    print("media: ",obras.media())

if __name__ == "__main__":
    main()