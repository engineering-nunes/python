import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def verificar_triangulo(a,b,c):
    if a + b <= c or a+c <=b or b+c <= a:
        return 'Não é um triângulo'
    else:
        s = (a + b + c) / 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return f'É um triângulo de área {round(area, 2)} u.a.!'

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.get_json()
    a = data['a']
    b = data['b']
    c = data['c']
    result = verificar_triangulo(a, b, c)
    return result

if __name__ == '__main__':
    app.run(debug=True)