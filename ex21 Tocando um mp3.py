#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init() #inicia a biblioteca
pygame.mixer.music.load("ex01.mp3") #Carrega a musica OBS:não adicionei nenhum arquivo de musica para testar
pygame.mixer.music.play() #Inicia a musica
pygame.event.wait() #Comando para esperar a musica terminar para parar de rodar