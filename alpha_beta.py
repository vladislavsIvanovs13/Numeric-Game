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
            print("check: ", node.id, node.heu)
            return node.heu

        if max_level:
            best_max_heu = float('-inf')
            children_node_ids = self.tree.edges.get(node.id)
            for id in children_node_ids:
                print("ID = ", id)
                node.heu = AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, False)
                print(node.id, node.string, node.p1, node.p2, node.level, "heu = ", node.heu)
                print()
                print("best_heu MAX -----: ", best_max_heu)
                best_max_heu = max(best_max_heu, node.heu)
                print("best_heu MAX ----1: ", best_max_heu)
                print("alpha MAX -----: ", alpha)
                alpha = max(alpha, best_max_heu)
                print("alpha MAX ----1: ", alpha)
                print()
                # cut off the unnecessary node
                if (beta <= alpha):
                    print("BREAK")
                    break
            print("best_heu MAX: ", best_max_heu)
            return best_max_heu
        else:
            best_min_heu = float("inf")
            children_node_ids = self.tree.edges.get(node.id)
            for id in children_node_ids:
                print("ID = ", id)
                node.heu = AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, True)
                print(node.id, node.string, node.p1, node.p2, node.level, "heu = ", node.heu)
                print()
                print("best_heu MIN -----: ", best_min_heu)
                best_min_heu = min(best_min_heu, node.heu)
                print("best_heu MIN ----1: ", best_min_heu)
                print("alpha MAX -----: ", alpha)
                beta = min(beta, best_min_heu)
                print("alpha MAX ----1: ", alpha)
                print()
                # cut off the unnecessary node
                if (beta <= alpha):
                    break
            print("best_heu MIN: ", best_min_heu)
            return best_min_heu

    def alphabeta(self):
        AlphaBeta.calculate_heu(self, self.tree.nodes[0], 1, float('inf'), float('-inf'), False)
        return self.tree