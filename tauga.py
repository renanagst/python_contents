import turtle
p = turtle.Pen()

p.pencolor("red") # Muda a cor da caneta
p.speed("fastest") # Muda a velocidade de desenho
p.pensize(3) # Muda o tamanho da caneta

count = 0
for i in range(10000):
	p.forward(i)
	p.right(145)

	if count == 5:
		p.clear() # Apaga tudo o que estiver desenhado até agora
		count = 0	

	count += 1


#Different colors and possibilities
#colors = ["red", "green", "blue"]
#colorIndex = 0

#for i in range(360):
#    p.pencolor(colors[colorIndex])
#    p.forward(i)
#    p.right(100)
#
#    if colorIndex < len(colors) - 1:
#        colorIndex += 1
#    else:
#        colorIndex = 0

#Things that are different 2 
#for i in range(50):
#    p.circle(i)
#    p.right(10)

#Things that are different
#for i in range(1000):
#    p.right(50)
#    p.forward(i)

#Circle with for i n
#for i in range(360):
#    p.right(1)
#    p.forward(1)

#how to make circles
#p.goto(0, 0) # Move a tartaruga para um local específico da tela
#p.circle(100) # Cria um círculo para você com diâmetro definido como parâmetro

#How to make a square below!
#p.forward(100)
#p.right(90)
#p.forward(100)
#p.right(90)
#p.forward(100)
#p.right(90)
#p.forward(100)
#p.right(90)

# Mover pra frente 50 pixels =  p.forward(50)
# Virar pra direita em 90 graus = p.right(90)
# Virar pra esquerda 180 graus = p.left(180) 
# Mover pra trás 50 pixels = p.backward(50) 