import tkinter  # Bibliothèque GUI standard de Python
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOWS_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Fenêtre de jeu | Game window

window = tkinter.Tk()  # Crée la fenêtre principale
window.title("Nassim Snake")
window.resizable(False, False)  # Empêche le redimensionnement de la fenêtre

# Canvas : zone de dessin pour des formes et des graphismes
canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOWS_HEIGHT, border=0, highlightthickness=0)
canvas.pack()  # Ajoute le canvas à la fenêtre
window.update()

# Jeu | Game
snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5) # Début du serpent
food = Tile(TILE_SIZE * 10, TILE_SIZE * 10) # Nourriture   
snake_body = [] 

# Pour le contrôle
velocityX = 0
velocityY = 0

game_over = False
score = 0

def change_direction(e): #e = event
    # print(e) = affiche la touche pressée
    # print(e.keysym) = affiche le symbole de la touche pressée

    global velocityX, velocityY, game_over
    if(game_over):
        return 

    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
        
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1

    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0

    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
def move():
    global snake, food, snake_body, game_over, score
    if(game_over):
        return 
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOWS_HEIGHT):
        game_over = True
        return
    
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
    
    # Gestion des collisions 
    if (snake.x == food.x and snake.y == food.y): 
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    # Corps du serpent
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()
    
    canvas.delete("all")
    
    # Dessine le serpent
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "blue")
    
    #Dessine la nourriture 
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")
    
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "blue")
        
    if(game_over):
        canvas.create_text(85, 20, font = "Arial 20", text = "GAME OVER", fill = "white")
    else: 
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score : {score}", fill = "white")
    
    window.after(100, draw) #10 FPS
    
draw()

window.bind("<KeyRelease>", change_direction) # Pour les changements de directions avec les flèches
window.mainloop()  # Garde la fenêtre ouverte
