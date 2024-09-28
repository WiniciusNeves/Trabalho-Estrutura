import matplotlib.pyplot as plt
import numpy as np

class Inteiros:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return Inteiros(self.valor + other.valor)

    def __sub__(self, other):
        return Inteiros(self.valor - other.valor)

    def __mul__(self, other):
        return Inteiros(self.valor * other.valor)

    def __str__(self):
        return str(self.valor)

    def __eq__(self, other):
        if isinstance(other, Inteiros):
            return self.valor == other.valor
        return False


    def teste_associatividade(self, b, c):
        return (self + (b + c)) == ((self + b) + c)

    def teste_comutatividade(self, other):
        return (self + other) == (other + self) and (self * other) == (other * self)

    def teste_elemento_neutro(self):
        return (self + Inteiros(0)) == self and (self * Inteiros(1)) == self

    def teste_distributividade(self, b, c):
        return self * (b + c) == (self * b) + (self * c)

 
    def polinomio(self, coeficientes, x):
        return sum(coef * (x ** i) for i, coef in enumerate(coeficientes))


def plot_operations(a, b):
    valores_a = [a.valor] * 5
    valores_b = [b.valor] * 5
    resultados_adicao = [a.valor + i for i in range(-2, 3)]
    resultados_multiplicacao = [a.valor * i for i in range(-2, 3)]

    plt.figure(figsize=(10, 5))

   
    plt.subplot(1, 2, 1)
    plt.plot(range(-2, 3), resultados_adicao, marker='o', label=f'{a.valor} + x')
    plt.title('Adição')
    plt.xlabel('x')
    plt.ylabel('Resultado')
    plt.legend()

  
    plt.subplot(1, 2, 2)
    plt.plot(range(-2, 3), resultados_multiplicacao, marker='o', label=f'{a.valor} * x', color='orange')
    plt.title('Multiplicação')
    plt.xlabel('x')
    plt.ylabel('Resultado')
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_polynomial(a, coeficientes):
    x = np.linspace(-2, 2, 100)
    y = [a.polinomio(coeficientes, xi) for xi in x]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='Polinômio', color='green')
    plt.title('Gráfico do Polinômio')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()


a = Inteiros(int(input("Informe um número: ")))
b = Inteiros(int(input("Informe outro número: ")))
c = Inteiros(int(input("Informe mais um número: ")))
10

print(f'Teste de associatividade: {a.teste_associatividade(b, c)}')
print(f'Teste de comutatividade: {a.teste_comutatividade(b)}')
print(f'Teste de elemento neutro: {a.teste_elemento_neutro()}')
print(f'Teste de distributividade: {a.teste_distributividade(b, c)}')

