import pygame

def starting_screen(screen, scr_w, text_font):
    screen.fill('black')

    top_text = text_font.render('Arkanoid',False,'blue')
    top_text_rect = top_text.get_rect(center = (scr_w/2, 100))

    bottom_text = text_font.render('Press "Space" to start!',False,'blue')
    bottom_text_rect = bottom_text.get_rect(center = (scr_w/2, 250))

    screen.blit(top_text, top_text_rect)
    screen.blit(bottom_text, bottom_text_rect)

def bouncing(ball, scr_w, scr_h, tables, table, level):
    ball.update()

    if ball.rect.right > scr_w or ball.rect.left < 0:
        ball.x_speed *= -1
    if ball.rect.top < 0 or ball.rect.bottom  > scr_h:
        ball.y_speed *= -1

    collision_range = 5

    collision_sprites = pygame.sprite.spritecollide(ball, tables, False)

    if collision_sprites:
        if abs(table.rect.top - ball.rect.bottom) < collision_range and ball.y_speed > 0:
            ball.y_speed *= -1
        if abs(table.rect.left - ball.rect.right) < collision_range and ball.x_speed > 0:
            ball.x_speed *= -1
        if abs(table.rect.right - ball.rect.left) < collision_range and ball.x_speed < 0:
            ball.x_speed *= -1
        
    collision_sprites_tiles = pygame.sprite.spritecollide(ball, level.blocks, True)

    if collision_sprites_tiles:
        for block in level.blocks:
            if block.rect.bottom <= ball.rect.top and ball.y_speed < 0:
                ball.y_speed *= -1
            if block.rect.top >= ball.rect.bottom and ball.y_speed > 0:
                ball.y_speed *= -1
            if block.rect.left <= ball.rect.right and ball.x_speed < 0:
                ball.x_speed *= -1
            if block.rect.right >= ball.rect.left and ball.x_speed > 0:
                ball.x_speed *= -1