#pygame music

import os, pygame
from pygame.locals import *
from sys import exit
from random import *

__des__ = '''
    Name:
        PyMusic
    Feature(s):
        1.Add state bar and something information
          eg:author information,volume state...
        2.The volume can be around the keyboard direction
          key(LEFT, RIGHT) controls.
        3.Add four circles in the screen
        4.Draw the Play button and Stop button
'''
__version__ = '2.0'
__author__ = {'name' : 'Hongten',
              'mail' : 'hongtenzone@foxmail.com',
              'blog' : 'http://www.cnblogs.com/hongten',
              'version' : __version__}

if not pygame.mixer: print('Warning, sound disabled!')
if not pygame.font: print('Warning, fonts disabled!')

pygame.init()

SCREEN_W = 580
SCREEN_H = 450
SCREEN_DEFAULT_SIZE = (SCREEN_W, SCREEN_H + 20)
VOLUME = 5
IMAGE_START_POS = (60, 60)
IMAGE_END_POS = (245, 245)
CIRCLES_POS = [(85, 350), (150, 350), (215, 350), (280, 350), (555, 425)]
CIRCLR_R = 25
CIRCLR_W = 3

PLAY_FLAG = True
PREFER_FLAG = True


DATA_DIR = 'data'
IMAGE_DIR = 'image'
BG_IMAGE_DIR = 'image\\background'
FONT_DIR = 'font'
SOUND_DIR = 'sound'

BG_IMAGE = 'bg.jpg'
AUTHOR_IMAGE = 'author.png'
#size:(240*240)
BGS = []
SONG_FLAG = 0
SONGS = [('1.OGG', 'You Raise Me Up', 'WestLife', '1.png'),
         ('2.OGG', '不完整的旋律', '王力宏', '2.png'),
         ('3.OGG', 'A Place Nearby' , 'Lene Marlin', '3.png'),
         ('4.OGG', 'Just Give Me A Reason' , 'Pink', '4.png'),
         ('5.OGG', '我 ' , '张国荣', '5.png'),
         ('6.OGG', '大城小爱' , '王力宏', '6.png'),
         ('7.OGG', '聊天' , '郭静', '7.png')]
westlift = 'westlife.png'

VOLUME_POINTS = []
VOLUME_POINTS_START = []
VOLUME_RECT_COLORS = []
for p in range(170, 250, 7):
    VOLUME_POINTS.append([SCREEN_W - p,SCREEN_H + 20])
for ps in range(175, 250, 7):
    VOLUME_POINTS_START.append([SCREEN_W - ps, SCREEN_H])
    VOLUME_RECT_COLORS.append((randint(0, 255), randint(0, 255), randint(0, 255)))

screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
bg = pygame.image.load(os.path.join(DATA_DIR, BG_IMAGE_DIR, BG_IMAGE)).convert()
author_image = pygame.image.load(os.path.join(DATA_DIR, IMAGE_DIR, AUTHOR_IMAGE)).convert()

SONG_ARRAY = []
SONG_IMAGE = []
for song in range(len(SONGS)):
    SONG_ARRAY.append(pygame.mixer.Sound(os.path.join(DATA_DIR, SOUND_DIR, SONGS[song][0])))
    SONG_IMAGE.append(pygame.image.load(os.path.join(DATA_DIR, IMAGE_DIR, SONGS[song][3])).convert())

font = pygame.font.Font(os.path.join(DATA_DIR, FONT_DIR, 'TORK____.ttf'), 14)
font_song_title = pygame.font.Font(os.path.join(DATA_DIR, FONT_DIR, 'msyhbd.ttf'), 24)
font_song = pygame.font.Font(os.path.join(DATA_DIR, FONT_DIR, 'msyh.ttf'), 16)

def draw_picture_rect():
     #picture rect
    pygame.draw.rect(screen,
                     (255, 255, 255),
                     Rect(IMAGE_START_POS, IMAGE_END_POS))

def button_play(screen, color):
    pygame.draw.circle(screen, color, CIRCLES_POS[0], CIRCLR_R, CIRCLR_W)
    points=[(77,340),(77,360),(95,350)]
    pygame.draw.polygon(screen,color,points)

