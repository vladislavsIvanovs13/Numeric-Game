# Balstīts uz pseidokoda:
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

from game_tree import DEPTH

class AlphaBetaSolver:
    def __init__(self, tree):
        self.tree = tree

    # pārbauda, vai virsotnei ir bērni
    # return -> boolean
    def no_children(self, node):
        if (self.tree.edges.get(node.id) != None):
            return False
        else:
            return True

    # rekursīva metode
    # Metode iet no saknes, izsaucot sevi, līdz sasniedz pēdējo koka līmeni,
    # katru reizi mainot iestatījumus max/min.
    # Tālāk, salīdzinot bērnus, metode piešķir vecākam
    # heiristisku novērtējumu.
    def calculate_heu(self, node, depth, alpha, beta, max_level):
        if (depth == DEPTH or AlphaBetaSolver.no_children(self,node)):
            return node.heu

        if max_level:
            best_heu = float('-inf')
            children_nodes = self.tree.edges.get(node.id)
            heu_array = []
            for n in children_nodes:
                heu_array.append(AlphaBetaSolver.calculate_heu(self, n, depth + 1, alpha, beta, False))
                node.heu = max(heu_array)
                best_heu = max(best_heu, node.heu)
                alpha = max(alpha, best_heu)
                # nogriezt nevajadzīgo zaru
                if (beta <= alpha):
                    break
            return best_heu
        else:
            best_heu = float("inf")
            children_nodes = self.tree.edges.get(node.id)
            heu_array = []
            for n in children_nodes:
                heu_array.append(AlphaBetaSolver.calculate_heu(self, n, depth + 1, alpha, beta, True))
                node.heu = min(heu_array)
                best_heu = min(best_heu, node.heu)
                beta = min(beta, best_heu)
                # nogriezt nevajadzīgo zaru
                if (beta <= alpha):
                    break
            return best_heu

    # metode izsauc rekursīvu metodi calculate_heu, ar sākuma parametriem
    # metode ir veidota, lai pamatklasē ar pašu spēli,
    # izmantojot Alfa-beta algoritmu, nebūtu jādomā par
    # sākuma parametriem un nebūtu iespējams pieļaut kļūdu
    # return -> spēles koks ar heiristiskiem novērtējumiem
    def alpha_beta(self):
        AlphaBetaSolver.calculate_heu(self, self.tree.nodes[0], 1, float('-inf'), float('inf'), True)
        return self.tree