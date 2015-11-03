import pygame
import pygame.locals
import sys
import random

def main():
	pygame.init()
	BandBalonEnJuego=False
	Blanco=(255,255,255)
	ventana=pygame.display.set_mode((500,500))
	pygame.display.set_caption("Laberinto")

	rectanguloUno=pygame.Rect(0,50,100,100)
	rectanguloDos=pygame.Rect(0,200,100,100)
	rectanguloTres=pygame.Rect(0,350,100,100)
	rectanguloCuatro=pygame.Rect(150,0,100,100)
	rectanguloCinco=pygame.Rect(150,150,100,50)
	rectanguloSeis=pygame.Rect(150,250,100,100)
	rectanguloSiete=pygame.Rect(150,400,100,100)
	rectanguloOcho=pygame.Rect(300,0,50,350)
	rectanguloNueve=pygame.Rect(400,0,100,100)
	rectanguloDiez=pygame.Rect(350,150,100,100)
	rectanguloOnce=pygame.Rect(400,300,100,150)
	rectanguloDoce=pygame.Rect(300,400,50,100)
	rectanguloAux=pygame.Rect(0,0,100,100)
	Salida=pygame.Rect(475,450,25,50)
	PosX=0
	PosY=0
	Avatar=pygame.Rect(PosX,PosY,10,10)

	bolitaMorada=pygame.image.load("BolaMorada.png")
	Winner=pygame.image.load("Winner.png")
	MensajePro=pygame.image.load("mensaje.png")
	AuxX=0
	AuxY=0
	#fuente=pygame.font.Font(None,30)
	#fuente2=pygame.font.Font(None,20)
	#texto=fuente.render("Ganaste",0,(0,255,0))
	#tutorial=fuente2.render("El avatar es",0,(0,0,255))
	#tutorial2=fuente2.render("el cuadro azul",0,(0,0,255))
	BandFin=False
	while True:
		
		ventana.fill(Blanco)
		
		
		pygame.draw.rect(ventana,(0,0,0),rectanguloUno)
		pygame.draw.rect(ventana,(0,0,0),rectanguloDos)
		pygame.draw.rect(ventana,(0,0,0),rectanguloTres)
		pygame.draw.rect(ventana,(0,0,0),rectanguloCuatro)
		pygame.draw.rect(ventana,(0,0,0),rectanguloCinco)
		pygame.draw.rect(ventana,(0,0,0),rectanguloSeis)
		pygame.draw.rect(ventana,(0,0,0),rectanguloSiete)
		pygame.draw.rect(ventana,(0,0,0),rectanguloOcho)
		pygame.draw.rect(ventana,(0,0,0),rectanguloNueve)
		pygame.draw.rect(ventana,(0,0,0),rectanguloDiez)
		pygame.draw.rect(ventana,(0,0,0),rectanguloOnce)
		pygame.draw.rect(ventana,(0,0,0),rectanguloDoce)
		pygame.draw.rect(ventana,(0,255,0),Salida)
		pygame.draw.rect(ventana,(0,0,255),Avatar)
		#ventana.blit(tutorial,(0,100))
		#ventana.blit(tutorial2,(0,120))
		ventana.blit(MensajePro,(0,50))
		if BandFin==True:
			ventana.blit(Winner,(0,0))
		if BandBalonEnJuego==False:
			AuxX=random.randrange(250,450)
			AuxY=random.randrange(250,450)
			rectanguloAux.move_ip(AuxX,AuxY)
			BandOk=False
			while BandOk==False:
				if rectanguloAux.colliderect(rectanguloUno) or rectanguloAux.colliderect(rectanguloDos) or rectanguloAux.colliderect(rectanguloTres) or rectanguloAux.colliderect(rectanguloCuatro) or rectanguloAux.colliderect(rectanguloCinco) or rectanguloAux.colliderect(rectanguloSeis) or rectanguloAux.colliderect(rectanguloSiete) or rectanguloAux.colliderect(rectanguloOcho) or rectanguloAux.colliderect(rectanguloNueve) or rectanguloAux.colliderect(rectanguloDiez) or rectanguloAux.colliderect(rectanguloOnce) or rectanguloAux.colliderect(rectanguloDoce):
					AuxX=random.randrange(250,300)
					AuxY=random.randrange(0,400)
					rectanguloAux.move_ip(AuxX,AuxY)
				else:
					#print "No"
					BandOk=True
			BandBalonEnJuego=True
		rectanguloAux=pygame.Rect(AuxX,AuxY,10,10)
		pygame.draw.rect(ventana,(255,255,255),rectanguloAux)
		ventana.blit(bolitaMorada,(AuxX,AuxY))
		
		rectArriba=pygame.Rect(AuxX,AuxY-5,10,3)
		pygame.draw.rect(ventana,(255,255,255),rectArriba)
		
		rectAbajo=pygame.Rect(AuxX,AuxY+15,10,3)
		pygame.draw.rect(ventana,(255,255,255),rectAbajo)
		
		rectIzq=pygame.Rect(AuxX-5,AuxY,3,10)
		pygame.draw.rect(ventana,(255,255,255),rectIzq)
		
		rectDer=pygame.Rect(AuxX+15,AuxY,3,10)
		pygame.draw.rect(ventana,(255,255,255),rectDer)
		
			
		pygame.display.update()
		(AntX,AntY)=(Avatar.left,Avatar.top)
		(AntX1,AntY1)=(rectanguloAux.left,rectanguloAux.top)
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					Avatar.move_ip(-10,0)
				if event.key==pygame.K_RIGHT:
					Avatar.move_ip(10,0)
				if event.key==pygame.K_DOWN:
					Avatar.move_ip(0,10)
				if event.key==pygame.K_UP:
					Avatar.move_ip(0,-10)
		
		if Avatar.colliderect(rectanguloUno) or Avatar.colliderect(rectanguloDos) or Avatar.colliderect(rectanguloTres) or Avatar.colliderect(rectanguloCuatro) or Avatar.colliderect(rectanguloCinco) or Avatar.colliderect(rectanguloSeis) or Avatar.colliderect(rectanguloSiete) or Avatar.colliderect(rectanguloOcho) or Avatar.colliderect(rectanguloNueve) or Avatar.colliderect(rectanguloDiez) or Avatar.colliderect(rectanguloOnce) or Avatar.colliderect(rectanguloDoce):
			(Avatar.left,Avatar.top)=(AntX,AntY)
		if rectanguloAux.colliderect(rectanguloUno) or rectanguloAux.colliderect(rectanguloDos) or rectanguloAux.colliderect(rectanguloTres) or rectanguloAux.colliderect(rectanguloCuatro) or rectanguloAux.colliderect(rectanguloCinco) or rectanguloAux.colliderect(rectanguloSeis) or rectanguloAux.colliderect(rectanguloSiete) or rectanguloAux.colliderect(rectanguloOcho) or rectanguloAux.colliderect(rectanguloNueve) or rectanguloAux.colliderect(rectanguloDiez) or rectanguloAux.colliderect(rectanguloOnce) or rectanguloAux.colliderect(rectanguloDoce):
			(AuxX,AuxY)=(AntX1-5,AntY1-5)
		if rectanguloAux.colliderect(Salida):
			#print "Gano"
			BandFin=True
		
			
		BandHecho=False
		if Avatar.colliderect(rectArriba):
			AuxY+=10
		if Avatar.colliderect(rectAbajo):
			AuxY-=10
		if Avatar.colliderect(rectIzq):
			AuxX+=10
		if Avatar.colliderect(rectDer):
			AuxX-=10
			
			

if __name__=="__main__":
	main()
