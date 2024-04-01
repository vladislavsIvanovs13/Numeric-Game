class MinimaxSolver:
    def __init__(self, tree):
        self.tree = tree
        
    def get_max_heu(self, node_id_list):
        max_heu = float('-inf')
        for id in node_id_list:
            node = self.get_node(id)
            if node.heu > max_heu:
                max_heu = node.heu
        return max_heu

    def get_min_heu(self, node_id_list):
        min_heu = float('inf')
        for id in node_id_list:
            node = self.get_node(id)
            if node.heu < min_heu:
                min_heu = node.heu
        return min_heu

    def minimax(self):
        child_level = self.get_max_level() - 1

        max_level = len(self.nodes[0].string) % 2 == 0

        for node in reversed(self.nodes):
            if (node.level < child_level):
                child_level -= 1
                max_level = not max_level
                
            if (node.level == child_level):
                children_node_ids = self.edges.get(node.id)
                if (max_level):
                    node.heu = MinimaxSolver.get_max_heu(self, children_node_ids)
                else:
                    node.heu = MinimaxSolver.get_min_heu(self, children_node_ids)

        return self