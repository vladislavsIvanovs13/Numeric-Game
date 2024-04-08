MOVE_ONE = '1'

# Novērtējuma klase, kas atbild par heiristiskā novērtējuma funkciju
class Evaluator():
    # novērtē virsotni, balstoties uz 2 faktoriem
    def evaluate_node(p1, p2, step_type):
        factor1 = p1 - p2
        factor2 = 1 if (step_type == MOVE_ONE) else 0
        return factor1 + factor2