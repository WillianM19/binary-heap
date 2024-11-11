import copy
import math

class BinaryHeap:
    # def __init__(self, array=[None, 50, 40, 20, 15, 16, 13, None, None]):
    #     self.array = array

    #     #Contador de elementos preechidos
    #     self.size = len([x for x in array if x is not None])

    def __init__(self, capacity):
        # Array com Nones de acordo com a capacidade
        self.array = [None] * (capacity + 1)
        #Contador de elementos preechidos
        self.size = 0


    def insert(self, novo):
        # Verifica se ainda há espaço na heap
        if self.size < len(self.array):

            # Adiciona o novo elemento no final do heap
            self.array[self.size + 1] = novo
            self.size += 1

            # Sobe ele para ordenar
            self._subir(self.size)
        else:
            print("Overflow: A heap está cheia.")

    def remove(self):
        if self.size != 0:
            # Salva o elemento raiz
            raiz = self.array[1]

            # Move o último elemento para a raiz
            self.array[1] = self.array[self.size]
            self.array[self.size] = None  # Adicona None para indicar que o elemento foi removido
            self.size -= 1

            # Desce ele para ordenar
            self._descer(1, self.size)

            return raiz
        else:
                print("Underflow: A heap está vazia.")

    def change_priority(self, index, prioridade):
        # Verifica se o índice está dentro dos limites do heap
        if 1 <= index <= self.size:

            # Salva prioridade antiga e atualiza para nova
            prioridade_antes = self.array[index]
            self.array[index] = prioridade

            # Sobe ou desce dependendo da prioridade nova
            if prioridade > prioridade_antes:
                self._subir(index)
            else:
                self._descer(index, self.size)

        else:
            print("Índice fora do limite do heap.")


    def get_high_priority(self):
        return self.array[1] if self.size > 0 else None

    def heap_sort(self):
        print("Criando cópia...")
        # Cópia de si mesmo para não alterar a heap original
        heap_copy = copy.deepcopy(self)
        print("Heap antes de ordenar:", heap_copy.array)

        # Loop removendoo elementos do heap e adicionando no array
        sorted_list = []
        while heap_copy.size > 0:
            high_priority = heap_copy.remove()
            sorted_list.append(high_priority)
            print("Estado após remoção:", heap_copy.array)

        print("Resultado do Heap Sort:", sorted_list)

    def display_heap(self):
        nivel = 1
        i = 1
        while i <= self.size:
            elementos_no_nivel = 2 ** (nivel - 1)
            nivel_str = ''
            for _ in range(elementos_no_nivel):
                if i <= self.size:
                    nivel_str += str(self.array[i]) + ' '
                    i += 1
            print(' ' * (math.ceil(math.log2(self.size)) - nivel + 1) + nivel_str)
            nivel += 1

    def _subir(self, i):
        # Pega o indice do pai
        pai = i//2

        if pai >= 1:
            # Se for maior que o elemento pai
            if self.array[i] > self.array[pai]:

                # Swap entre pai e filho
                aux = self.array[pai]
                self.array[pai] = self.array[i]
                self.array[i] = aux

                # Recursão com o pai que mudou para elemento filho.
                self._subir(pai)

    def _descer(self, i, n):
        filho = 2*i

        if filho <= n: #Se o filho não passa do ultimo elemento
            if filho < n:
                if self.array[filho+1] > self.array[filho]:
                    filho += 1

            if self.array[i] < self.array[filho]:

                # Swap entre pai e filho
                aux = self.array[i]
                self.array[i] = self.array[filho]
                self.array[filho] = aux

                # Recursão com o filho que mudou para elemento pai.
                self._descer(filho, n)
