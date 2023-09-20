"""O algoritmo PageRank é um algoritmo de classificação usado para determinar a importância relativa das páginas da web. 
Ele foi desenvolvido pelos fundadores do Google, Larry Page e Sergey Brin, enquanto estavam na Universidade Stanford, e é 
uma parte fundamental do algoritmo de pesquisa do Google. O PageRank funciona tratando a web como um 
grafo direcionado, onde as páginas são nós e os links entre elas são arestas. Cada nó (ou página) recebe 
um valor de PageRank, que é uma medida de sua importância."""

class PageRank:
    def __init__(self, pages, links, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
        self.pages = pages
        self.links = links
        self.damping_factor = damping_factor
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def calculate_page_rank(self):
        num_pages = len(self.pages)
        initial_rank = 1.0 / num_pages
        page_rank = {page: initial_rank for page in self.pages}

        for _ in range(self.max_iterations):
            new_page_rank = {}
            delta = 0.0

            for page in self.pages:
                rank = (1 - self.damping_factor) / num_pages
                for linking_page in self.links.get(page, []):
                    rank += self.damping_factor * (page_rank[linking_page] / len(self.links[linking_page]))
                new_page_rank[page] = rank
                delta += abs(new_page_rank[page] - page_rank[page])

            page_rank = new_page_rank

            if delta < self.tolerance:
                break

        return page_rank

# Exemplo de uso
if __name__ == "__main__":
    pages = ["A", "B", "C", "D"]
    links = {"A": ["B", "C"], "B": ["C"], "C": ["A", "D"], "D": ["A"]}

    pagerank_calculator = PageRank(pages, links)
    page_rank = pagerank_calculator.calculate_page_rank()
    for page, rank in page_rank.items():
        print(f"Page {page}: Rank = {rank}")


"""
Nesta solução Python, estamos usando um grafo representado por dicionários, onde as chaves são as 
páginas e os valores são listas de páginas para as quais elas têm links. O algoritmo itera várias 
vezes, atualizando os valores de PageRank para cada página até que as mudanças se tornem 
insignificantes (convergência). O fator de amortecimento (damping factor) é usado para controlar a 
probabilidade de saltar aleatoriamente para outra página, em vez de seguir os links.
"""

"""

   A   -->   B
   | \    / |
   |  \  /  |
   |   \/   |
   |   /\   |
   |  /  \  |
   | /    \ |
   C   <--   D

"""