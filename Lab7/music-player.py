import pygame
import sys
import os

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")

tracks = [f for f in os.listdir("C://Code//python-files//python-univ//Lab7//tracks") if f.endswith(".mp3")]
paused = False
track_num = 0

def play_music(song_index):
    pygame.mixer.music.load(os.path.join("C://Code//python-files//python-univ//Lab7//tracks", tracks[song_index]))  
    pygame.mixer.music.play()
play_music(track_num)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if paused != True:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
            
            elif event.key == pygame.K_a: 
                track_num = (track_num + 1) % len(tracks)
                play_music(track_num)
            
            elif event.key == pygame.K_s:  
                track_num = (track_num - 1) % len(tracks)
                play_music(track_num)


    