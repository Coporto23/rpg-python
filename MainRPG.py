
""" Proyecto RPG Prueba combate"""

""" Variables y estadisticas principales """

""" Estadisticas y datos jugador """
pjnombre = 'random'
pjvidamax = 100
pjvida = 100
pjataque = 20

hachaatk = 35
hachacrt = 0
espadaatk = 20
espadacrt = 0.5
dagaatk = 15
dagacrt = 0.2

""" Estadisticas enemigo generico """

envidamax = 50
envida = 50
enataque = 15

""" Menu """

contadormenu = 0

while contadormenu == 0:
	print('--------------------------------------------------------')
	print('****************************************')
	print('*                 MENU                 ')
	print('* 1. Jugar							  ')
	print('* 2. Salir							  ')
	print('*                                      ')
	print('****************************************')
	opcion = int(input('Ingrese una opción: '))
	if opcion == 1:
		print()
		contadorjuego = 0
		while contadorjuego == 0:
			print('--------------------------------------------------------')
			print('****************************************')
			print('*              Estadisticas            	')
			print(f'* Vida = {pjvida}/{pjvidamax} 			')
			print(f'* Ataque = {pjataque} 			')
			print('****************************************')
			opcionjuego = int(input('Ingrese una opción: '))

	if opcion == 2:
		contadormenu = 1
	else:
		print('Por favor elija una opcion correcta')





