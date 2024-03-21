#Aizgūts no studiju kursa materiāliem:
# https://estudijas.rtu.lv/mod/resource/view.php?id=4161716
from string_generator import MAX_NUMBER

POINT = 1
BIG_NUMBERS = {7, 8, 9, 10, 11, 12}
 
class Node:
    def __init__(self, id, string, p1, p2, level, heu=0):
        self.id = id
        self.string = string
        self.p1 = p1
        self.p2 = p2
        self.level = level
        self.heu = heu
        
class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = dict()
    
    def add_node(self, Node):
        self.nodes.append(Node)
        
    def add_edge(self, start_id, end_id):
        self.edges[start_id] = self.edges.get(start_id, []) + [end_id]
        
def check_step(step_type, generated_nodes, current_node, ptr):
        global j
        id_new = 'A' + str(j)
        string_new = current_node[1]
        
        if (step_type == '2') and (len(string_new) % 2 == 1) \
                and (len(string_new) > 1):
            string_new = string_new[:-1]
            
        elif (step_type == '1'):
            sum = int(string_new[ptr:ptr+1]) + \
                  int(string_new[ptr+1:ptr+2])
            
            if sum in BIG_NUMBERS:
                sum -= MAX_NUMBER
                
            string_new = string_new[:ptr] + str(sum) \
                        + string_new[ptr+2:]
            
        else: return
        
        j += 1
        if (current_node[4] % 2 == 0):
            p1_new = current_node[2]
            if (step_type == '1'):
                p2_new = current_node[3] + POINT
            else:
                p2_new = current_node[3] - POINT
        else:
            p2_new = current_node[3]
            if (step_type == '1'):
                p1_new = current_node[2] + POINT
            else:
                p1_new = current_node[2] - POINT
        
        level_new = current_node[4] + 1
        node_new = Node(id_new, string_new, p1_new, p2_new, level_new)
        
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
            generated_nodes.append([id_new, string_new, p1_new, p2_new, level_new])
            game_tree.add_edge(current_node[0], id_new)
        else:
            j -= 1
            game_tree.add_edge(current_node[0], game_tree.nodes[i].id)
     
game_tree = Tree()
generated_nodes = []
game_tree.add_node(Node('A1', '1632416324', 0, 0, 1))
# 16324 should be replaced with the generated string
# from string_generator class
generated_nodes.append(['A1', '1632416324', 0, 0, 1])

j = 2
while len(generated_nodes) > 0:
    current_node = generated_nodes[0]
    ptr = 0
    while ptr < len(current_node[1]) - 1:
        check_step('1', generated_nodes, current_node, ptr)
        ptr += 2
    check_step('2', generated_nodes, current_node, ptr)
    generated_nodes.pop(0)

for x in game_tree.nodes:
    print(x.id,x.string,x.p1,x.p2,x.level,x.heu)

for x, y in game_tree.edges.items():
    print(x, y)