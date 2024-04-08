class MinimaxSolver:
    def __init__(self, tree):
        self.tree = tree
        
    def get_max_heu(self, nodes):
        max_heu = float('-inf')
        for node in nodes:
            if node.heu > max_heu:
                max_heu = node.heu
        return max_heu

    def get_min_heu(self, nodes):
        min_heu = float('inf')
        for node in nodes:
            if node.heu < min_heu:
                min_heu = node.heu
        return min_heu

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

        for x in self.nodes:
            print(x.id, x.string, x.p1, x.p2, x.level, x.heu)
        return self