# Pseudocode: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
class AlphaBeta:
    def __init__(self, tree, DEPTH):
        self.tree = tree
        self.DEPTH = DEPTH

    def no_children(self, node):
        if (self.tree.edges.get(node.id) != None):
            return False
        else:
            return True

    def calculate_heu(self, node, depth, alpha, beta, max_level):
        if (depth == self.DEPTH or AlphaBeta.no_children(self,node)):
            return node.heu

        if max_level:
            best_heu = float('-inf')
            children_nodes = self.tree.edges.get(node.id)
            heu_array = []
            for n in children_nodes:
                heu_array.append(AlphaBeta.calculate_heu(self, n, depth + 1, alpha, beta, False))
                node.heu = max(heu_array)
                best_heu = max(best_heu, node.heu)
                alpha = max(alpha, best_heu)
                # cut off the unnecessary node
                if (beta <= alpha):
                    break
            return best_heu
        else:
            best_heu = float("inf")
            children_nodes = self.tree.edges.get(node.id)
            heu_array = []
            for n in children_nodes:
                heu_array.append(AlphaBeta.calculate_heu(self, n, depth + 1, alpha, beta, True))
                node.heu = min(heu_array)
                best_heu = min(best_heu, node.heu)
                beta = min(beta, best_heu)
                # cut off the unnecessary node
                if (beta <= alpha):
                    break
            return best_heu

    def alphabeta(self):
        AlphaBeta.calculate_heu(self, self.tree.nodes[0], 1, float('-inf'), float('inf'), True)
        return self.tree