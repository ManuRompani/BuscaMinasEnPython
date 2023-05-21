import random


def verificacion_mina(fila,columna):
	if(matriz[fila][columna]==1):
		return True
	else: return False

def mostrar_matriz(matriz):
	for i in range(3):
		for j in range(3):
			print('\t',matriz[i][j], end='   ')
		print("\n")
	return 0

def cambiador_de_X(matriz_X,mf1,mc1,mf2,mc2,ufil,ucol,matriz_oficial):
	contador_contacto=0
	if(mf1==ufil and mc1==ucol):
		matriz_muestra_avance[ufil][ucol]=-1
	elif(mf2==ufil and mc2==ucol):
		matriz_muestra_avance[ufil][ucol]=-1
	else:
		
		if(ufil==0 and ucol==0):
			if(matriz_oficial[0][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][0]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto
		
		if(ufil==0 and ucol==2):
			if(matriz_oficial[0][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][2]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto
		
		if(ufil==2 and ucol==2):
			if(matriz_oficial[1][2]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[2][1]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==2 and ucol==0):
			if(matriz_oficial[1][0]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[2][1]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==0 and ucol==1):
			if(matriz_oficial[0][0]==1):
				contador_contacto+=1
			if(matriz_oficial[1][0]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][2]==1):
				contador_contacto+=1	
			if(matriz_oficial[0][2]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==2 and ucol==1):
			if(matriz_oficial[2][0]==1):
				contador_contacto+=1
			if(matriz_oficial[1][0]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][2]==1):
				contador_contacto+=1	
			if(matriz_oficial[2][2]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==1 and ucol==0):
			if(matriz_oficial[0][0]==1):
				contador_contacto+=1
			if(matriz_oficial[0][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[2][1]==1):
				contador_contacto+=1	
			if(matriz_oficial[2][0]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==1 and ucol==2):
			if(matriz_oficial[0][2]==1):
				contador_contacto+=1
			if(matriz_oficial[0][1]==1):
				contador_contacto+=1
			if(matriz_oficial[1][1]==1):
				contador_contacto+=1
			if(matriz_oficial[2][1]==1):
				contador_contacto+=1	
			if(matriz_oficial[2][2]==1):
				contador_contacto+=1
			matriz_muestra_avance[ufil][ucol]=contador_contacto

		if(ufil==1 and ucol==1):
			while(contador_contacto<2):
				if(matriz_oficial[0][0]==1):
					contador_contacto+=1
				if(matriz_oficial[0][1]==1):
					contador_contacto+=1
				if(matriz_oficial[0][2]==1):
					contador_contacto+=1
				if(matriz_oficial[1][0]==1):
					contador_contacto+=1	
				if(matriz_oficial[1][2]==1):
					contador_contacto+=1
				if(matriz_oficial[2][0]==1):
					contador_contacto+=1
				if(matriz_oficial[2][1]==1):
					contador_contacto+=1
				if(matriz_oficial[2][2]==1):
					contador_contacto+=1
				matriz_muestra_avance[ufil][ucol]=contador_contacto
	
	return 0


#INICIO

print("--------MENU--------")
print('\n1_Jugar\n0_Salir\n')
iniciacion=int(input(">>"))


while(iniciacion!=0):
	
	matriz=[[0,0,0],[0,0,0],[0,0,0]]
	matriz_muestra_coordenadas=[["0:0","0:1","0:2"],["1:0","1:1","1:2"],["2:0","2:1","2:2"]]
	matriz_muestra_avance=[['x','x','x'],['x','x','x'],['x','x','x']]
	contador_ganaste=0
	matriz=[[0,0,0],[0,0,0],[0,0,0]]
	matriz_muestra_coordenadas=[["0:0","0:1","0:2"],["1:0","1:1","1:2"],["2:0","2:1","2:2"]]
	matriz_muestra_avance=[['x','x','x'],['x','x','x'],['x','x','x']]
	contador_ganaste=0

#GENERADOR DE MINAS

	mina_uno_fila=random.randint(0, 2)
	mina_uno_columna=random.randint(0, 2)
	mina_dos_fila=random.randint(0, 2)
	while(mina_dos_fila==mina_uno_fila):
		mina_dos_fila=random.randint(0, 2)
	mina_dos_columna=random.randint(0, 2)
	while(mina_dos_columna==mina_uno_columna):
		mina_dos_columna=random.randint(0, 2)

	matriz[mina_uno_fila][mina_uno_columna]=1
	matriz[mina_dos_fila][mina_dos_columna]=1

#FORMA DE INDICAR COORDENADAS

	print("\t\t FILA:COLUMNA\n")
	mostrar_matriz(matriz_muestra_coordenadas)




#INICIO PETICION COORDENADAS

	ubicacion_Fila=int(input('\nIngrese sus coordenadas "FILA" y "COLUMNA"\n\nFILA(0-2): '))
	while(ubicacion_Fila>2 or ubicacion_Fila<0):
		print("Dato incorrecto")
		ubicacion_Fila=int(input('Ingrese sus coordenadas "FILA" y "COLUMNA"\n\nFILA(0-2): '))
	ubicacion_Columna=int(input("COLUMNA(0-2): "))
	while(ubicacion_Columna>2 or ubicacion_Columna<0):
			print("Dato incorrecto")
			ubicacion_Columna=int(input("COLUMNA(0-2): "))
	print("")
	cambiador_de_X(matriz_muestra_avance,mina_uno_fila,mina_uno_columna,mina_dos_fila,mina_dos_columna,ubicacion_Fila,ubicacion_Columna,matriz)
	print("")
	mostrar_matriz(matriz_muestra_avance)



#BUCLE MIENTRAS "NO SE PISE UNA MINA"

	while(verificacion_mina(ubicacion_Fila,ubicacion_Columna)!=True and contador_ganaste!=6):
		contador_ganaste+=1
		ubicacion_Fila=int(input('\nIngrese sus coordenadas "FILA" y "COLUMNA"\n\nFILA(0-2): '))
		while(ubicacion_Fila>2 or ubicacion_Fila<0):
			print("Dato incorrecto")
			ubicacion_Fila=int(input('Ingrese sus coordenadas "FILA" y "COLUMNA"\n\nFILA(0-2): '))
		ubicacion_Columna=int(input("COLUMNA(0-2): "))
		while(ubicacion_Columna>2 or ubicacion_Columna<0):
			print("Dato incorrecto")
			ubicacion_Columna=int(input("COLUMNA(0-2): "))
		print("")
		cambiador_de_X(matriz_muestra_avance,mina_uno_fila,mina_uno_columna,mina_dos_fila,mina_dos_columna,ubicacion_Fila,ubicacion_Columna,matriz)
		print("")
		mostrar_matriz(matriz_muestra_avance)

	if(contador_ganaste==6):
		print("GANASTE CRACK!!")
	else:
		print("PERDISTE :(")
	print("--------MENU--------")
	print('\n1_Volver a jugar\n0_Salir\n')
	iniciacion=int(input(">>"))







