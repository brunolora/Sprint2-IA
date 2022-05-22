#Imports utilizados
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import cv2
import mediapipe as mp
import time
import webbrowser

#https://google.github.io/mediapipe/solutions/face_detection
#fonte utilizada para utilizar face com webcam

#função webcam
camera = cv2.VideoCapture(0)

#mediapipe já tem tudo pronto para ser utilizado
formula_rosto = mp.solutions.face_detection

deteccao_rosto = formula_rosto.FaceDetection()

#Desenho que rodea a face
retangulo = mp.solutions.drawing_utils

#While para a detectar e liberar o programa
while True:
    detector, frame = camera.read()

    #Se não detectar não continua o programa
    if not detector:
        break

    rostos = deteccao_rosto.process(frame)

    if rostos.detections:
        for rosto in rostos.detections:
            retangulo.draw_detection(frame, rosto)
        if rostos.detections:
            time.sleep(2)
            break

    #Mostrando a capturação
    cv2.imshow("Detector de face", frame)

    #Dica de um amigo, aperta ESC e sai
    if cv2.waitKey(5) == 27:
        break

camera.release()
cv2.destroyAllWindows()

print("Começando a IA DareDevil, bem vindo!")

recon = sr.Recognizer()
resposta = ""

#função para não ficar repetindo o comando cada vez que tiver que falar
def escutar_daredevil():
    audio = recon.listen(source)
    recon.adjust_for_ambient_noise(source)
    #.lower() para padronizar os textos para facil reconhecimento
    resposta = recon.recognize_google(audio, language='pt').lower()
    return(resposta)

with sr.Microphone() as source:
    #Setando a IA
    daredevil = pyttsx3.init()
    daredevil.setProperty("voice", b'brasil')
    daredevil.setProperty('rate', 140)
    daredevil.setProperty('volume', 1)

    resposta = escutar_daredevil()
    print("Comando reconhecido:", resposta)

    #Programa só executará se for fala ""Ok, Vermelho"
    while True:
        if resposta == "ok vermelho":
            daredevil.say("No que posso ajudar?")
            print("No que posso ajudar?")
            daredevil.runAndWait()
            #Todos os comandos
            while True:
                resposta = escutar_daredevil()
                print("Comando reconhecido:", resposta)

                #Anotando futuros eventos
                if resposta == "cadastrar evento na agenda":
                    daredevil.say("Ok, qual evento devo cadastrar? ")
                    print("Ok, qual evento devo cadastrar")
                    daredevil.runAndWait()

                    txt2 = escutar_daredevil()

                    arquivoTxt = open("agenda.txt", "w")
                    arquivoTxt.write(txt2)
                    arquivoTxt.close()
                    daredevil.say("Evento cadastrado!")
                    print("Evento cadastrado!")
                    continue

                #Lendo esses eventos
                if resposta == "ler agenda":
                    with open("agenda.txt") as file:
                        for linha in file:
                            linha = linha.strip()
                            daredevil.runAndWait()
                            daredevil.say(linha)
                            print(linha)
                        continue

                #Calculadora
                if resposta == "calculadora":
                    try:
                        daredevil.say("Quais valores deseja calcular?")
                        print("Quais valores deseja calcular?")
                        daredevil.runAndWait()

                        contatxt = escutar_daredevil()

                        print("Texto reconhecido: ", contatxt)
                        if contatxt == "fechar":
                            break
                        conta = contatxt.split()
                        if conta[1] == "+":
                            resultado = str(int(conta[0]) + int(conta[2]))
                            daredevil.say("Resultado é: ", resultado)
                            daredevil.runAndWait()
                        elif conta[1] == "-":
                            resultado = str(int(conta[0]) - int(conta[2]))
                            daredevil.say("Resultado é: ", resultado)
                            daredevil.runAndWait()
                        elif conta[1] == "/":
                            resultado = str(int(conta[0]) / int(conta[2]))
                            daredevil.say("Resultado é: ", resultado)
                            daredevil.runAndWait()
                        elif conta[1] == "x":
                            resultado = str(int(conta[0]) * int(conta[2]))
                            daredevil.say("Resultado é: ", resultado)
                            daredevil.runAndWait()
                    #Except para pegar os erros
                    except ValueError:
                        print("O valor precisa ser númerico ")
                    except ZeroDivisionError:
                        print("Divisão por zero")
                        break
                #Fala o horário do momento atual
                if resposta == "horário":
                    horario = (str(datetime.today().hour) + ":" + str(datetime.today().minute))
                    daredevil.say(horario)
                    print(horario)
                    daredevil.runAndWait()
                    break

                #Fala o dia atual
                if resposta == "que dia é hoje":
                    meses = {1: "Janeiro", 2: "fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho",
                             8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

                    if datetime.today().month in meses.keys():
                        mes = meses.get(datetime.today().month)

                    dia = datetime.today().day
                    ano = datetime.today().year

                    sentenca = "Hoje é dia " + str(dia) + " de " + str(mes) + " de " + str(ano)

                    daredevil.say(sentenca)
                    print(sentenca)
                    daredevil.runAndWait()
                    break

                #Abre site de lançamentos de livros novos 2022
                if resposta == "lançamentos":
                    webbrowser.open("https://capricho.abril.com.br/entretenimento/lancamentos-de-livros-de-fantasia-para-voce-conferir-em-2022/",
                                    autoraise=True)
                    daredevil.say("Abrindo site para lançamentos de novos livros")
                    print("Abrindo site para lançamentos de novos livros")
                    daredevil.runAndWait()
                    break

                #Abre site para compra de livros
                #
                if resposta == "comprar livros":
                    webbrowser.open("https://www.amazon.com.br/Livros/b/?ie=UTF8&node=6740748011&ref_=nav_cs_books", autoraise=True)
                    daredevil.say("Abrindo site para compra de livros")
                    print("Abrindo site para compra de livros")
                    daredevil.runAndWait()
                    break