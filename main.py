import random
import keyboard
import os
from colorama import Fore, Style, init
from dataclasses import dataclass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class OIDMatrix:
    matrix: list
    position: tuple
    visited: list
    food: tuple
    direction: str = "RIGHT"
    game_over: bool = False

    def move(self):
        if self.game_over:
            return False
        
        x, y = self.position
        
        if self.direction == "UP":
            next_pos = (x - 1, y)
        elif self.direction == "DOWN":
            next_pos = (x + 1, y)
        elif self.direction == "LEFT":
            next_pos = (x, y - 1)
        elif self.direction == "RIGHT":
            next_pos = (x, y + 1)
        
        if (next_pos[0] < 0 or next_pos[0] >= len(self.matrix) or
            next_pos[1] < 0 or next_pos[1] >= len(self.matrix[0]) or
            next_pos in self.visited):
            print("Game Over: Snake hit the boundary or itself")
            self.game_over = True
            return False
        
        self.position = next_pos
        self.visited.append(self.position)
        
        if self.position == self.food:
            self.spawn_food()
        else:
            if len(self.visited) >= len(self.matrix) * len(self.matrix[0]):
                print("Congrats: You Win!")
                self.game_over = True
                return False
            self.visited.pop(0)
        
        return True

    def spawn_food(self):
        available_positions = [(i, j) for i in range(len(self.matrix)) for j in range(len(self.matrix[0])) if (i, j) not in self.visited]
        if available_positions:
            self.food = random.choice(available_positions)
        else:
            self.food = None

    def reset_game(self):
        self.position = (0, 0)
        self.visited = [self.position]
        self.direction = "RIGHT"
        self.game_over = False
        self.spawn_food()
        clear_screen()
        self.display()
    
    def display(self):
        print("----------------------------------------------------------")
        print("Moved to", self.matrix[self.position[0]][self.position[1]])
        print("Snake length:", len(self.visited))
        
        snake_data = [self.matrix[i][j] for i, j in self.visited]
        print("Snake Data:", snake_data)
        
        grid = [[Fore.RED + "+" + Style.RESET_ALL if (i, j) == self.food else Fore.BLUE + "-" + Style.RESET_ALL 
            for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for idx, (i, j) in enumerate(self.visited):
            if idx == 0:
                grid[i][j] = Fore.RED + "T" if len(self.visited) > 1 else Fore.BLUE + "S"
            elif idx == len(self.visited) - 1:
                grid[i][j] = Fore.GREEN + "H"
            else:
                grid[i][j] = Fore.YELLOW + "O"
        
        if self.food:
            fx, fy = self.food
            grid[fx][fy] = Fore.RED + "+"
        
        for row in grid:
            print(" ".join(row))
        
        if self.food:
            print("Food is at:", self.matrix[self.food[0]][self.food[1]])

base_oid = ".1.3.6.1.2.1.2.2.1.7."

oid_matrix = OIDMatrix([
    [str(base_oid + str(i)) for i in range(1, 24, 2)],
    [str(base_oid + str(i)) for i in range(2, 25, 2)]
], position=(0, 0), visited=[(0, 0)], food=None)

oid_matrix.spawn_food()

def on_key_event(e):
    if oid_matrix.game_over and e.name == "r":
        oid_matrix.reset_game()
        return
    elif oid_matrix.game_over and e.name == "x":
        print("Exit!")
        os._exit(0)
    
    opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
    
    if e.name == "up" and oid_matrix.direction != opposite_directions.get("UP"):
        oid_matrix.direction = "UP"
    elif e.name == "down" and oid_matrix.direction != opposite_directions.get("DOWN"):
        oid_matrix.direction = "DOWN"
    elif e.name == "left" and oid_matrix.direction != opposite_directions.get("LEFT"):
        oid_matrix.direction = "LEFT"
    elif e.name == "right" and oid_matrix.direction != opposite_directions.get("RIGHT"):
        oid_matrix.direction = "RIGHT"
    else:
        print("Incorrect movement")
        return
    
    if not oid_matrix.move():
        print("Press 'R' to restart the game.")
        print("Press 'X' to exit the game.")
        return
    
    clear_screen()
    oid_matrix.display()

keyboard.on_press(on_key_event)

oid_matrix.display()
keyboard.wait()
