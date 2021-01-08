import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("Grafiken/Hintergrund.jpg")
fenster = pygame.display.set_mode([600,600])
uhr = pygame.time.Clock()
pygame.display.set_caption("Mein Spiel")


spielerschaden = pygame.mixer.Sound("Geräusche/Spieler/Uffs.wav")

class spieler:
    def __init__(self,x,y,geschwindigkeit,richtung):
        self.leben = 100
        self.x = x
        self.y = y
        self.geschwindigkeit = geschwindigkeit
        self.dieRichtung = 0
        self.spielerbilder = [pygame.image.load("Grafiken/Figuren/Spieler/Spieler.png"),pygame.image.load("Grafiken/Figuren/Spieler/SpielerRechts.png"),pygame.image.load("Grafiken/Figuren/Spieler/SpielerLinks.png"),pygame.image.load("Grafiken/Figuren/Spieler/SpielerOben.png")]
        self.derSpieler = fenster.blit(self.spielerbilder[self.dieRichtung], (self.x,self.y))
    def laufen(self,richtung):
        if richtung == 3:
            self.y -= self.geschwindigkeit
            richtung = 3
        if richtung == 1:
            self.x += self.geschwindigkeit
            self.dieRichtung = 1
        if richtung == 0:
            self.y += self.geschwindigkeit
            self.dieRichtung = 0
        if richtung == 2:
            self.x -= self.geschwindigkeit
            self.dieRichtung = 2
        

def zeichnen():
    fenster.blit(hintergrund, (0,0))
    pygame.display.update()


linkeWand = pygame.draw.rect(fenster, (0,0,0), (-2,0,4,600), 0)
rechteWand = pygame.draw.rect(fenster, (0,0,0), (598,0,2,600), 0)
Wandoben = pygame.draw.rect(fenster, (0,0,0), (0,-2,600,4), 0)
Wandunten = pygame.draw.rect(fenster, (0,0,0), (0,598,600,2), 0)

spieler1= spieler(300,300,3,0)
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,38,44)
    gedrückt = pygame.key.get_pressed()
    if gedrückt[pygame.K_UP] and not spielerRechteck.colliderect(Wandoben):
        spieler1.laufen(3)
    if gedrückt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
        spieler1.laufen(1)
    if gedrückt[pygame.K_DOWN] and not spielerRechteck.colliderect(Wandunten):
        spieler1.laufen(0)
    if gedrückt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
        spieler1.laufen(2)
    zeichnen()
    uhr.tick(60)
