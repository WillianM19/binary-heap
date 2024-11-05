from BinaryHeap import BinaryHeap

arvore = BinaryHeap()

print("\nArvore inicial:\n")
print(arvore, "\n")

print("🆕 Adicionando número 1000:\n")
arvore.adicionar(1000)
print("Resultado:", arvore, "\n")

print("🆕 Adicionando número 1999:\n")
arvore.adicionar(1999)
print("Resultado:", arvore, "\n")

print("⏪ Removendo elemento raiz:\n")
elemento_removido = arvore.remover()
print("Resultado:", arvore, "\n")
print(f"🆗 Raiz removida: {elemento_removido}")