def button_stop(screen, color):
    pygame.draw.circle(screen, color, CIRCLES_POS[0], CIRCLR_R, CIRCLR_W)
    pygame.draw.rect(screen,
                     color,
                     Rect(77, 340, 5, 23 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(88, 340, 5, 23 ))

def button_perfer(screen, color):
    pygame.draw.circle(screen, color, CIRCLES_POS[1], CIRCLR_R, CIRCLR_W)
    points=[(138,340),(162,340),(150,363)]
    pygame.draw.polygon(screen,color,points)

def button_del(screen, color):
    pygame.draw.circle(screen, color, CIRCLES_POS[2], CIRCLR_R, CIRCLR_W)
    pygame.draw.circle(screen, color, (215, 340), 6, 3)
    pygame.draw.rect(screen,
                     color,
                     Rect(200, 340, 30, 6 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(204, 340, 3, 20 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(210, 340, 3, 20 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(217, 340, 3, 20 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(223, 340, 3, 20 ))
    pygame.draw.rect(screen,
                     color,
                     Rect(204, 360, 22, 5 ))

def button_next_song(screen, color):
    pygame.draw.circle(screen, color, CIRCLES_POS[3], CIRCLR_R, CIRCLR_W)
    points_one =[(270,343),(270,357),(277,350)]
    points_two =[(277,343),(277,357),(284,350)]
    pygame.draw.polygon(screen,color,points_one)
    pygame.draw.polygon(screen,color,points_two)
    pygame.draw.rect(screen,
                     color,
                     Rect(284, 343, 5, 15 ))

def button_authon_image(screen, color):
     pygame.draw.circle(screen, color, CIRCLES_POS[4], CIRCLR_R, CIRCLR_W)
     pygame.draw.rect(screen,
                     (255, 255, 255),
                     Rect(418, 248, 144, 154 ))
     screen.blit(author_image, (420, 250))
     luck = font_song_title.render('Yes, You are Luck :-)', True, (255,165,10))
     screen.blit(luck, (280, 416))

def listener():
    global PLAY_FLAG
    global PREFER_FLAG
    x, y = pygame.mouse.get_pos()
    color = (255,255,25)
    color_red = (230, 0, 0)
    for index in range(len(CIRCLES_POS)):
        p_x = (CIRCLES_POS[index][0] - x)**2
        p_y = (CIRCLES_POS[index][1] - y)**2
        p_r = (CIRCLR_R)**2
        if (p_x + p_y <= p_r):
            if index == 0 and PLAY_FLAG:
                button_stop(screen, color)
            elif index == 0 and not PLAY_FLAG:
                button_play(screen, color)
            elif index == 1 and PREFER_FLAG:
                button_perfer(screen, color)
            elif index == 1 and not PREFER_FLAG:
                button_perfer(screen, color_red)
            elif index == 2:
                button_del(screen, color)
            elif index == 3:
                button_next_song(screen, color)
            elif index == 4:
                button_authon_image(screen, color)

def mouse_down_listener(sound):
    global PLAY_FLAG
    global PREFER_FLAG
    global SONG_FLAG
    x, y = pygame.mouse.get_pos()
    for index in range(len(CIRCLES_POS)):
        p_x = (CIRCLES_POS[index][0] - x)**2
        p_y = (CIRCLES_POS[index][1] - y)**2
        p_r = (CIRCLR_R)**2
        if (p_x + p_y <= p_r):
            if index == 0 and PLAY_FLAG:
                #print('stop now......')
                sound.stop()
                PLAY_FLAG = False
            elif index == 0 and not PLAY_FLAG:
                #print('play now ... ... ... ...')
                sound.play(0)
                PLAY_FLAG = True
            elif index == 1 and PREFER_FLAG:
                print('perfer song....<<', SONGS[SONG_FLAG][1], '>>')
                PREFER_FLAG = False
            elif index == 1 and not PREFER_FLAG:
                print('not perfer song... <<', SONGS[SONG_FLAG][1], '>>')
                PREFER_FLAG = True
            elif index == 2:
                sound.stop()
                print('delete song....<<', SONGS[SONG_FLAG][1], '>>')
                if SONG_FLAG > 0:
                    SONGS.pop(SONG_FLAG)
                    SONG_IMAGE.pop(SONG_FLAG)
                    SONG_ARRAY.pop(SONG_FLAG)
                    if SONG_FLAG >= len(SONGS) - 1:
                        SONG_FLAG -= 1
                else:
                    print('This is the last song.')
            elif index == 3:
                sound.stop()
                if SONG_FLAG < len(SONGS) - 1:
                    SONG_FLAG += 1
                else:
                    SONG_FLAG = 0
                #print('next song....')
                
def draw_button(sound):
    color = (255,255,255)
    color_red = (230, 0, 0)
    #play or stop
    if PLAY_FLAG:
        sound.play(0)
        button_stop(screen, color)
    elif not PLAY_FLAG:
        button_play(screen, color)
    #perfer song
    if PREFER_FLAG:
        button_perfer(screen, color)
    elif not PREFER_FLAG:
        button_perfer(screen, color_red)
    #delete
    button_del(screen, color)
    #next song
    button_next_song(screen, color)

def draw_volume_info():
    #the background of volume
    pygame.draw.rect(screen,
                     (255, 255, 255),
                     Rect((VOLUME_POINTS_START[-1][0],
                           VOLUME_POINTS_START[-1][1]),
                          (VOLUME_POINTS[-10][0] - VOLUME_POINTS_START[-1][0],
                           20)))
    #the size of volume
    for v in range(VOLUME+1):
        if v > 0:
            pygame.draw.rect(screen,
                             VOLUME_RECT_COLORS[v],
                             Rect((VOLUME_POINTS_START[-v][0],
                                   VOLUME_POINTS_START[-v][1]),
                                  (VOLUME_POINTS[-v][0] - VOLUME_POINTS_START[-v][0],
                                   20)))

def draw_song_title():
    title = font_song_title.render(SONGS[SONG_FLAG][1], True, (255,165,0))
    songer = font_song.render(SONGS[SONG_FLAG][2], True, (255, 255, 255))
    screen.blit(title, (320, 60))
    screen.blit(songer, (320, 110))

def draw_state_bar_info():
    pygame.draw.line(screen, (165,42,42),(0, SCREEN_H), (SCREEN_W, SCREEN_H))
    #music info
    music_info = 'AllSongs: ' + str(len(SONGS)) +'     Current: ' + str(SONG_FLAG + 1)
    text = font.render(music_info, True, (255,255,255))
    screen.blit(text, (0, SCREEN_H+5))
    #author into
    author_info = font.render('hongtenzone@foxmail.com', True, (255,255,255))
    screen.blit(author_info, (SCREEN_W - 160, SCREEN_H+5))
    #volume info
    volume_text = font.render('Volume: ' + str(VOLUME), True, (255, 255, 255))
    screen.blit(volume_text, (SCREEN_W - 310, SCREEN_H+5))
    
while True:
    
    screen.blit(bg, (0, 0))
    pic = SONG_IMAGE[SONG_FLAG]
    bg_sound = SONG_ARRAY[SONG_FLAG]
    bg_sound.set_volume(0.1 * VOLUME)
    draw_button(bg_sound)
    listener()
    for event in pygame.event.get():
        if event.type == QUIT:
            bg_sound.stop()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pass
            elif event.key == K_DOWN:
                pass
            elif event.key == K_LEFT:
                if VOLUME > 0:
                    VOLUME -= 1
            elif event.key == K_RIGHT:
                if VOLUME <= 9:
                    VOLUME += 1
        elif event.type == MOUSEMOTION:
            pass
                    
        elif event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0: #When the LEFT button down
                        mouse_down_listener(bg_sound)

    #picture rect
    draw_picture_rect()
    #volume information
    draw_volume_info()
    #state bar information
    draw_state_bar_info()
    #song title
    draw_song_title()
    
    screen.blit(pic, (62.5, 62.5))
    pygame.display.update()
