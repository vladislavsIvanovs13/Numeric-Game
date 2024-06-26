# Balstīts uz studiju kursa materiāliem:
# https://estudijas.rtu.lv/mod/resource/view.php?id=4161716

from node_evaluator import Evaluator
from string_generator import MAX_NUMBER

POINT = 1
BIG_NUMBERS = {7, 8, 9, 10, 11, 12}
MOVE_ONE = '1'
MOVE_TWO = '2'
PAIR_LENGTH = 2
DEPTH = 5

# Virsotnes klase, kas atspoguļo stāvokli raksturojošus parametrus
class Node:
    def __init__(self, id, string, p1, p2, level, heu=float('-inf')):
        self.id = id # virsotnes identifikators
        self.string = string # konkrētajā brīdī pieejama virkne
        self.p1 = p1 # pirmā spēlētāja punktu skaits
        self.p2 = p2 # otrā spēlētāja punktu skaits
        self.level = level # virsotnes dziļums spēles kokā
        self.heu = heu # virsotnes heiristiskais vērtējums

# Koka klase, kas tikai satur virsotnes un lokus un atbalsta darbības ar tiem
class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = dict()

    def add_node(self, Node):
        self.nodes.append(Node)

    def add_edge(self, start_id, node):
        self.edges[start_id] = self.edges.get(start_id, []) + [node]

    def get_max_level(self):
        return self.nodes[len(self.nodes) - 1].level

# Spēles koka klase 
class GameTree:
    def check_step(step_type, generated_nodes, current_node, ptr, game_tree):
        global j
        id_new = 'A' + str(j) # atjauno identifikatoru
        string_new = current_node.string

        #atjauno brīdī pieejamo virkni
        if (step_type == MOVE_TWO) and (len(string_new) % 2 == 1) \
                and (len(string_new) > 1):
            string_new = string_new[:-1]

        elif (step_type == MOVE_ONE):
            sum = int(string_new[ptr:ptr + 1]) + \
                  int(string_new[ptr + 1:ptr + 2])

            if sum in BIG_NUMBERS:
                sum -= MAX_NUMBER

            string_new = string_new[:ptr] + str(sum) \
                         + string_new[ptr + 2:]

        else:
            return

        # atjauno spēlētāju punktus
        j += 1
        if (current_node.level % 2 == 0):
            p1_new = current_node.p1
            if (step_type == MOVE_ONE):
                p2_new = current_node.p2 + POINT
            else:
                p2_new = current_node.p2 - POINT
        else:
            p2_new = current_node.p2
            if (step_type == MOVE_ONE):
                p1_new = current_node.p1 + POINT
            else:
                p1_new = current_node.p1 - POINT

        # atjauno virsotnes dziļumu
        level_new = current_node.level + 1

        # novērtē strupceļa virsotnes
        if (level_new == DEPTH or len(string_new) == 1):
            heu_new = Evaluator.evaluate_node(p1_new, p2_new, step_type)
            node_new = Node(id_new, string_new, p1_new, p2_new, level_new, heu_new)
        else:
            node_new = Node(id_new, string_new, p1_new, p2_new, level_new)

        # pārbauda, vai jauna virsotne jau ir spēles kokā
        checked = False
        i = 0
        while (not checked) and (i <= len(game_tree.nodes) - 1):
            if (game_tree.nodes[i].string == node_new.string) \
                    and (game_tree.nodes[i].p1 == node_new.p1) \
                    and (game_tree.nodes[i].p2 == node_new.p2) \
                    and (game_tree.nodes[i].level == node_new.level):
                checked = True
            else:
                i += 1
        if not checked:
            game_tree.add_node(node_new)
            generated_nodes.append(Node(id_new, string_new, p1_new, p2_new, level_new))
            game_tree.add_edge(current_node.id, node_new)
        else:
            j -= 1
            game_tree.add_edge(current_node.id, game_tree.nodes[i])

    # pamatfunkcija, kas konstruē spēles koku
    def construct_tree(root_node, p1=0, p2=0):
        global j
        game_tree = Tree()
        generated_nodes = []
        game_tree.add_node(Node('A1', root_node, p1, p2, 1))
        generated_nodes.append(Node('A1', root_node, p1, p2, 1))
        
        j = 2
        while (len(generated_nodes) > 0) and (generated_nodes[0].level < DEPTH):
            current_node = generated_nodes[0]
            ptr = 0
            while ptr < len(current_node.string) - 1:
                GameTree.check_step(MOVE_ONE, generated_nodes, current_node, ptr, game_tree)
                ptr += PAIR_LENGTH
            GameTree.check_step(MOVE_TWO, generated_nodes, current_node, ptr, game_tree)
            generated_nodes.pop(0)

        return game_tree