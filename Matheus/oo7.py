# 1. Inicializa a lista de cidades
lista_cidades = ['Belo Horizonte']

# Exibe a lista inicial para referência
print("Lista inicial de cidades:", lista_cidades)

# 2. Utiliza um loop para solicitar 3 cidades ao usuário
for i in range(3):
    # 3. Solicita ao usuário o nome de uma cidade
    cidade = input(f"Digite o nome da {i+1}ª cidade para adicionar: ")
    
    # 4. Adiciona a cidade à lista
    lista_cidades.append(cidade)
    
    # 5. Imprime a lista atualizada
    print("Lista atualizada:", lista_cidades)

print("\n--- Processo concluído ---")
print("Lista final de cidades:", lista_cidades)

