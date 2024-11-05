import math

class BinaryHeap:
    def __init__(self, array=[None, 50, 40, 20, 15, 16, 13, None, None]):
        self.array = array
        
        #Contador de elementos preechidos
        self.size = len([x for x in array if x is not None]) 

    
    def adicionar(self, novo):
        # Verifica se ainda há espaço na heap
        if self.size < len(self.array):
            
            # Adiciona o novo elemento na próxima posição disponível
            self.array[self.size + 1] = novo
            self.size += 1
            
            # Ajusta a posição do novo elemento para manter a propriedade da heap
            self._subir(self.size)
        else:
            print("Overflow: A heap está cheia.")
            
    def remover(self):
        if self.size != 0:
            # Salva o elemento raiz
            raiz = self.array[1]
            
            print(f"Movendo ultimo para raiz - {self.array[self.size]} <-> {self.array[1]}")
            
            # Pega o ultimo elemento e move para a raiz
            self.array[1] = self.array[self.size]
            
            
            self._descer(1, self.size)
            
            return raiz
        else:
                print("Underflow: A heap está vazia.")
    
    def _subir(self, i):
        # Pega o indice do pai
        pai = i//2
        
        if pai >= 1:
            # Se for maior que o elemento pai
            if self.array[i] > self.array[pai]:
                print(f"Subindo - {self.array[i]} <-> {self.array[pai]}")
                
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
                print(f"Descendo - {self.array[i]} <-> {self.array[filho]}")
                # Swap entre pai e filho
                aux = self.array[i]
                self.array[i] = self.array[filho]
                self.array[filho] = aux
                
                # Recursão com o filho que mudou para elemento pai.
                self._descer(filho, n)
            
    def __str__(self):
        return str(self.array)
    