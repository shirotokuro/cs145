import pyglet, random, math
from game import player, resources, lvl1

game_window = pyglet.window.Window(1024, 600)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player1 = player.Player(lvl= lvl1.lvl1, x=30, y=50, batch=main_batch)
player2 = player.Player(lvl= lvl1.lvl1, x=30, y=150, batch=main_batch)
player2.set(2)

game_objects = [player1, player2]

# Tell the main window that the player object responds to events

game_window.push_handlers(player1.key_handler)
game_window.push_handlers(player2.key_handler)
pyglet.gl.glClearColor(0.16, 0.50, 0.72,1.0)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    lvl1.lvl1_bg()

def update(dt):
    for obj in game_objects:
        obj.update(dt)

if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
