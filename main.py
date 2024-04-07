#Izmantotie resursi:
#https://stackoverflow.com/questions/38539617/tkinter-check-if-text-widget-is-empty

import random
from tkinter import *
from tkinter import Canvas, Button, PhotoImage
from tkinter import messagebox
from alpha_beta_solver import AlphaBetaSolver
from game_tree import DEPTH, GameTree
from minimax_solver import MinimaxSolver
from string_generator import Generator

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Numeric Game")
        
        self.canvas = Canvas(
            window,
            bg = "#1A1A1A",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        
        self.image_1 = PhotoImage(file=self.add_to_path("image_1.png"))
        self.canvas.create_image(1764.65, 761.75, image=self.image_1)

        self.canvas.create_text(
            424.25,
            186.0,
            anchor="nw",
            text="Spēles Noteikumi",
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 24 * -1)
        )

        self.canvas.create_text(
            216.25,
            228.75,
            anchor="nw",
            text="Spēles sākumā ir dota ģenerētā skaitļu virkne. Katram spēlētājam ir 0 punktu spēles sākumā.",
            fill="#FFFFFF",
            font=("AnonymousPro Regular", 13 * -1)
        )

        self.canvas.create_text(
            216.25,
            264.75,
            anchor="nw",
            text="Gājiena laikā spēlētājs var - saskaitīt skaitļu pāri un summu ierakstīt saskaitīto skaitļu pāra  vietā\nkā arī pieskaitīt savam punktu skaitam 1 punktu, VAI nodzēst to skaitli, kas ir palicis bez pāra\nun atņemt vienu punktu no sava punktu skaita.",
            fill="#FFFFFF",
            font=("AnonymousPro Regular", 13 * -1)
        )

        self.canvas.create_text(
            216.25,
            330.75,
            anchor="nw",
            text="Spēle beidzas, kad skaitļu virknē paliek viens skaitlis. Uzvar spēlētājs, kam ir vairāk punktu.",
            fill="#FFFFFF",
            font=("AnonymousPro Regular", 13 * -1)
        )

        self.canvas.create_rectangle(
            105.75,
            464.25,
            914.25,
            508.25,
            fill="#FFFFFF",
            outline=""
        )
        
        self.user_flag = None
        self.minimax_flag = None
        self.user_score = 0
        self.computer_score = 0
        self.move = 1
        
        self.text = Text(height=1.2, width=47, font=('Times New Roman',25))
        
        self.button_image_1 = PhotoImage(file=self.add_to_path("button_1.png"))
        self.button_delete = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.clear_string,
            relief="flat"
        )
        self.button_delete.place(x=105.75, y=526.75, width=133.5, height=39.0)
        
        self.button_image_2 = PhotoImage(
            file=self.add_to_path("button_2.png"))
        self.button_confirm = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.confirm,
            relief="flat"
        )
        self.button_confirm.place(x=400.5, y=519.25, width=216.75, height=54.0)
        
        self.button_image_3 = PhotoImage(
            file=self.add_to_path("button_3.png"))
        self.button_restart = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.restart,
            relief="flat"
        )
        self.button_restart.place(x=780.75, y=526.75, width=133.5, height=39.0)
        
        self.button_image_4 = PhotoImage(
            file=self.add_to_path("button_4.png"))
        self.button_start = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.start,
            relief="flat"
        )
        self.button_start.place(x=443.25, y=407.0, width=133.5, height=39.0)
        
        self.canvas.create_text(
            831.25,
            416.0,
            anchor="nw",
            text="USER",
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 18 * -1)
        )

        self.user_score_text = self.canvas.create_text(
            894.0,
            401.0,
            anchor="nw",
            text=str(self.user_score),
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 36 * -1)
        )
        
        self.canvas.create_text(
            105.75,
            416.0,
            anchor="nw",
            text="COMPUTER",
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 18 * -1)
        )

        self.computer_score_text = self.canvas.create_text(
            227.25,
            401.75,
            anchor="nw",
            text=str(self.computer_score),
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 36 * -1)
        )

        self.canvas.create_text(
            149.625,
            57.0,
            anchor="nw",
            text="Choose who starts",
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 24 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=self.add_to_path("button_5.png"))
        self.button_user = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.play_user,
            relief="flat"
        )
        self.button_user.place(x=113.5, y=106.75, width=133.5, height=39.0)

        self.button_image_6 = PhotoImage(
            file=self.add_to_path("button_6.png"))
        self.button_computer = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.play_computer,
            relief="flat"
        )
        self.button_computer.place(x=285.0, y=106.75, width=133.5, height=39.0)

        self.canvas.create_text(
            651.75,
            57.0,
            anchor="nw",
            text="Choose algorithm",
            fill="#FFFFFF",
            font=("AnonymousPro Bold", 24 * -1)
        )

        self.button_image_7 = PhotoImage(
            file=self.add_to_path("button_7.png"))
        self.button_minimax = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.play_minimax,
            relief="flat"
        )
        self.button_minimax.place(x=599.25, y=106.75, width=133.5, height=39.0)

        self.button_image_8 = PhotoImage(
            file=self.add_to_path("button_8.png"))
        self.button_alpha_beta = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.play_alpha_beta,
            relief="flat"
        )
        self.button_alpha_beta.place(x=780.75, y=106.75, width=133.5, height=39.0)

    def start(self):
        if not (self.user_flag == None or self.minimax_flag == None):
            if not len(self.text.get("1.0", "end-1c")) == 0:
                return messagebox.showwarning("Warning", "Press 'Delete' first") 
            
            self.correct_string = Generator.generate_string()
            self.text.insert(END, self.correct_string)
            self.text.place(x=108, y=465)
            
            tree = GameTree.construct_tree(self.correct_string)
            
            if (self.minimax_flag):
                self.modified_tree = MinimaxSolver.minimax(tree)
            else:
                self.modified_tree = AlphaBetaSolver.alpha_beta(tree)

            self.computer_score = 0
            self.user_score = 0
            self.move = 1
            
            if not (self.user_flag):
                best_node = self.choose_best_node()

                self.best_node_id = best_node.id
                self.correct_string = best_node.string
                # saves string for the upcoming user move check
                
                self.clear_string()
                self.text.insert(END, self.correct_string)
                self.text.place(x=108, y=465)
                
                self.computer_score = best_node.p1
                
                self.canvas.itemconfigure(self.computer_score_text, text=self.computer_score)
                self.move += 1

                self.start_after_user = False
            else:
                # to see if we need to re-generate the tree
                self.start_after_user = True
                # to check the first user move
                self.best_node_id = self.modified_tree.nodes[0]

            
        else:
            return messagebox.showwarning("Warning", "Please prepare well")
        
    def choose_best_node(self, valid_node=None):
        # root node scenario
        if (valid_node == None):
            valid_node = self.modified_tree.nodes[0]
        
        print(valid_node.id)
        
        children_nodes = self.modified_tree.edges.get(valid_node.id)  
        best_heu = valid_node.heu
        
        best_children = []
        for children_node in children_nodes:
            if (children_node.heu == best_heu):
                best_children.append(children_node)
        
        best_node = self.shuffle(best_children)
        
        return best_node
        
        
    def shuffle(self, best_children):
        index = random.randint(0, len(best_children)-1)
        return best_children[index]
    
    def confirm(self):
        if not (self.user_flag == None or self.minimax_flag == None):
            if len(self.text.get("1.0", "end-1c")) == 0:
                return messagebox.showwarning("Warning", "Press 'Start' first") 
              
            # user logic
            string = self.text.get("1.0", "end-1c")
            self.valid_node = self.check_valid_move(string)
            
            if (self.valid_node == None):
                self.clear_string()
                self.text.insert(END, self.correct_string)
                self.text.place(x=108, y=465)
                return messagebox.showwarning("Warning", "Please follow the rules") 

            self.user_score = self.valid_node.p2
            self.canvas.itemconfigure(self.user_score_text, text=self.user_score)
            self.move += 1
            
            self.check_if_to_reconstruct_tree()
            
            # computer logic
            best_node = self.choose_best_node(self.valid_node)
            self.best_node_id = best_node.id
            self.correct_string = best_node.string
            
            self.clear_string()
            self.text.insert(END, self.correct_string)
            self.text.place(x=108, y=465)
            
            self.computer_score = best_node.p1
            
            self.canvas.itemconfigure(self.computer_score_text, text=self.computer_score)
            self.move += 1
            
            # self.check_if_to_reconstruct_tree()
            
        else:
            return messagebox.showwarning("Warning", "Please prepare well")  
        
    def check_valid_move(self, string):
        possible_moves = self.modified_tree.edges.get(self.best_node_id)
        valid_node = None
        
        for move in possible_moves:
            if (move.string == string):
                valid_node = move
                break
            
        return valid_node
    
    def check_if_to_reconstruct_tree(self):
        if(self.move % DEPTH == 0 or self.start_after_user):
            tree = GameTree.construct_tree(self.correct_string, self.computer_score, self.user_score)

            self.check_DEPTH() !!!!!!!!!!

            if (self.minimax_flag):
                self.modified_tree = MinimaxSolver.minimax(tree)
            else:
                self.modified_tree = AlphaBetaSolver.alpha_beta(tree)

            self.start_after_user = False
            self.valid_node = None
            self.move = 1
            
    def clear_string(self):
        self.text.delete(1.0, END)
        
    def play_user(self):
        if (self.user_flag == None):
            self.user_flag = True
            self.button_image_9 = PhotoImage(
                file=self.add_to_path("button_9.png"))
            self.button_user.config(image=self.button_image_9)
        else:
            return messagebox.showwarning("Warning", "Player has already been chosen")
    
    def play_computer(self):
        if (self.user_flag == None):
            self.user_flag = False
            self.button_image_6 = PhotoImage(
                file=self.add_to_path("button_10.png"))
            self.button_computer.config(image=self.button_image_6)
        else:
            return messagebox.showwarning("Warning", "Player has already been chosen")
        
    def play_minimax(self):
        if (self.minimax_flag == None):
            self.minimax_flag = True
            self.button_image_7 = PhotoImage(
                file=self.add_to_path("button_11.png"))
            self.button_minimax.config(image=self.button_image_7)
        else:
            return messagebox.showwarning("Warning", "Algorithm has already been chosen")
        
    def play_alpha_beta(self):
        if (self.minimax_flag == None):
            self.minimax_flag = False
            self.button_image_8 = PhotoImage(
                file=self.add_to_path("button_12.png"))
            self.button_alpha_beta.config(image=self.button_image_8)
        else:
            return messagebox.showwarning("Warning", "Algorithm has already been chosen")
    
    def restart(self):
        self.clear_string()
        self.user_flag = None
        self.minimax_flag = None
        self.button_image_5 = PhotoImage(
            file=self.add_to_path("button_5.png"))
        self.button_user.config(image=self.button_image_5)
        
        self.button_image_6 = PhotoImage(
            file=self.add_to_path("button_6.png"))
        self.button_computer.config(image=self.button_image_6)
        
        self.button_image_7 = PhotoImage(
            file=self.add_to_path("button_7.png"))
        self.button_minimax.config(image=self.button_image_7)
        
        self.button_image_8 = PhotoImage(
            file=self.add_to_path("button_8.png"))
        self.button_alpha_beta.config(image=self.button_image_8)
        
        self.canvas.itemconfigure(self.user_score_text, text=str(0))
        self.canvas.itemconfigure(self.computer_score_text, text=str(0))
        
        self.user_score = 0
        self.computer_score = 0
    
    def add_to_path(self, file_name):
        return "./assets/" + file_name

        
if __name__ == "__main__":
    window = Tk()
    window.geometry("1000x600")
    Main(window)
    window.mainloop()


    
