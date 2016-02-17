import sys, pygame


pygame.init()
black = (0,0,0)
width = 1280
height = 1024
window = pygame.display.set_mode((width, height),0,32)
window.fill(black)

while True:
    event = pygame.event.get()
    for e in event:
        print(e.key+"\n")
        if(e.key == "q"):
            pygame.quit()
            sys.exit()
    print("Char: "+c+"\n")
    
    
 
