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
            best_heu = float('-inf')
            children_node_ids = self.tree.edges.get(node.id)
            heu_array = []
            for id in children_node_ids:
                print("ID = ", id)
                heu_array.append(AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, False))
                print("heu_array MAX: " , heu_array)
                node.heu = max(heu_array)
                print(node.id, node.string, node.p1, node.p2, node.level, "heu = ", node.heu)
                print()
                print("best_heu MAX -----: ", best_heu)
                best_heu = max(best_heu, node.heu)
                print("best_heu MAX ----1: ", best_heu)
                print("alpha MAX -----: ", alpha)
                print("beta  -----: ", beta)
                alpha = max(alpha, best_heu)
                print("alpha MAX ----1: ", alpha)
                print()
                # cut off the unnecessary node
                if (beta <= alpha):
                    print("BREAK")
                    break
            print("best_heu MAX: ", best_heu)
            return best_heu
        else:
            best_heu = float("inf")
            children_node_ids = self.tree.edges.get(node.id)
            heu_array = []
            for id in children_node_ids:
                print("ID = ", id)
                heu_array.append(AlphaBeta.calculate_heu(self, self.tree.get_node(id), depth + 1, alpha, beta, True))
                print("heu_array MIN: " , heu_array)
                node.heu = min(heu_array)
                print(node.id, node.string, node.p1, node.p2, node.level, "heu = ", node.heu)
                print()
                print("best_heu MIN -----: ", best_heu)
                best_heu = min(best_heu, node.heu)
                print("best_heu MIN ----1: ", best_heu)
                print("beta MIN -----: ", beta)
                print("alpha -----: ", alpha)
                beta = min(beta, best_heu)
                print("beta MIN ----1: ", beta)
                print()
                # cut off the unnecessary node
                if (beta <= alpha):
                    print("BREAK")
                    break
            print("best_heu MIN: ", best_heu)
            return best_heu

    def alphabeta(self):
        AlphaBeta.calculate_heu(self, self.tree.nodes[0], 1, float('-inf'), float('inf'), True)
        return self.tree