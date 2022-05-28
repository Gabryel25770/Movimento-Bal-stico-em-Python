from time import sleep #importação para o tempo
import math #importação para calculos matemáticos

def main(): #função principal
    print("*OBS: Efeitos da resistência do ar são desprezíveis* \n \n") #observação
    sleep(3)

    print("Exercício 1:\n") #primeiro exercício

    vel_inicial = float(input("1. Digite a velocidade inicial (em m/s): ")) #input da velocidade inicial

    angulo = float(input("2. Digite o ângulo inicial (entre 0 e 90 graus): ")) #input do ângulo inicial
    
    altura_solo_cm = float(input("3. Digite a altura em relação ao solo (em centímetros): ")) #input da altura em relação ao solo

    td = float(input("4. Digite um instante qualquer (em segundos): ")) #input do instante

    g = 9.8 #valor da gravidade

    #menu dos dados obtidos 
    print("\n\nDados obtidos a partir do que o usuário digitou:\n")
    print("Velocidade Inicial: %.1f m/s"%vel_inicial)
    print("Ângulo Inicial: %.3f graus"%angulo)
    print("Altura em relação ao solo: %.3f centímetros"%altura_solo_cm)
    print("Instante escolhido: %.3f segundos"%td)
    print("\n\n")

    altura_solo = altura_solo_cm/100 #converção de centímetros para metros

    print("a) Calcule as componentes nos eixos x e y da velocidade inicial da bola.\n") #primeira questão

    sen_ang = math.sin(math.radians(angulo)) #cálculo para obter o seno do ângulo
    cos_ang = math.cos(math.radians(angulo)) #cálculo para obter o cosseno do ângulo
    #converter o ângulo em graus p radianos pra funcionar
    v0x = vel_inicial*cos_ang #descobrindo o v0x
    v0y = vel_inicial*sen_ang #descobrindo o v0y

    print("Componentes da velocidade inicial:\nComponente x = %.3f m/s\nComponente y = %.3f m/s\n\n"%(v0x,v0y)) #resultado da primeira questão

    print("b) Calcule o tempo em que a bola permanece no ar.\n") #segunda questão

    t_sub = (vel_inicial*sen_ang)/g #cálculo para descobrir o tempo de subida
    t_alc = t_sub*2 #cálculo para descobrir o tempo de alcance

    print("Tempo no ar: %.3f segundos\n\n"%t_alc) #resultado da segunda questão

    print("c) Ache a posição da bola no instante td = 0.479 s.\n") #terceira questão

    x = v0x*td #cálculo para obter a posção de x
    y = altura_solo + v0y*td - (g*td**2)/2 #cálculo para obter a posição de y

    #resultado da terceira questão
    print("Posição no tempo escolhido:")
    print("Em X = %.3f"%x)
    print("Em Y = %.3f\n\n"%y)

    print("d) Calcule a velocidade e suas componentes nos eixos x e y no instante td= 0.479 s.\n") #quarta questão

    vx = x/td #cálculo para obter o vx
    vy = 2*(((y-altura_solo)/td)-v0y/2) #cálculo para obter o vy

    modulo = math.sqrt(vx**2+vy**2) #cálculo para obter o módulo da velocidade no instante escolhido

    #resultado da quarta questão
    print("Velocidade no tempo escolhido pelo usuário:")
    print("Componente x = %.3f m/s"%vx)
    print("Componente y = %.3f m/s"%vy)
    print("Módulo = %.3f m/s\n\n"%modulo)


    print("e) Ache a altura máxima alcançada pela bola.\n") #quinta questão

    altura_max = (((vel_inicial**2)*(sen_ang**2))/(2*g))+altura_solo #cálculo para obter a altura máxima
    
    print("Altura máxima: %.3f metros\n\n"%altura_max) #resultado da quinta questão

    print("f) Ache o alcance horizontal — ou seja, a distância entre o ponto inicial e o ponto onde a bola atinge o solo.\n") #sexta questão

    alcance = v0x*t_alc #cálculo para obter o alcance

    print("Alcance máximo = %.3f metros\n\n"%alcance) #resultado da sexta questão

    print("g) Calcule a velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y.\n") #sétima questão

    y_final = altura_solo + v0y*t_alc - (g*t_alc**2)/2 #cálculo para obter o y final

    velocidadefinal_y = 2*(((y_final-altura_solo)/t_alc)-v0y/2) #cálculo para obter o vy final

    mod_final = math.sqrt(v0x**2+velocidadefinal_y**2) #cálculo para obter o módulo da velocidade antes de alcançar o solo

    #resultado da sétima questão
    print("Velocidade prestes a atingir o chão:")
    print("Velocidade final x = %.3f"%v0x)
    print("Velocidade final y = %.3f"%velocidadefinal_y)
    print("Módulo = %.3f\n\n"%mod_final)
    
    print("h) Calcule a velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y.\n") #oitava questão

    #quando alcançar a altura máxima vx será igual a v0x
    #quando alcançar a altura máxima vy sempre será 0 pois atingiu o estado de repouso
    #já que vy é igual a 0, o módulo da velocidadec ao atingir a altura máxima será igual a vx, evitando assim cálculos desnecessários 

    #resultado da oitava questão
    print("Velocidade na altura máxima")
    print("Componente x = %.3f m/s\nComponente y = 0"%v0x)
    print("Módulo da Velocidade: %.3f m/s\n\n"%v0x)

    input("Aperte enter para continuar...\n\n") #input para ir para o próximo exercício

    print("Exercício 2:\n") #segundo exercício

    vel_inicial_x = float(input("1. Digite a velocidade inicial (em m/s): ")) #input da velocidade inicial

    altura_mesa_cm = float(input("3. Digite a altura da mesa (em centímetros): ")) #input da altura da mesa

    g = 9.8 #valor da gravidade

    v0y = 0

    #menu dos dados obtidos 
    print("\n\nDados obtidos a partir do que o usuário digitou:\n")
    print("Velocidade Inicial: %.1f m/s"%vel_inicial_x)
    print("Altura em relação ao solo: %.3f centímetros"%altura_mesa_cm)
    print("\n\n")

    altura_mesa = altura_mesa_cm/100 #converção de centímetros para metros

    print("a) a distância horizontal entre a extremidade da mesa e o ponto onde ele atingiu o solo.\n") #primeira questão

    dist_hori = vel_inicial_x* math.sqrt((2*altura_mesa)/g)  #cálculo para obter a distância horizontal

    print("Distância horizontal = %.3f metros\n\n"%dist_hori) #resultado da primeira questão

    print("b) os componentes horizontal e vertical da velocidade do livro e o módulo imediatamente antes de o livro atingir o solo.\n") #segunda questão

    v_final_y = math.sqrt((v0x**2)+ 2*(g*altura_mesa)) #cálculo para obter o vy final

    mod_finalb = math.sqrt(v0x**2+v_final_y**2) #cálculo para obter o módulo da velocidade antes de alcançar o solo

    #resultado da sétima questão
    print("Velocidade prestes a atingir o chão:")
    print("Velocidade final x = %.3f"%vel_inicial_x)
    print("Velocidade final y = -%.3f"%v_final_y)
    print("Módulo = %.3f\n\n"%mod_finalb)

    input("Aperte enter para continuar...\n\n") #input para ir para o próximo exercício

    print("Exercício 3:\n") #terceiro exercício

    vel_inicial_km = float(input("1. Digite a velocidade inicial (em km/h): ")) #input da velocidade inicial

    angulo = float(input("2. Digite o ângulo inicial (entre 0 e 90 graus): ")) #input do ângulo inicial
    
    altura_solo_cm = float(input("3. Digite a altura em relação ao solo (em centímetros): ")) #input da altura em relação ao solo

    td = float(input("4. Digite um instante qualquer (em segundos): ")) #input do instante

    g = 9.8 #valor da gravidade

    #menu dos dados obtidos 
    print("\n\nDados obtidos a partir do que o usuário digitou:\n")
    print("Velocidade Inicial: %.1f m/s"%vel_inicial)
    print("Ângulo Inicial: %.3f graus"%angulo)
    print("Altura em relação ao solo: %.3f centímetros"%altura_solo_cm)
    print("Instante escolhido: %.3f segundos"%td)
    print("\n\n")

    altura_solo = altura_solo_cm/100 #converção de centímetros para metros
    vel_inicial = vel_inicial_km/3.6 #converção de km/h para m/s 

    print("a) Calcule as componentes nos eixos x e y da velocidade inicial da bola.\n") #primeira questão

    sen_ang = math.sin(math.radians(angulo)) #cálculo para obter o seno do ângulo
    cos_ang = math.cos(math.radians(angulo)) #cálculo para obter o cosseno do ângulo
    #converter o ângulo em graus p radianos pra funcionar
    v0x = vel_inicial*cos_ang #descobrindo o v0x
    v0y = vel_inicial*sen_ang #descobrindo o v0y

    print("Componentes da velocidade inicial:\nComponente x = %.3f m/s\nComponente y = %.3f m/s\n\n"%(v0x,v0y)) #resultado da primeira questão

    print("b) Calcule o tempo em que a bola permanece no ar.\n") #segunda questão

    t_sub = (vel_inicial*sen_ang)/g #cálculo para descobrir o tempo de subida
    t_alc = t_sub*2 #cálculo para descobrir o tempo de alcance

    print("Tempo no ar: %.3f segundos\n\n"%t_alc) #resultado da segunda questão

    print("c) Ache a posição da bola no instante td = 0.479 s.\n") #terceira questão

    x = v0x*td #cálculo para obter a posção de x
    y = altura_solo + v0y*td - (g*td**2)/2 #cálculo para obter a posição de y

    #resultado da terceira questão
    print("Posição no tempo escolhido:")
    print("Em X = %.3f"%x)
    print("Em Y = %.3f\n\n"%y)

    print("d) Calcule a velocidade e suas componentes nos eixos x e y no instante td= 0.479 s.\n") #quarta questão

    vx = x/td #cálculo para obter o vx
    vy = 2*(((y-altura_solo)/td)-v0y/2) #cálculo para obter o vy

    modulo = math.sqrt(vx**2+vy**2) #cálculo para obter o módulo da velocidade no instante escolhido

    #resultado da quarta questão
    print("Velocidade no tempo escolhido pelo usuário:")
    print("Componente x = %.3f m/s"%vx)
    print("Componente y = %.3f m/s"%vy)
    print("Módulo = %.3f m/s\n\n"%modulo)


    print("e) Ache a altura máxima alcançada pela bola.\n") #quinta questão

    altura_max = (((vel_inicial**2)*(sen_ang**2))/(2*g))+altura_solo #cálculo para obter a altura máxima
    
    print("Altura máxima: %.3f metros\n\n"%altura_max) #resultado da quinta questão

    print("f) Ache o alcance horizontal — ou seja, a distância entre o ponto inicial e o ponto onde a bola atinge o solo.\n") #sexta questão

    alcance = v0x*t_alc #cálculo para obter o alcance

    print("Alcance máximo = %.3f metros\n\n"%alcance) #resultado da sexta questão

    print("g) Calcule a velocidade da bola imediatamente antes de alcançar o solo e suas componentes nos eixos x e y.\n") #sétima questão

    y_final = altura_solo + v0y*t_alc - (g*t_alc**2)/2 #cálculo para obter o y final

    velocidadefinal_y = 2*(((y_final-altura_solo)/t_alc)-v0y/2) #cálculo para obter o vy final

    mod_final = math.sqrt(v0x**2+velocidadefinal_y**2) #cálculo para obter o módulo da velocidade antes de alcançar o solo

    #resultado da sétima questão
    print("Velocidade prestes a atingir o chão:")
    print("Velocidade final x = %.3f"%v0x)
    print("Velocidade final y = %.3f"%velocidadefinal_y)
    print("Módulo = %.3f\n\n"%mod_final)
    
    print("h) Calcule a velocidade no instante em que a bola atinge a altura máxima e suas componentes nos eixos x e y.\n") #oitava questão

    #quando alcançar a altura máxima vx será igual a v0x
    #quando alcançar a altura máxima vy sempre será 0 pois atingiu o estado de repouso
    #já que vy é igual a 0, o módulo da velocidadec ao atingir a altura máxima será igual a vx, evitando assim cálculos desnecessários 

    #resultado da oitava questão
    print("Velocidade na altura máxima")
    print("Componente x = %.3f m/s\nComponente y = 0"%v0x)
    print("Módulo da Velocidade: %.3f m/s\n\n"%v0x)

    input("Aperte enter para finalizar...") #input para finalizar a atividade e evitar que o código entre em looping descontroladamente

#MENU
while(True): #condição para forçar um looping
    print("\nMovimento Balístico em Python ") #nome da atividade
    input("Pressione o Enter\n") #comando de iniciação
    main() #chamando a função principal que contém todo o corpo do código