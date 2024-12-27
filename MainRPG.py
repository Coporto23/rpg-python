
""" Proyecto RPG Prueba combate"""

from clases.jugador import Personaje
from clases.enemigo import Enemigo

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
			print('*                                      	')
			print('*  Favor indicar su nombre            	')
			print('*                                      	')
			print('****************************************')

			opcionNombre = input('Nombre: ')

			print('--------------------------------------------------------')
			print('****************************************')
			print(f'*  ¿Su nombre es {opcionNombre}?         ')
			print('* 1. No                                  ')
			print('* 2. Si                                  ')
			print('****************************************')

			opcionconfnombre = int(input('Ingrese una opción: '))

			if opcionconfnombre == 2:

				personaje.nombre = opcionNombre 
				print('')
				contadornombre = 1

			else:
				print('Por favor elija una opcion correcta')

		""" Juego / Combate """
		contadorjuego = 0
		while contadorjuego != 11:

			contadorjuego = contadorjuego + 1

			print('--------------------------------------------------------')
			print('****************************************')
			print('*                                      	')
			print(f'*  Estás en el nivel {contadorjuego}    ')
			print('*                                      	')
			print('****************************************')

			print('--------------------------------------------------------')
			print('*********************** SLIME **************************')
			print('*               ⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀               ')
			print('*           ⠀⠀⠀⠀⣠⣾⠿⠛⠉⠉⠉⠉⠉⠉⠛⠿⣷⣄⠀⠀⠀⠀⠀              ')
			print('*          ⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀             ')
			print('*         ⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀            ')
			print('*         ⠀⠀⢀⣿⡇⠀⠀⢠⡶⠶⢿⣿⣿⡿⠶⢦⡀⠀⠀⢸⣿⡇⠀            ')
			print('*         ⠀⠀⢸⣿⠃⠀⢀⣾⡇⠀⢸⣿⣿⠁⠀⢸⣷⡀⠀⠘⣿⡇⠀            ')
			print('*         ⠀⠀⢸⣿⠀⠀⢸⣿⣧⣤⣼⣿⣿⣧⣤⣼⣿⡇⠀⠀⣿⡇⠀            ')
			print('*         ⠀⠀⠘⣿⡀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢀⣿⡇⠀            ')
			print('*          ⠀⠀⠹⣧⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀⠀⢀⣾⡟⠀⠀            ')
			print('*           ⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠀            ')
			print('*             ⠀⠀⠀⠙⠿⣶⣤⣤⣤⣤⣤⣤⣤⣶⡿⠿⠁⠀⠀⠀⠀⠀           ')
			print('*******************************************************')

			enemigo = Enemigo()

			enemigo.nombre = 'Slime'
			enemigo.vida = 50
			enemigo.vidamax = 50
			enemigo.ataque = 10
			enemigo.defensa = 0

			contadorcombate = 0
			while contadorcombate == 0:
				if enemigo.vida == 0:

					print('****************************************')
					print('* HAS GANADO!!                          ')
					print('****************************************')
					contadorcombate = 1
				else:
					print('--------------------------------------------------------')
					print('****************************************')
					print('*                                      	')
					print(f'*  {personaje.nombre} {personaje.vida}/{personaje.vidamax} HP   ')
					print(f'*  {enemigo.nombre} {enemigo.vida}/{enemigo.vidamax} HP    		')
					print('*                                      	')
					print('****************************************')
					contadorturno = 0

					while contadorturno == 0:
						

						print('****************************************')
						print('*  ¿Que quieres hacer?			       ')
						print('* 1. Ataque                             ')
						print('* 2. Defensa                            ')
						print('****************************************')
						opcionturno = int(input('Elija una opción: '))
						if opcionturno == 1:
							enemigo.vida = enemigo.vida - personaje.ataque
							if enemigo.vida <= 0:
								enemigo.vida = 0
							print('****************************************')
							print(f'* Has hecho {personaje.ataque} de daño ')
							print('****************************************')
							contadorturno = 1
						else:
							contadorturno = 1



	elif opcion == 2:
		contadormenu = 1

	else:
		print('Por favor elija una opcion correcta')





