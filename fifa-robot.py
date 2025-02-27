import pyautogui
import pydirectinput
import pygetwindow as gw
import dxcam
import time
import subprocess
import pytesseract
from PIL import Image
from PIL import ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Verifica daca fereastra GameRanger: Bronze este deja deschisa
def is_window_open(window_title):
    return window_title in (win.title for win in gw.getWindowsWithTitle(window_title))

# Deschide GameRanger daca nu este deja deschis
def open_game_ranger():
    game_ranger_path = r"C:\Users\Administrator\AppData\Roaming\GameRanger\GameRanger\GameRanger.exe"
    subprocess.Popen(game_ranger_path)

# Activeaza fereastra
def activate_window(window_title):
    window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()

# Asteapta cateva secunde pentru a da timp aplicatiei sa se incarce
def wait(seconds):
    time.sleep(seconds)

# Simuleaza combinatii de taste
def send_keys(keys):
    pyautogui.write(keys)
    pyautogui.press('enter')

def preprocess_image(image):
    # Îmbunătățește contrastul
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Ajustează factorul de contrast
    
    # Convertește imaginea într-un format alb-negru
    image = image.convert('L')  # Convertim imaginea la gri
    image = image.point(lambda p: 255 if p > 128 else 0)
    # image = image.point(lambda p: p > 128 and 255)  # Transformăm la alb și negru

    return image

def preprocess_image2(image):
    # Îmbunătățește contrastul
    enhancer = ImageEnhance.Contrast(image)
    
    # Convertește imaginea într-un format alb-negru
    image = image.convert('L')  # Convertim imaginea la gri
    image = image.point(lambda p: 255 if p > 128 else 0)
    # image = image.point(lambda p: p > 128 and 255)  # Transformăm la alb și negru

    return image

