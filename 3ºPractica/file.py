import cv2  
import numpy as np
import matplotlib.pyplot as plt

# identifica las monedas de una imagen, (param1, param2, param3)
# param1: dirección de la imagen
# param2: moneda a identificar (0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2) es una string
# param3: si es True, identifica todas las monedas, da igual el valor de param2

def contar_dinero(all, coin, img, x, y, r):
    if(((coin=="0.01") | (all)) & (r<50.0)): # 1cent
        cv2.circle(img,(int(x), int(y)), int(r), (255,0,0), 2)
        print(" r: ", r, " 0.01")
        return 0.01
    
    elif(((coin=="0.02") | (all)) & (r>50.0) & (r<53.0)): # 2cent
        print(" r: ", r, " 0.02")
        return 0.02
    
    elif(((coin=="0.10") | (all)) & (r>53.0) & (r<56.0)): # 10cent
        print(" r: ", r, " 0.1")
        return 0.10
    
    elif(((coin=="0.05") | (all)) & (r>56.0) & (r<59.0)): # 5cent
        print(" r: ", r, " 0.05")
        return 0.05
    
    elif(((coin=="0.20") | (all)) & (r>59.0) & (r<62.0)): # 20cent
        print(" r: ", r, " 0.2")
        return 0.20
    
    elif(((coin=="1") | (all)) & (r>62.0) & (r<66.0)): # 1euro
        print(" r: ", r, " 1")
        return 1.0
    
    elif(((coin=="0.50") | (all)) & (r>66.0) & (r<68.0)): # 50cent
        print(" r: ", r, " 0.5")
        return 0.50
    
    elif(((coin=="2") | (all)) & (r>68.0)): # 2euros
        print(" r: ", r, " 2")
        return 2.0
    
    else: 
        print(" r: ", r, "0")
        return 0.0
# identifica las monedas de una imagen, (param1, param2, param3)
# param1: dirección de la imagen
# param2: moneda a identificar (0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2) es una string
# param3: si es True, identifica todas las monedas, da igual el valor de param2
def identificar_moneda(dir_img, moneda, todas):
    cont = 0
    dinero = 0.0
    img = cv2.imread(dir_img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # show_picture(img_rgb, "Imagen Original", False)
    
    #Conversión a gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show_picture(gris, "Imagen en Gris", True)
    
    #Suaviza altas frecuencias
    pimg = cv2.GaussianBlur(gris, (5, 5), 1)
    # show_picture(pimg, "Imagen Suavizada", True)
    
    umbral = cv2.threshold(pimg,248,255,cv2.THRESH_BINARY_INV)[1]
    #show_picture(umbral, "Imagen Umbralizada", True)
    
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    img_cont = np.zeros(img_rgb.shape)
    
    for c in contornos:
        #Área
        cont += 1
        #Mínimo círculo que lo contiene
        (cx,cy),radio = cv2.minEnclosingCircle(c)
        dinero += contar_dinero(todas, moneda, img, cx, cy, radio)  
                  

    print("Nº de moneda: ", cont)
    print("Costo total: ", dinero)
    
    # cv2.drawContours(img_rgb, contornos, -1, (0,0,255), 5)
    # plt.axis("off")
    # plt.imshow(img_rgb) 
    # plt.title('Todos los contornos')
    # plt.show()
    
identificar_moneda('Fotos/diferentes tipos.webp', "0.", True)