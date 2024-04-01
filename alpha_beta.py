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
            best_max_heu = float('-inf')
            children_node_ids = self.tree.edges.get(node.id)
            for id in children_node_ids:
                node.heu = AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, False)
                best_max_heu = max(best_max_heu, node.heu)
                alpha = max(alpha, best_max_heu)
                # cut off the unnecessary node
                if (beta <= alpha):
                    break
            return best_max_heu
        else:
            best_min_heu = float("inf")
            children_node_ids = self.tree.edges.get(node.id)
            for id in children_node_ids:
                node.heu = AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, True)
                best_min_heu = min(best_min_heu, node.heu)
                beta = min(beta, best_min_heu)
                # cut off the unnecessary node
                if (beta <= alpha):
                    break
            return best_min_heu

    def alphabeta(self):
        AlphaBeta.calculate_heu(self, self.tree.nodes[0], 1, float('inf'), float('-inf'), False)
        return self.tree