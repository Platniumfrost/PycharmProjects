### under Game functions ###
###under draw text 1 ###
def draw_bar(surf,x,y,pct):
    if pct < 0:
        pct = 0
    bar_len = 200
    bar_height = 40
    fill = (pct/100)*bar_len
    outline_rect = pg.Rect(x,y,bar_len,bar_height)
    fill_rect = pg.Rect(x,y,fill, bar_height)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect,2)
    pass


draw_bar(screen, 5, 10, player.sheild)
#pg.display.flip()

###under class player###
#under super(player...)
self.sheild = 100
#under self.speedx
self.shoot_delay = 250
self.last_shot = pg.time.get_ticks()



###under r.choice(expl_sounds).play()###
## change 'if hits' to 'for hit in hits:'
player.sheild -= hits.radius*2
if player.sheild <= 0:
    playing = False


### under def shoot(self):####
if now - self.last_shot > self.shoot_delay:
    pass
    b = Bullet(self.)


