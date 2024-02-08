class Pagina:
    def __init__(self, nome, conteudo, ligacoes) -> None:
        self.nome =  nome
        self.conteudo = conteudo
        self.ligacoes = ligacoes

    def mostrar(self):
        return f"{self.nome} - {self.conteudo}"
    
class PageRank:
    def __init__(self, paginas) -> None:
        self.paginas = paginas
    
    def calcular_pagerank(self):
        grafo = {pagina.nome: pagina.ligacoes for pagina in self.paginas}

        return self.pagerank(grafo)

    def pagerank(self, grafo, d=0.85, iteracoes=100):
        num_paginas = len(grafo)
        pagerank_atual = {pagina: 1/num_paginas for pagina in grafo}

        for _ in range(iteracoes):
            pagerank_novo = {}

            for pagina in grafo:
                soma_pagerank = 0

                for pagina_que_linka, links in grafo.items():
                    if pagina in links:
                        num_links = len(links)
                        soma_pagerank += pagerank_atual[pagina_que_linka] / num_links

                novo_pagerank = (1 - d) + d * soma_pagerank
                pagerank_novo[pagina] = novo_pagerank

            pagerank_atual = pagerank_novo

        return pagerank_atual
    
    def buscar_pagina(self, termo):
        paginas = []
        for pagina in self.paginas:
            if termo in pagina.conteudo:
                paginas.append(pagina)
        resposta = input("usar page rank:[y/n]")

        if resposta == "y":
            resultado_pagerank = self.calcular_pagerank()
            paginas_ordenadas = sorted(paginas, key=lambda pagina: resultado_pagerank[pagina.nome], reverse=True)
            return paginas_ordenadas
        else:
            return paginas

paginas = [
    Pagina(nome='pagina1', conteudo='Aqui tem um conteudo de algebra e matematica', ligacoes=['pagina4', 'pagina3', 'pagina2']),
    Pagina(nome='pagina2', conteudo='Aqui fala sobre vetores e algebra', ligacoes=['pagina3', 'pagina4']),
    Pagina(nome='pagina3', conteudo='Aqui fala sobre algebra e matematica', ligacoes=['pagina1', 'pagina4']),
    Pagina(nome='pagina4', conteudo='Aqui não fala de nada algebra apenas fisica', ligacoes=['pagina1']),
]

pageRank = PageRank(paginas)
print(pageRank.calcular_pagerank())
termo_busca = input("Digite um termo: ")
paginas = pageRank.buscar_pagina("algebra")
for pagina in paginas:
    print(pagina.mostrar())
