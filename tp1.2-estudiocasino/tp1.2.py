import numpy as np
import matplotlib.pyplot as plt

def generarNumeroAleatorios():
   listaAleatorios = []
   for i in range(1000):
       listaAleatorios.append(np.random.randint(0,37))
   return listaAleatorios

def calcularColor(numero):
  #ROJO DEVUELVE TRUE
  if numero in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
      return True
  return False

def calcularParidad(numero):
  if numero % 2 == 0:
      return True
  return False

def calcularColumna(numero, jugada):
    if(jugada == 1):
        if(numero<12):
            return True
        return False

    if(jugada == 2):
        if(13<numero<24):
            return True
        return False

    if(jugada == 3):
        if(24<numero<36):
            return True
        return False

def martinGala(apuestaInicial, dinero, numeros):
    #La apuesta es para el color rojo
    dineroJugador = dinero
    apuesta = apuestaInicial
    dineroTiempo = []
    dineroTiempo.append(dineroJugador)
    frecuenciaRelativa = []
    contFrecuencias = 0
    indice = 0
    for i in range(1000):
        numero = numeros[i]
        if(dineroJugador >= apuesta):
            if(calcularColor(numero)):
                dineroJugador = dineroJugador + apuesta
                apuesta = apuestaInicial
                contFrecuencias = contFrecuencias + 1
            else:
                dineroJugador = dineroJugador - apuesta
                apuesta = (apuesta * 2)
            dineroTiempo.append(dineroJugador)
            indice += 1
            frecuenciaRelativa.append(contFrecuencias/indice)

    #graficarFrecuencias(frecuenciaRelativa,indice)
    return dineroTiempo, frecuenciaRelativa, indice

def graficoDinero(dineroTiempo, titulo,dineroInicial):
   for i in range(5):
       plt.title(titulo)
       plt.axhline(dineroInicial,color='k', ls="solid")
       plt.plot(dineroTiempo[i], linewidth=0.8)
       plt.xlabel("(Número de tiradas)")
       plt.ylabel("Capital en el tiempo")
       #Me ajustan los x e y
       ax = plt.gca()
       ax.relim()
       ax.autoscale_view()
       #plt.axhline(dineroInicial,color='w', ls="solid",visible=False) #Linea invisible para agregar legend
       #dineroIni = 'Capital inicial: ' + str(dineroInicial)
       #dineroFin = 'Capital Final: ' + str(round(dineroFinal,2))
       #plt.legend((dineroIni,dineroFin), loc="lower left")
       plt.ioff()
   plt.show()

def graficoDineroPrimeraTirada(dineroTiempo, titulo,dineroInicial):
   plt.title(titulo)
   plt.axhline(dineroInicial,color='k', ls="solid")
   plt.plot(dineroTiempo, linewidth=0.8)
   plt.xlabel("(Número de tiradas)")
   plt.ylabel("Capital en el tiempo")
   ax = plt.gca()
   ax.relim()
   ax.autoscale_view()
   plt.axhline(dineroInicial,color='w', ls="solid",visible=False) #Linea invisible para agregar legend
   dineroIni = 'Capital inicial: ' + str(dineroInicial)
   dineroFin = 'Capital Final: ' + str(round(dineroTiempo[-1],2))
   plt.legend((dineroIni,dineroFin), loc="lower left")
   plt.show()

def graficarFrecuencias(frecuenciaPromedio,indice):
    plt.bar(range(0,indice),frecuenciaPromedio, width=0.6)
    plt.ylabel('Frec. Rel. de la apuesta favorable')
    plt.ylim(0, 1)
    plt.xlabel('Nro iteración')
    plt.show()

def dalembert(apuesta, dinero, numeros):
    #La apuesta es para color rojo
    dineroJugador = dinero
    apuesta = apuesta
    indice = 0
    contFrecuencias = 0
    frecuenciaRelativa = []
    dineroTiempo = []
    dineroTiempo.append(dinero)
    for i in range(1000):
            numero = numeros[i]
            if(dineroJugador >= apuesta):
                if calcularColor(numero):
                    dineroJugador = dineroJugador + apuesta
                    contFrecuencias += 1
                    if apuesta>1:
                        apuesta = apuesta - 1
                else:
                    dineroJugador = dineroJugador - apuesta
                    apuesta = apuesta + 1
                dineroTiempo.append(dineroJugador)
                indice += 1
                frecuenciaRelativa.append(contFrecuencias/indice)

    return dineroTiempo, frecuenciaRelativa, indice

