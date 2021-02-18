
class Formiga:
    def __init__(self, linha, coluna, move):
        self.linha = linha
        self.coluna = coluna
        self.move = move

def run_langton(rules, size):
    cor = len(rules)
    centro = size//2
    cont = 0

    matriz = [[0 for i in range(size)] for j in range(size)]
    dentro = True
    
    turn = Formiga(centro, centro, 'cima')
    
    while dentro == True:
        matriz[turn.linha][turn.coluna] += 1
        if matriz[turn.linha][turn.coluna] >= cor:
            matriz[turn.linha][turn.coluna] = 0
        
        if turn.move == 'cima':
            turn.linha -= 1
        elif turn.move == 'baixo':
            turn.linha += 1
        elif turn.move == 'direita':
            turn.coluna += 1
        elif turn.move == 'esquerda':
            turn.coluna -= 1
        cont = cont + 1

        if turn.linha < 0 or turn.coluna < 0 or turn.linha >= size or turn.coluna >= size:
            dentro = False

        if dentro == True:
            cor = matriz[turn.linha][turn.coluna]
            regra = rules[cor]
            if turn.move == 'cima':
                if regra == 'R':
                    turn.move = 'direita'
                elif regra == 'L':
                    turn.move = 'esquerda'

            elif turn.move == 'baixo':
                if regra == 'R':
                    turn.move = 'esquerda'
                elif regra == 'L':
                    turn.move = 'direita'

            elif turn.move == 'direita':
                if regra == 'R':
                    turn.move = 'baixo'
                elif regra == 'L':
                    turn.move = 'cima'

            elif turn.move == 'esquerda':
                if regra == 'R':
                    turn.move = 'cima'

                elif regra == 'L':
                    turn.move = 'baixo' 
        
    return (cont, matriz)