
""" Proyecto RPG Prueba combate"""

from clases.jugador import Personaje

personaje = Personaje()

""" Menu """


contadormenu = 0

while contadormenu == 0:
	print('--------------------------------------------------------')
	print('****************************************')
	print('*                 MENU             		')
	print('* 1. Jugar							  	')
	print('* 2. Salir							  	')
	print('*                                      	')
	print('****************************************')
	opcion = int(input('Ingrese una opción: '))
	if opcion == 1:
		""" Creación de personaje """

		contadorclase = 0
		while contadorclase == 0:
			print('--------------------------------------------------------')
			print('****************************************')
			print('*  Seleccione un personaje             	')
			print('* 1. Tanque							  	')
			print('* 2. Guerrero							')
			print('* 3. Asesino							  	')
			print('*                                      	')
			print('****************************************')
			opcionClase = int(input('Ingrese una opción: '))

			if opcionClase == 1:
				personaje.vidamax = 200
				personaje.vida = personaje.vidamax
				personaje.defensa = 20
				personaje.ataque = 15
				contadorclase = 1

			elif opcionClase == 2:
				personaje.vidamax = 150
				personaje.vida = personaje.vidamax
				personaje.defensa = 15
				personaje.ataque = 20
				contadorclase = 1

			elif opcionClase == 3:
				personaje.vidamax = 100
				personaje.vida = personaje.vidamax
				personaje.defensa = 10
				personaje.ataque = 30
				contadorclase = 1

			else:
				print('Por favor elija una opcion correcta')

		contadornombre = 0
		while contadornombre == 0:
			print('--------------------------------------------------------')
			print('****************************************')
			print('*  Favor indicar su nombre            	')
			print('*                                      	')
			print('****************************************')

			opcionClase = input('Nombre: ')

			print('--------------------------------------------------------')
			print('****************************************')
			print(f'*  ¿Su nombre es {opcionClase}?         ')
			print('* 1. No                                  ')
			print('* 2. Si                                  ')
			print('****************************************')

			opcionconfnombre = int(input('Ingrese una opción: '))

			if opcionconfnombre == 2:
				contadornombre = 1

			else:
				print('Por favor elija una opcion correcta')

		""" Juego / Combate """
		contadorjuego = 0
		while contadorjuego == 0:
			print('--------------------------------------------------------')
			print('****************************************')
			print('*              Estadisticas     			')
			print(f'* Nombre = 								')
			print(f'* Vida = 								')
			print(f'* Ataque =  							')
			print('****************************************')
			opcionjuego = int(input('Ingrese una opción: '))

	elif opcion == 2:
		contadormenu = 1
		
	else:
		print('Por favor elija una opcion correcta')





