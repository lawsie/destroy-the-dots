# Write your code here :-)
from guizero import App, Waffle, Text, PushButton
from random import randint
 
# Light up a pixel
def light():
    global speed, lit
    
    # Find a pixel that isn't lit yet and light it
    x, y = randint(0,4), randint(0,4)
    while board[x, y].dotty == True:
        x, y = randint(0,4), randint(0,4)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")
    lit += 1
    
    # Speed up more when the player is struggling!
    if lit > 0 and lit < 3:
        speed = 600
    elif lit >= 3 and lit < 6:
        speed = 500
    elif lit >= 6 and lit < 9:
        speed = 400
    else:
        speed = 300
    
    # Check whether the player lost the game
    all_pixels = board.get_all()
    if all(pixel == all_pixels[0] for pixel in all_pixels):
        message.value = "You have been destroyed by dots"
        reset_button.enable()
    else:
        board.after(speed, light)

# When a pixel is clicked, turn it off again
def turn_off(x, y):
    global score
    if board[x,y].dotty == True:
        score += 1  # Only score a point if it was actually a dot
        score_text.value = "Score: " + str(score)
    board[x,y].dotty = False
    board.set_pixel(x, y, "white")

# Reset the board
def reset():
    global score
    for i in range(board.width):
        for j in range(board.height):
            board[i,j].dotty = False
            board[i,j].color = "white"
    # Restart the game
    score = 0
    score_text.value = "Score: 0"
    board.after(speed, light)
    reset_button.disable()

# Keep track of the pixels
lit = 0
speed = 1000
score = 0

# Create the GUI
app = App()
instructions = Text(app, "Click the dots to destroy them")
board = Waffle(app, width=5, height=5, command=turn_off)
message = Text(app)
score_text = Text(app, text="Score: 0")
reset_button = PushButton(app, reset, text="New game")
reset_button.disable()
# Light a new pixel after a given interval
board.after(speed, light)
app.display()