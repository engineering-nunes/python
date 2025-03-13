import matplotlib.pyplot as plt

def G(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
    
def run_collatz():
    eixo_x = []  
    eixo_y = []
    
    n = int(input('Digite um valor inicial positivo diferente de 1: '))
    
    
    eixo_x.append(0)  
    eixo_y.append(n)  
    
    iteration = 1
    while n != 1:
        n = int(G(n))  
        eixo_x.append(iteration)  
        eixo_y.append(n)  
        print(f"Itneração {iteration}: {n}")
        iteration += 1
    
    if eixo_y[-1] != 1:
        eixo_x.append(iteration)
        eixo_y.append(1)
        
    print(f"Final eixo_x: {eixo_x}")  
    print(f"Final eixo_y: {eixo_y}")
    
    return eixo_x, eixo_y

def main():
    x_values, y_values = run_collatz()
    
    if len(x_values) > 1: 
        plt.figure(figsize=(10, 6))  
        plt.plot(x_values, y_values, marker='o', linewidth=0, color='blue')
        plt.title('Sequência de Collatz')
        plt.xlabel('Iteração')
        plt.ylabel('Valor')
        plt.grid(True)
        plt.tight_layout()  
        plt.show()
    else:
        print("Não há pontos suficientes para plotar.")

if __name__ == '__main__':
    main()