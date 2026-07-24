game_is_on = True
while game_is_on:
    screen.update()
    paddle1.move()
    paddle2.move()
    if ball.direction == "left":
        ball.move_left()
    else:
        ball.move_right()