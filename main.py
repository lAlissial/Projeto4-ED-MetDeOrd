from frufru import *
import random
import time

def bubbleSort(lista):
  tamanhozito = len(lista)

  for i in range(tamanhozito):
    for j in range(0, tamanhozito - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]


def insertionSort(lista):
  for i in range(1, len(lista)):
    posat = lista[i]
    j = i - 1

    while j >= 0 and posat < lista[j]:
      lista[j + 1] = lista[j]
      j -= 1
    lista[j + 1] = posat


def shellSort(lista):
  aux = len(lista) // 2
  while aux > 0:
    for i in range(aux, len(lista)):
      variavel = lista[i]
      j = i
      while j >= aux and lista[j - aux] > variavel:
        lista[j] = lista[j - aux]
        j -= aux
      lista[j] = variavel
    aux //= 2


def partezita(lista, co, fi):
  i = (co - 1)
  pivot = lista[fi]

  for j in range(co, fi):
    if lista[j] <= pivot:
      i = i + 1
      lista[i], lista[j] = lista[j], lista[i]

  lista[i + 1], lista[fi] = lista[fi], lista[i + 1]
  return (i + 1)


def quickSort(lista, co, fi):
  if len(lista) == 1:
    return lista
  if co < fi:
    pi = partezita(lista, co, fi)

    quickSort(lista, co, pi - 1)
    quickSort(lista, pi + 1, fi)


def mergeSort(lista):
  taman = len(lista)
  if taman > 1:
    meio = taman // 2
    esquerdo = lista[:meio]
    direito = lista[meio:]

    mergeSort(esquerdo)
    mergeSort(direito)

    i = 0
    j = 0
    k = 0

    taman_esq = len(esquerdo)
    taman_dir = len(direito)
    while i < taman_esq and j < taman_dir:
      if esquerdo[i] < direito[j]:
        lista[k] = esquerdo[i]
        i += 1
      else:
        lista[k] = direito[j]
        j += 1
      k += 1

    while i < taman_esq:
      lista[k] = esquerdo[i]
      i = i + 1
      k = k + 1

    while j < taman_dir:
      lista[k] = direito[j]
      j = j + 1
      k = k + 1


def printazito(funcao, nome, lista, cor1, cor2):
    cabecalho(f'{nome.upper()}', cor1)
    print('\nLista desordenada recebida pelo método:')
    print(lista)
    if nome.upper() != 'QUICKSORT':
      antes = time.time()
      funcao(lista)
      depois = time.time()
      total = (depois - antes)
    else:
      antes = time.time()
      funcao(lista, 0, len(lista)-1)
      depois = time.time()
      total = (depois - antes)
    print(f'{c[cor2]}A lista foi ordenada:{c[0]}')
    print(f'{c[cor1]}{listazita}{c[0]}')
    print(f'\n{c[cor2]}O tempo de ordenação do {nome.capitalize()} foi: {total}s{c[0]}\n')
    print('=' * 50)
    return total


listinha = []
for i in range(0, 20000):
  listinha.append(random.randint(1, 5000))
  

print(f'*' * 50)
print(f"{c[10]}{'EXECUÇÃO + TEMPO DE ALGORITMOS DE ORDENAÇÃO':^50}{c[0]}")
print(f'*' * 50)

while True:
    resp = menu(["BubbleSort", "InsertionSort", "ShellSort", "QuickSort", "MergeSort", "Todos juntos", "Sair do Sistema"],"MENU PRINCIPAL")
    listazita = listinha.copy()
    if resp == 1:
      printazito(bubbleSort, 'BubbleSort', listazita, 6, 32)

    if resp == 2:
      printazito(insertionSort, 'InsertionSort', listazita, 15, 21)

    if resp == 3:
      printazito(shellSort, 'ShellSort', listazita, 3, 19)

    if resp == 4:
      printazito(quickSort, 'QuickSort', listazita, 10, 26)

    if resp == 5:
      printazito(mergeSort, 'MergeSort', listazita, 11, 27)

    if resp == 6:
      listazita1 = listinha.copy()
      listazita2 = listinha.copy()
      listazita3 = listinha.copy()
      listazita4 = listinha.copy()

      cabecalho('TODOS', 12)

      p1 = printazito(bubbleSort, 'BubbleSort', listazita, 6, 32)
      p2 = printazito(insertionSort, 'InsertionSort', listazita1, 15, 21)
      p3 = printazito(shellSort, 'ShellSort', listazita2, 3, 19)
      p4 = printazito(quickSort, 'QuickSort', listazita3, 10, 26)
      p5 = printazito(mergeSort, 'MergeSort', listazita4, 11, 27)


      cabecalho('TODOS JUNTOS', 8)
      print(f'{c[32]}O tempo de ordenação do BubbleSort foi: {p1}s{c[0]}\n{c[21]}O tempo de ordenação do InsertionSort foi: {p2}s{c[0]}\n{c[19]}O tempo de ordenação do ShellSort foi: {p3}s{c[0]}\n{c[26]}O tempo de ordenação do QuickSort foi: {p4}s{c[0]}\n{c[27]}O tempo de ordenação do MergeSort foi: {p5}s{c[0]}')
      print('=' * 50)

    if resp == 7:
        cabecalho('ATÉ A PRÓXIMA!', 0)
        break
