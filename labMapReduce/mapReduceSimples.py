# Define um dicionário para armazenar os dados
dados_usuario = {}

# Abre o arquivo para leitura
with open('arquivo.txt', 'r') as arquivo:
    # Lê as linhas do arquivo, excluindo o cabeçalho
    linhas = arquivo.readlines()[1:]

    # Itera sobre as linhas do arquivo
    for linha in linhas:
        # Divide a linha em partes com base nos espaços em branco
        partes = linha.split()

        # Extrai os valores de user_id, movie_id e rating
        user_id = int(partes[0])
        movie_id = int(partes[1])
        rating = int(partes[2])

        # Verifica se o user_id já existe no dicionário
        if user_id in dados_usuario:
            dados_usuario[user_id].append((movie_id, rating))
        else:
            dados_usuario[user_id] = [(movie_id, rating)]

# Itera sobre o dicionário e imprime os filmes e ratings para cada user_id
for user_id, filmes_ratings in dados_usuario.items():
    print(f'User ID {user_id}:')
    for movie_id, rating in filmes_ratings:
        print(f'Movie ID: {movie_id}, Rating: {rating}')