def apostarDocena(apuesta, dinero, numeros):
  #La apuesta es para la primer docena
  apuesta = apuesta
  dineroJugador = dinero
  dineroTiempo = []
  frecuenciaRelativa = []
  dineroTiempo.append(dineroJugador)
  indice = 0
  contFrecuencias = 0
  for i in range(1000):
      if(dineroJugador >= apuesta):
          numero = numeros[i]
          if(calcularColumna(numero, 1) or calcularColumna(numero,2)):
              contFrecuencias += 1
              dineroJugador = dineroJugador + apuesta
              if apuesta > 1:
                apuesta = apuesta - 1
          else:
              dineroJugador = dineroJugador - (apuesta*2)
              apuesta = apuesta + 1
          dineroTiempo.append(dineroJugador)
          indice += 1
          frecuenciaRelativa.append(contFrecuencias/indice)

  return dineroTiempo, frecuenciaRelativa, indice

def apostarAUnNumero(apuesta, dinero, numeros):
  numeroApostado = 5
  apuesta = apuesta
  dineroJugador = dinero
  dineroTiempo = []
  indice = 0
  contFrecuencias = 0
  frecuenciaRelativa = []
  dineroTiempo.append(dineroJugador)
  for i in range(1000):
      if(dineroJugador >= apuesta):
          numero = numeros[i]
          if(numero == numeroApostado):
              dineroJugador = dineroJugador + (apuesta * 36)
              contFrecuencias += 1
          else:
              dineroJugador = dineroJugador - apuesta #el dinero final se corta mucho antes porque la apuesta es mas grande

          dineroTiempo.append(dineroJugador)
          indice += 1
          frecuenciaRelativa.append(contFrecuencias/indice)

  return dineroTiempo, frecuenciaRelativa, indice


apuestaInicial = 25
capitalJugadorAcotado = 1000
capitalJugadorIdeal = 100_000

dineroMartinGalaAcotado = []
dineroDalembertAcotado = []
dineroDocenaAcotado = []
dineroNumeroAcotado = []
dineroDocenaIdeal = []
dineroMartinGalaIdeal = []
dineroDalembertIdeal = []
dineroNumeroIdeal = []

numeros = generarNumeroAleatorios()

#Graficas para 1 tirada Capital acotado
resultadoMartingala = martinGala(apuestaInicial,capitalJugadorAcotado,numeros)
resultadoDalembert = dalembert(apuestaInicial,capitalJugadorAcotado,numeros)
resultadoDocena = apostarDocena(apuestaInicial,capitalJugadorAcotado,numeros)
resultadosNumero = apostarAUnNumero(apuestaInicial,capitalJugadorAcotado,numeros)
graficoDineroPrimeraTirada(resultadoMartingala[0],'Apuesta Martingala',capitalJugadorAcotado)
graficarFrecuencias(resultadoMartingala[1],resultadoMartingala[2])
graficoDineroPrimeraTirada(resultadoDalembert[0],'Apuesta Dalembert',capitalJugadorAcotado)
graficarFrecuencias(resultadoDalembert[1], resultadoDalembert[2])
graficoDineroPrimeraTirada(resultadoDocena[0],'Apuesta a docena',capitalJugadorAcotado)
graficarFrecuencias(resultadoDocena[1], resultadoDocena[2])
graficoDineroPrimeraTirada(resultadosNumero[0],'Apuesta a Numero',capitalJugadorAcotado)
graficarFrecuencias(resultadosNumero[1],resultadosNumero[2])
for i in range(5):
    numeros = generarNumeroAleatorios()
    dineroMartinGalaIdeal.append(martinGala(apuestaInicial,capitalJugadorIdeal,numeros)[0])
    dineroDalembertIdeal.append(dalembert(apuestaInicial,capitalJugadorIdeal,numeros)[0])
    dineroDocenaIdeal.append(apostarDocena(apuestaInicial,capitalJugadorIdeal,numeros)[0])
    dineroNumeroIdeal.append(apostarAUnNumero(apuestaInicial,capitalJugadorIdeal,numeros)[0])
#Graficas en simultaneo de 5 corridas
graficoDinero(dineroMartinGalaIdeal,'Apuesta Martingala',capitalJugadorIdeal)
graficoDinero(dineroDalembertIdeal,'Apuesta Dalembert',capitalJugadorIdeal)
graficoDinero(dineroDocenaIdeal,'Apuesta a docena',capitalJugadorIdeal)
graficoDinero(dineroNumeroIdeal,'Apuesta a Numero',capitalJugadorIdeal)