# Muta cursorul si face click
def click_at_position(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Functie care citeste textul dintr-o captura de ecran a chatului
def read_chat_from_screenshot():
    screenshot = pyautogui.screenshot(region=(10, 90, 450, 380))
    screenshot.save("chat_screenshot.png")
    screenshot = preprocess_image(screenshot)
    
    text = pytesseract.image_to_string(screenshot)
    
    return text.lower()

# def extract_coordinates_for_text():
#     screenshot = pyautogui.screenshot(region=(10, 90, 450, 380))  # Regiunea de captură a ecranului
#     screenshot.save("chat_screenshot2.png")
    
#     # Preprocesare imagine (opțional, dacă este necesar)
#     screenshot = preprocess_image(screenshot)
    
#     # Folosește pytesseract pentru a obține datele complete (text + coordonate)
#     data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    
#     # Afișează textul complet recunoscut de pytesseract pentru a înțelege ce se extrage
#     full_text = " ".join(data['text'])
#     print("Textul complet recunoscut:", full_text)  # Pentru debugging
    
#     # Căutăm fraza întreagă
#     target_text = "<<hm - berserk joined the room >>"  # Folosește litere mici pentru căutare
    
#     # Reconstruim fraza completă din cuvintele extrase și o normalizăm
#     reconstructed_text = " ".join([word.strip().lower() for word in data['text']])
#     print("Textul reconstruit:", reconstructed_text)  # Pentru debugging
    
#     # Comparăm fraza completă recunoscută cu fraza căutată (ambele în litere mici)
#     if target_text.lower() in reconstructed_text:
#         # Dacă fraza a fost găsită, extragem coordonatele
#         for i, word in enumerate(data['text']):
#             print(f"{reconstructed_text}")  # Afișează tot textul extras
#             if word.strip().lower() == "berserk":  # Căutăm un cuvânt cheie sau primul cuvânt din frază
#                 x = data['left'][i]
#                 y = data['top'][i]
#                 width = data['width'][i]
#                 height = data['height'][i]
                
#                 print(f"Textul '{target_text}' a fost găsit la coordonatele: (x: {x}, y: {y}, width: {width}, height: {height})")
#                 return x, y  # Returnează coordonatele
    
#     print(f"Fraza '{target_text}' nu a fost găsită în captura de ecran.")
#     return None, None  # Dacă fraza nu a fost găsită, returnează None


def check_for_start_in_fifa():
    camera = dxcam.create(output_color="RGB")
    region = (95, 350, 275, 460)
    
    time.sleep(1)
    
    frame = camera.grab(region=region)
    
    if frame is not None:
        image = Image.fromarray(frame)
        image.save("game_screenshot.png")
        image = preprocess_image2(image)
        text = pytesseract.image_to_string(image)
        return text.lower()
    return None

def esc_from_first_half():
    camera = dxcam.create(output_color="RGB")
    region = (250, 30, 300, 50)

    frame = camera.grab(region=region)

    if frame is not None:
        image = Image.fromarray(frame)
        image.save("firsthalf_exit.png")
        image = preprocess_image(image)
        text = pytesseract.image_to_string(image)
        return text
    return None

def esc_from_second_half():
    camera = dxcam.create(output_color="RGB")
    region = (250, 30, 300, 50)

    frame = camera.grab(region=region)

    if frame is not None:
        image = Image.fromarray(frame)
        image.save("secondhalf_exit.png")
        image = preprocess_image(image)
        text = pytesseract.image_to_string(image)
        return text
    return None

# Deschide GameRanger daca nu este deja deschis
if not is_window_open("GameRanger: Bronze"):
    open_game_ranger()

wait(5)  # Asteapta 5 secunde pentru a da timp GameRanger sa se incarce

# Activeaza fereastra GameRanger: Bronze
if is_window_open("GameRanger: Bronze"):
    activate_window("GameRanger: Bronze")
    wait(1)

    # Apasa Ctrl+G pentru a deschide fereastra de creare a camerei
    pyautogui.hotkey('ctrl', 'g')
    wait(1)

    # Apasa Enter pentru a confirma si crea camera
    send_keys('')

    wait(2)

    # Apasa ALT pentru a activa meniul si folosește sagetile
    pyautogui.hotkey('alt')
    pyautogui.press('up')
    pyautogui.press('left')

    # Apasa de mai multe ori sagetile pentru a naviga
    for _ in range(4):
        pyautogui.press('down')

    send_keys('')  # Apasa Enter pentru a confirma

    # Monitorizează chatul pentru mesajul '!start'
    while True:
        chat_text = read_chat_from_screenshot()

        # Apelăm funcția pentru a extrage coordonatele textului căutat
        # x, y = extract_coordinates_for_text()

        # Verificăm dacă coordonatele au fost găsite
        # if x is not None and y is not None:
        #     pyautogui.write('Welcome @')
        #     pyautogui.press('enter')
        
        # Verifică dacă mesajul '!start' există în chat
        if 'hm - berserk: !start' in chat_text:
            print("Mesajul !start a fost detectat! Pornim jocul...")
            
            # Muta cursorul la coordonatele 641, 551 si apasa pe butonul "Start"
            pyautogui.write('ATTENTION: the server will start after .5 seconds.')
            pyautogui.press('enter')
            wait(5)
            click_at_position(641, 551)
            wait(1)  # Pauză de 3 secunde după ce ai dat click pe butonul "Start"
            break  # Iese din buclă odată ce a fost găsit mesajul și jocul a început

        # Așteaptă 3 secunde înainte de a verifica din nou chatul, pentru a reduce încărcarea CPU-ului
        time.sleep(10)  # Pauză între verificările chatului
    
    wait(5)

    # Activeaza fereastra jocului FIFA
    if is_window_open("FIFA"):
        activate_window("FIFA")

    wait(2)
    pydirectinput.press('enter')
    wait(13)
    pydirectinput.press('space')
    wait(4)
    pydirectinput.press('space')
    wait(2)
    pydirectinput.press('down')
    wait(1)
    pydirectinput.press('enter')
    wait(0.5)
    pydirectinput.press('enter')
    wait(0.5)
    pydirectinput.press('enter')
    wait(5)
    pydirectinput.press('esc')
    wait(1.5)
    pydirectinput.press('down')
    wait(0.5)
    pydirectinput.press('down')
    wait(0.5)
    pydirectinput.press('enter')
    wait(0.5)
    pydirectinput.press('down')
    wait(0.5)
    pydirectinput.press('enter')
    wait(0.5)
    pydirectinput.press('down')
    wait(0.5)
    pydirectinput.press('enter')
    wait(1)
    pydirectinput.press('enter')
    wait(2)
    pydirectinput.write('robohost')
    wait(1)
    pydirectinput.press('enter')
    wait(1)
    pydirectinput.press('s')
    wait(1)
    pydirectinput.press('enter')
    pydirectinput.write('robo-room')
    wait(1)
    pydirectinput.press('enter')
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('right')
    pydirectinput.press('s')
    wait(2)

    while True:
        chat_game = check_for_start_in_fifa()
        
        if chat_game and '!start' in chat_game:
            break

        time.sleep(15)
    
    wait(2)
    pydirectinput.press('q')
    time.sleep(1)
    pydirectinput.write('game start in 5 sec')
    time.sleep(3)
    pydirectinput.press('enter')
    wait(2)
    pydirectinput.press('enter')
    wait(10)
    pydirectinput.press('right')
    wait(2)
    pydirectinput.press('enter')
    wait(10)
    pydirectinput.press('space')
    wait(4)
    pydirectinput.press('space')
    wait(15)
    pydirectinput.press('space')
    wait(2)

    while True:
        first_half = esc_from_first_half()

        print(first_half)
        
        if first_half and ('0' in first_half or '1' in first_half or '2' in first_half):
            break
    
    wait(2)
    pydirectinput.keyDown('esc')
    time.sleep(1)
    pydirectinput.keyUp('esc')
    time.sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    wait(1)
    pyautogui.keyUp('alt')
    wait(2)

    start_time = time.time()  # Timpul curent la începutul execuției
    duration = 60  # Durata totală de execuție a ciclului, în secunde

while True:
    chat_text = read_chat_from_screenshot()
    if '!abort' in chat_text:
        print("Mesajul !abort a fost detectat! Oprim jocul...")
        break

    click_at_position(602, 282)
    time.sleep(1)

    if time.time() - start_time > duration:
        print("Timpul de 400 de secunde a fost atins. Deschidem jocul...")
        break

    time.sleep(15)

time.sleep(4)
pyautogui.keyDown('alt')
wait(1)
pyautogui.press('tab')
pyautogui.press('right')
pyautogui.keyUp('alt')
wait(4)

while True:
    second_half = esc_from_second_half()

    if second_half and ('45' in second_half or '46' in second_half or '47' in second_half):
        break

wait(2)
pydirectinput.keyDown('esc')  # Simulează apăsarea tastei ESC
time.sleep(3)  # Ține apăsată tasta pentru 3 secunde
pydirectinput.keyUp('esc')  # Eliberează tasta ESC
wait(2)
pyautogui.keyDown('alt')
wait(1)
pyautogui.press('tab')
pyautogui.press('left')
pyautogui.keyUp('alt')

start_time = time.time()  # Timpul curent la începutul execuției
duration = 60  # Durata totală de execuție a ciclului, în secunde


while True:
    chat_text = read_chat_from_screenshot()
    if '!abort' in chat_text:
        print("Mesajul !abort a fost detectat! Oprim jocul...")
        break

    click_at_position(602, 282)
    time.sleep(1)

    if time.time() - start_time > duration:
        print("Timpul de 400 de secunde a fost atins. Deschidem jocul...")
        break

    time.sleep(15)