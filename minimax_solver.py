# Minimaksa algoritms balstās uz galveno principu:
# https://www.youtube.com/watch?v=GtPXxl2QjKU

class MinimaxSolver:
    def __init__(self, tree):
        self.tree = tree

    # metode meklē maksimālo heiristisko novērtējumu no virsotņu saraksta
    # return -> maksimālo heiristisko novērtējumu
    def get_max_heu(self, nodes):
        max_heu = float('-inf')
        for node in nodes:
            if node.heu > max_heu:
                max_heu = node.heu
        return max_heu

    # metode meklē minimālo heiristisko novērtējumu no virsotņu saraksta
    # return -> minimālo heiristisko novērtējumu
    def get_min_heu(self, nodes):
        min_heu = float('inf')
        for node in nodes:
            if node.heu < min_heu:
                min_heu = node.heu
        return min_heu

    # koka DEPTH (dziļums) = 5
    # metode sāk meklēt bērnus virsotnēm priekšpēdējā līmenī (4),
    # salīdzina vērtības un piešķir vecākam
    # heiristisku vērtējumu atbilstoši līmenim (max/min)
    # return -> spēles koks ar heiristiskiem novērtējumiem
    def minimax(self):
        child_level = self.get_max_level() - 1

        max_level = False

        for node in reversed(self.nodes):
            if (node.level < child_level):
                child_level -= 1
                max_level = not max_level
                
            if (node.level == child_level):
                children_nodes = self.edges.get(node.id)
                if (max_level):
                    node.heu = MinimaxSolver.get_max_heu(self, children_nodes)
                else:
                    node.heu = MinimaxSolver.get_min_heu(self, children_nodes)
        
        return self