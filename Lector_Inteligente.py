#LIBRERIAS
import os
import cv2
import pytesseract
from gtts import gTTS


#Variables para Captura de video
cuadro=100
anchocam, altocam=640,480

#Captura de video
cap=cv2.VideoCapture(0)
cap.set(3,anchocam)
cap.set(4,altocam)

#Funcion para extraer el texto
def text(image):
    #Funcion para reproducir la voz
    def voz(archi_text, lenguaje, nom_archi):
        with open(archi_text,"r") as lec:
            lectura=lec.read()
        lect=gTTS(text=lectura,lang=lenguaje,slow=False)
        nombre=nom_archi
        lect.save(nombre)
    
    pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    gris=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    texto=pytesseract.image_to_string(gris)
    print(texto)
    dire=open('Info.txt','w')
    dire.write(texto)
    dire.close()
    voz("Info.txt","es","Voz.mp3")
    os.system("start  Voz.mp3")



#Parte Principal del programa
while True:
    ret,fr = cap.read() #Se lee la captura del video 
    if ret == False:break #Si no lee correctamente se cierra
    cv2.putText(fr, 'Coloque aqui el texto a leer',(158,80),cv2.FONT_HERSHEY_SIMPLEX,0.71,(255,255,0),2)
    cv2.putText(fr, 'Coloque aqui el texto a leer',(160,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
    cv2.rectangle(fr,(cuadro,cuadro),(anchocam-cuadro,altocam-cuadro),(0,0,0),2) #Generamos rectangulo o marco de donde se sacaran los pixeles
    x1,y1=cuadro,cuadro
    ancho,alto= (anchocam-cuadro)-x1,(altocam-cuadro)-y1 #se extrae el ancho y el alto
    x2,y2=x1+ancho,y1+alto
    docu=fr[y1:y2,x1:x2] #Se Guardan los pixeles
    cv2.imwrite("Imatext.jpg",docu)
    
    cv2.imshow("Lector Inteligente",fr)
    t=cv2.waitKey(1)
    if t== 27:
        break

text(docu)
cap.release()
cv2.destroyAllWindows()
    