import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")  #p.49
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  #p.61 よく使う
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tori_img = pg.image.load("fig/3.png")   #★２
    tori_img = pg.transform.flip(tori_img, True, False)
    #★8
    tori_rct = tori_img.get_rect()
    tori_rct.center = 300, 200
    tmr = 0  #タイマー

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #8-3
        if key_lst[pg.K_UP]:
            tori_rct.move_ip((-1, -1))
        if key_lst[pg.K_DOWN]:
            tori_rct.move_ip((-1, 1))
        if key_lst[pg.K_LEFT]:
            tori_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            tori_rct.move_ip((1, 0)) 
        else:
            tori_rct.move_ip((-1, 0))
        
        
        x = -(tmr%3200)
        #背景
        screen.blit(bg_img, [x, 0])  #読み込んだ画像を貼り付け(blit), 基本的にループの中
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        #こうかとん
        #screen.blit(tori_img, [300, 200])  #★４
        screen.blit(tori_img, tori_rct) #8-3
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()