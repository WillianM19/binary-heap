# Manipulação e Visualização do Binary Heap

Atividade realizada durante a disciplina de Estrutura de Dados não lineares - IFRN 2024.

## Objetivo
Implementar e validar todas as operações de um Binary Heap, garantindo que cada etapa de execução seja visível. Você deverá realizar a manipulação de dados
diretamente no main , com diferentes conjuntos de dados e uma sequência de operações que demonstrem o funcionamento completo do Binary Heap.

## Parte 1: Implementação dos Métodos
Implemente os seguintes métodos para o Binary Heap:
1. insert(value)
Insere um valor no heap e reorganiza a estrutura para manter as propriedades do Binary Heap.
Entrada: Um valor inteiro.
Saída: Estado atualizado do heap.
2. remove()
Remove o elemento de alta prioridade e reorganiza o heap.
Saída: Estado atualizado do heap após a remoção.
3. change_priority(index, new_priority)
Altera a prioridade de um elemento em uma posição arbitrária.
Entrada: Um índice e a nova prioridade.
Saída: Estado atualizado do heap após a alteração.
4. get_high_priority()
Retorna o elemento de alta prioridade, ou seja, o elemento da raiz do heap.
Saída: Valor do elemento de alta prioridade.
5. heap_sort()
Realiza a ordenação do heap.
Saída: Estado do heap em cada etapa.
6. display_heap()
Exibe o estado atual do heap, seja em formato de array ou visualização gráfica opcional.

## Parte 2: Testes no main
Implemente a sequência de operações abaixo no main . Cada operação deve exibir o estado do Binary Heap após a execução.
Conjunto de Dados e Testes
Para cada conjunto de dados, siga a ordem de operações abaixo:

### Conjunto 1: Dados Aleatórios Pequenos
Dados de Construção: [10, 5, 20, 1, 15, 30, 25]
1. Construção do Heap
Insira os valores [10, 5, 20, 1, 15, 30, 25] em sequência usando insert(value) . Exiba o heap após cada inserção com display_heap() .
2. Alteração de Prioridade
Alterar a prioridade do índice 3 para 50 usando change_priority(3, 50) .
Alterar a prioridade do índice 1 para 8 usando change_priority(1, 8) .
Exiba o heap após cada alteração.
3. Remoções
Execute remove() três vezes consecutivas, exibindo o heap após cada remoção.
4. Heapsort
Aplique heap_sort() para remover e ordenar todos os elementos. Exiba o estado do heap após cada remoção.
5. Selecionar Alta Prioridade
Use get_high_priority() para exibir o elemento de alta prioridade.

### Conjunto 2: Sequência Crescente
Dados de Construção: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

1. Construção do Heap
Insira os valores [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] em sequência e exiba o heap após cada inserção.
2. Alteração de Prioridade
Altere o índice 4 para a prioridade 15 ( change_priority(4, 15) ).
Alterar o índice 8 para a prioridade 3 e exibir o heap após cada alteração.
3. Remoções
Execute remove() cinco vezes consecutivas, visualizando o heap após cada remoção.
4. Heapsort
Aplique heap_sort() para remover todos os elementos, exibindo o estado do heap em cada etapa.
5. Selecionar Alta Prioridade
Use get_high_priority() para exibir o elemento de alta prioridade.

### Conjunto 3: Sequência Decrescente
Dados de Construção: [50, 40, 30, 20, 10, 5, 3]
1. Construção do Heap
Insira os valores [50, 40, 30, 20, 10, 5, 3] e exiba o heap após cada inserção.
2. Alteração de Prioridade
Alterar a prioridade do índice 2 para 60 usando change_priority(2, 60) .
Alterar o índice 5 para 1 e visualizar após cada alteração.
3. Remoções
Remova o elemento de alta prioridade três vezes consecutivas, exibindo o heap após cada remoção.
4. Heapsort
Remova todos os elementos em ordem com heap_sort() , visualizando o heap em cada etapa.
5. Selecionar Alta Prioridade
Exiba o elemento de alta prioridade após a construção inicial.

### Conjunto 4: Dados Aleatórios Maiores
Dados de Construção: [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
1. Construção do Heap
Insira os valores [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18] em sequência, exibindo o heap após cada inserção.
2. Alteração de Prioridade
Altere o índice 7 para 35 e exiba o resultado.
Alterar o índice 10 para 12 e visualizar após cada alteração.
3. Remoções
Execute remove() quatro vezes consecutivas, visualizando o heap após cada remoção.
4. Heapsort
Aplique heap_sort() para ordenar todos os elementos, exibindo o heap em cada remoção.
5. Selecionar Alta Prioridade
Use get_high_priority() para exibir o elemento de alta prioridade após a construção inicial.