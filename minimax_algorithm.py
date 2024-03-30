class MiniMax:
    def __init__(self, tree):
        self.tree = tree
    def MAX_heu(self, node_id_list):
        max_heu = float('-inf')
        if (len(node_id_list) == 1):
            return self.get_node(node_id_list[0]).heu
        else:
            for id in node_id_list:
                node = self.get_node(id)
                if node.heu > max_heu:
                    max_heu = node.heu
        return max_heu

    def MIN_heu(self, node_id_list):
        min_heu = float('inf')
        if (len(node_id_list) == 1):
            return self.get_node(node_id_list[0]).heu
        else:
            for id in node_id_list:
                node = self.get_node(id)
                if node.heu < min_heu:
                    min_heu = node.heu
        return min_heu

    def minimax(self):
        level = self.get_MAX_level() - 1

        if (len(self.nodes[0].string) % 2 == 0):
            maxLevel = True
        else:
            maxLevel = False

        for node in reversed(self.nodes):
            if(node.level < level):
                level-=1
                maxLevel = False if maxLevel == True else True
            if(node.level == level):
                nodeChildren_id = self.edges.get(node.id)
                if (nodeChildren_id == None or len(nodeChildren_id) == 0):
                    continue
                if(maxLevel):
                    node.heu = MiniMax.MAX_heu(self, nodeChildren_id)
                else:
                    node.heu = MiniMax.MIN_heu(self, nodeChildren_id)

        return self