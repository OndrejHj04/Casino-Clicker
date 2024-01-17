import pygame
from Button import Button
from Label import Label
from Coins import Coins

pygame.init()

init_list = []

# Read of data
with open("storage.txt", "r") as file:
    for line in range(8):
        init_list.append(int(file.readline()))
        print(init_list[line])

# Initialize coins
coins = Coins(init_list[0], init_list[1], init_list[2], init_list[3], init_list[4], init_list[5], init_list[6],
              init_list[7])


# Save data
def save():
    with open("storage.txt", "w") as file_2:
        data = [coins.money, coins.click_level, coins.poker_level, coins.blackjack_level, coins.dice_level,
                coins.roulette_level, coins.baccarat_level, coins.automate_level]
        for one_data in data:
            file_2.write(f"{one_data}\n")


# Set up the display
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Casino Clicker")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 36)

# Initial time
coin_timer = pygame.time.get_ticks()

# Create a dictionary of labels for displaying the values of variables
labels = {
    'money_label': Label(font_size=36, color=(255, 255, 255), x=0, y=0, width=400, height=50),
    'income_label': Label(font_size=36, color=(255, 255, 255), x=0, y=50, width=400, height=50),
    'level_click_label': Label(font_size=36, color=(255, 255, 255), x=0, y=500, width=400, height=50),
    'level_poker_label': Label(font_size=36, color=(255, 255, 255), x=800, y=0, width=200, height=50),
    'level_blackjack_label': Label(font_size=36, color=(255, 255, 255), x=800, y=100, width=200, height=50),
    'level_dice_label': Label(font_size=36, color=(255, 255, 255), x=800, y=200, width=200, height=50),
    'level_roulette_label': Label(font_size=36, color=(255, 255, 255), x=800, y=300, width=200, height=50),
    'level_baccarat_label': Label(font_size=36, color=(255, 255, 255), x=800, y=400, width=200, height=50),
    'level_automate_label': Label(font_size=36, color=(255, 255, 255), x=800, y=500, width=200, height=50),
}


# Buttons
button_cookie = Button(0, 100, 400, 400, blue, "Cookie", coins.click)
button_click_update = Button(0, 550, 400, 50, blue, "upgrade", coins.click_level_up)
button_poker_update = Button(800, 50, 200, 50, blue, "upgrade", coins.poker_level_up)
button_blackjack_update = Button(800, 150, 200, 50, blue, "upgrade", coins.blackjack_level_up)
button_dice_update = Button(800, 250, 200, 50, blue, "upgrade", coins.dice_level_up)
button_roulette_update = Button(800, 350, 200, 50, blue, "upgrade", coins.roulette_level_up)
button_baccarat_update = Button(800, 450, 200, 50, blue, "upgrade", coins.baccarat_level_up)
button_automate_update = Button(800, 550, 200, 50, blue, "upgrade", coins.automate_level_up)

buttons = [
    button_cookie,
    button_click_update,
    button_poker_update,
    button_blackjack_update,
    button_dice_update,
    button_roulette_update,
    button_baccarat_update,
    button_automate_update
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for button clicks
        for button in buttons:
            button.check_click(event)

    # Update the text of the labels with the actual values of the variables
    labels['money_label'].update_text(f"Money: {coins.money}")
    labels['income_label'].update_text(f"Income: {coins.poker_value() + coins.blackjack_value() + coins.dice_value() + coins.roulette_value() + coins.baccarat_value() + coins.automate_value()}")
    labels['level_click_label'].update_text(f"Click: {coins.click_level}")
    labels['level_poker_label'].update_text(f"Poker: {coins.poker_level}")
    labels['level_blackjack_label'].update_text(f"Blackjack: {coins.blackjack_level}")
    labels['level_dice_label'].update_text(f"Dice: {coins.dice_level}")
    labels['level_roulette_label'].update_text(f"Roulette: {coins.roulette_level}")
    labels['level_baccarat_label'].update_text(f"Baccarat: {coins.baccarat_level}")
    labels['level_automate_label'].update_text(f"Automate: {coins.automate_level}")

    # Render and display the labels
    for label in labels.values():
        label.render(screen)

    # Draw buttons
    for button in buttons:
        button.draw(screen, font)

    # Draw status bar
    for x in range(coins.poker_level):
        rect = pygame.Rect(50*x+400, 0, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    for x in range(coins.blackjack_level):
        rect = pygame.Rect(50*x+400, 100, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    for x in range(coins.dice_level):
        rect = pygame.Rect(50*x+400, 200, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    for x in range(coins.roulette_level):
        rect = pygame.Rect(50*x+400, 300, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    for x in range(coins.baccarat_level):
        rect = pygame.Rect(50*x+400, 400, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    for x in range(coins.automate_level):
        rect = pygame.Rect(50*x+400, 500, 50, 100)
        pygame.draw.rect(screen, "green", rect)

    pygame.display.flip()

    # Check if one second has passed
    current_time = pygame.time.get_ticks()
    if current_time - coin_timer >= 1000:  # 1000 milliseconds = 1 second
        coins.money += coins.poker_value() + coins.blackjack_value() + coins.dice_value() + coins.roulette_value()\
                       + coins.baccarat_value() + coins.automate_value()
        coin_timer = current_time  # Reset the time

    save()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
