from collections import defaultdict

# Função de mapeamento (map)
def mapper(line):
    user_id, movie_id, rating, _ = line.strip().split()
    return (user_id, [(movie_id, rating)])

# Função de redução (reduce)
def reducer(mapped_data):
    user_data = defaultdict(list)
    
    for user_id, movie_ratings in mapped_data:
        user_data[user_id].extend(movie_ratings)
    
    return user_data

# Função para ler o arquivo e aplicar o mapeamento
def read_file_and_map(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    mapped_data = [mapper(line) for line in lines[1:]]  # Ignorando o cabeçalho
    
    return mapped_data

# Função principal que coordena o processo MapReduce
def main():
    filename = 'arquivo.txt'
    mapped_data = read_file_and_map(filename)
    reduced_data = reducer(mapped_data)
    
    # Imprime os resultados
    for user_id, movie_ratings in reduced_data.items():
        print(f'User ID {user_id}:')
        for movie_id, rating in movie_ratings:
            print(f'Movie ID: {movie_id}, Rating: {rating}')

if __name__ == "__main__":
    main()
