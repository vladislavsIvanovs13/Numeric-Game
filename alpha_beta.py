# visa funkcija aizgūta no https://pastebin.com/rZg1Mz9G pseidokoda.

def alphabeta(pos, depth, alpha, beta, max):
    if depth == 0:  # or game over
        return pos
    
    if max == True:
        maxEval = float('-inf')
        for node in pos:
            eval = alphabeta(node, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
        return maxEval
    else:
        minEval = float("inf")
        for node in pos:
            eval = alphabeta(node, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
        return minEval