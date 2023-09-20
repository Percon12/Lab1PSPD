
"""
O algoritmo PageRank com MapReduce pode ser dividido em três fases:

* Fase de Mapeamento (Map):

Cada nó do grafo (página da web) emite uma proporção do seu PageRank para cada nó que ele se conecta. 
Isso é feito em um processo de mapeamento que gera pares chave-valor, onde a chave é o destino do link 
e o valor é a proporção do PageRank que está sendo passada.

* Fase de Shuffle e Ordenação:

Os pares chave-valor gerados na fase de mapeamento são agrupados por chave (destino do link) e ordenados.

* Fase de Redução (Reduce):

Nesta fase, o PageRank total para cada página é calculado somando todas as proporções recebidas de outras páginas. 
O novo valor do PageRank é calculado usando a fórmula do PageRank e, em seguida, normalizado.

O processo acima é repetido em várias iterações até que o PageRank converja para um valor estável.
"""

from collections import defaultdict

# Função de mapeamento
def map_page_rank(page, links, rank):
    num_links = len(links)
    for link in links:
        yield (link, rank / num_links)

# Função de redução
def reduce_page_rank(page, values, damping_factor, num_pages):
    new_rank = (1 - damping_factor) / num_pages
    for value in values:
        new_rank += damping_factor * value
    return new_rank

# Função principal do PageRank com MapReduce
def page_rank_map_reduce(pages, links, damping_factor=0.85, num_iterations=10):
    num_pages = len(pages)
    ranks = {page: 1.0 / num_pages for page in pages}

    for iteration in range(num_iterations):
        contributions = defaultdict(list)

        # Fase de mapeamento
        for page, rank in ranks.items():
            if page in links:
                for dest_page in links[page]:
                    contributions[dest_page].append(rank)

        # Fase de redução
        new_ranks = {}
        for page, values in contributions.items():
            new_rank = reduce_page_rank(page, values, damping_factor, num_pages)
            new_ranks[page] = new_rank

        # Atualiza os ranks
        ranks = dict(new_ranks)

    # Normalização dos PageRanks para que a soma seja igual a 1
    total_rank = sum(ranks.values())
    normalized_ranks = {page: rank / total_rank for page, rank in ranks.items()}

    return normalized_ranks

# Exemplo de uso
if __name__ == "__main__":
    pages = ["A", "B", "C", "D"]
    links = {"A": ["B", "C"], "B": ["C"], "C": ["A", "D"], "D": ["A"]}

    page_rank = page_rank_map_reduce(pages, links)
    for page, rank in page_rank.items():
        print(f"Page {page}: Rank = {rank}")
