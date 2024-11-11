from BinaryHeap import BinaryHeap

print("\n========== Conjunto 1: Dados Aleatórios Pequenos ==========\n")
data1 = [10, 5, 20, 1, 15, 30, 25]
conjunto1 = BinaryHeap(len(data1))
#                      ^Passo a capacidade com base no tamanho dos dados

# Inserções sequenciais
for value in data1:
    print(f"Inserindo o valor {value}")
    conjunto1.insert(value)
    conjunto1.display_heap()
    print("\n")

# Alterações de prioridade
print("Alterando o índice 3 para prioridade 50")
print(f"Antes:")
conjunto1.display_heap()
conjunto1.change_priority(3, 50)
print(f"Depois:")
conjunto1.display_heap()

# Alterações de prioridade
print("\nAlterando o índice 1 para prioridade 8")
print(f"Antes:")
conjunto1.display_heap()
conjunto1.change_priority(1, 8)
print(f"Depois:")
conjunto1.display_heap()

# Remoções
for i in range(3):
    print("\nRemovendo elemento de alta prioridade...")
    conjunto1.remove()
    conjunto1.display_heap()

# HeapSort
print("\nHeapSort (removendo todos os elementos e retornar eles ordenados):")
conjunto1.heap_sort()

# Selecionar alta prioridade
print("\nElemento de alta prioridade:", conjunto1.get_high_priority())

input("\nENTER - Próximo conjunto(2/4)\n")

#----------------------------------------------

print("\n========== Conjunto 2: Sequência Crescente ==========\n")
data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
conjunto2 = BinaryHeap(len(data2))

# Inserções sequenciais
for value in data2:
    print(f"Inserindo o valor {value}")
    conjunto2.insert(value)
    conjunto2.display_heap()
    print("\n")

# Alterações de prioridade
print("Alterando o índice 4 para prioridade 15")
print(f"Antes:")
conjunto2.display_heap()
conjunto2.change_priority(4, 15)
print(f"Depois:")
conjunto2.display_heap()

# Alterações de prioridade
print("\nAlterando o índice 8 para prioridade 3")
print(f"Antes:")
conjunto2.display_heap()
conjunto2.change_priority(8, 3)
print(f"Depois:")
conjunto2.display_heap()

# Remoções
for i in range(5):
    print("\nRemovendo elemento de alta prioridade...")
    conjunto2.remove()
    conjunto2.display_heap()

# HeapSort
print("\nHeapSort (removendo todos os elementos e retornar eles ordenados):")
conjunto2.heap_sort()

# Selecionar alta prioridade
print("\nElemento de alta prioridade:", conjunto2.get_high_priority())

input("\nENTER - Próximo conjunto(3/4)\n")

#----------------------------------------------

print("\n========== Conjunto 3: Sequência Decrescente ==========\n")
data3 = [50, 40, 30, 20, 10, 5, 3]
conjunto3 = BinaryHeap(len(data3))

# Inserções sequenciais
for value in data3:
    print(f"Inserindo o valor {value}")
    conjunto3.insert(value)
    conjunto3.display_heap()
    print("\n")

# Alterações de prioridade
print("Alterando o índice 2 para prioridade 60")
print(f"Antes:")
conjunto3.display_heap()
conjunto3.change_priority(2, 60)
print(f"Depois:")
conjunto3.display_heap()

# Alterações de prioridade
print("\nAlterando o índice 5 para prioridade 1")
print(f"Antes:")
conjunto3.display_heap()
conjunto3.change_priority(5, 1)
print(f"Depois:")
conjunto3.display_heap()

# Remoções
for i in range(3):
    print("\nRemovendo elemento de alta prioridade...")
    conjunto3.remove()
    conjunto3.display_heap()

# HeapSort
print("\nHeapSort (removendo todos os elementos e retornar eles ordenados):")
conjunto3.heap_sort()

# Selecionar alta prioridade
print("\nElemento de alta prioridade:", conjunto3.get_high_priority())

input("\nENTER - Próximo conjunto(4/4)\n")

#----------------------------------------------

print("\n========== Conjunto 4: Dados Aleatórios Maiores ==========\n")
data4 = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
conjunto4 = BinaryHeap(len(data4))

# Inserções sequenciais
for value in data4:
    print(f"Inserindo o valor {value}")
    conjunto4.insert(value)
    conjunto4.display_heap()
    print("\n")

# Alterações de prioridade
print("Alterando o índice 7 para prioridade 35")
print(f"Antes:")
conjunto4.display_heap()
conjunto4.change_priority(7, 35)
print(f"Depois:")
conjunto4.display_heap()

# Alterações de prioridade
print("\nAlterando o índice 10 para prioridade 12")
print(f"Antes:")
conjunto4.display_heap()
conjunto4.change_priority(10, 12)
print(f"Depois:")
conjunto4.display_heap()

# Remoções
for i in range(4):
    print("\nRemovendo elemento de alta prioridade...")
    conjunto4.remove()
    conjunto4.display_heap()

# HeapSort
print("\nHeapSort (removendo todos os elementos e retornar eles ordenados):")
conjunto4.heap_sort()

# Selecionar alta prioridade
print("\nElemento de alta prioridade:", conjunto4.get_high_priority())

input("\nENTER - Finalizar\n")

