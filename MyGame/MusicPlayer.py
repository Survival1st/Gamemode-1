import pygame
import os
import sys

def main():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Music Player")
    font = pygame.font.SysFont("Arial", 24)
    
    music_dir = "assets"
    songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
    
    if not songs:
        sys.exit()

    current_track_idx = 0
    is_playing = False

    def play_song():
        pygame.mixer.music.load(os.path.join(music_dir, songs[current_track_idx]))
        pygame.mixer.music.play()

    running = True
    while running:
        screen.fill((30, 30, 30))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if not is_playing:
                        play_song()
                        is_playing = True
                    else:
                        pygame.mixer.music.unpause()
                
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                
                elif event.key == pygame.K_n:
                    current_track_idx = (current_track_idx + 1) % len(songs)
                    play_song()
                    is_playing = True
                
                elif event.key == pygame.K_b:
                    current_track_idx = (current_track_idx - 1) % len(songs)
                    play_song()
                    is_playing = True
                
                elif event.key == pygame.K_q:
                    running = False

        track_text = font.render(f"Track: {songs[current_track_idx]}", True, (255, 255, 255))
        controls_text = font.render("P: Play | S: Pause | N: Next | B: Back | Q: Quit", True, (200, 200, 200))
        
        screen.blit(track_text, (50, 150))
        screen.blit(controls_text, (50, 250))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()