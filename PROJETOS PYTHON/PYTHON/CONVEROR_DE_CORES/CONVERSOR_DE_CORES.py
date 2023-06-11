import platform, os, math

CRED = '\33[31m'
CGREEN = '\33[32m'
CBLUE = '\33[34m'

messages = []

def clear_console():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    else:
        "\n\n @@@Não foi possível limpar o console@@@\n\n"

def user_menu():
    clear_console()
    print("Opções de Conversão:\n")
    print("1 - Normalizar um valor RGB")
    print("2 - Converter um valor RGB para HSV")
    print("3 - Converter um valor HSV para RGB")
    print("4 - Converter um valor RGB para CMYK")
    print("5 - Converter CMYK para RGB")
    print("6 - Converter um valor RGB para Escala de Cinza")
    print("0 - Sair")
    print("\n")
    read_messages()

    try:
        option = int(input("Escolha uma das opções disponíveis: "))
    except Exception as e:
        return None

    if option < 0 or option > 6:
        return None
    
    return option

def normalize_rgb(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    if (red, green, blue) == (0, 0, 0):
        return (0, 0, 0)

    total = red + green + blue
    normalized_red = red / total
    normalized_green = green / total
    normalized_blue = blue / total

    return (normalized_red, normalized_green, normalized_blue)

def rgb_to_hsv(rgb):
    r = rgb[0] / 255
    g = rgb[1] / 255
    b = rgb[2] / 255
    mini = min(r, g, b)
    maxi = max(r, g, b)

    if (mini == maxi):
        return (0, 0, mini)
    
    result_green_blue = g - b
    result_blue_red = b - r
    result_red_green = r - g

    to_use = result_green_blue
    to_add = 0

    if maxi == r:
        if g < b:
            to_add = 360
    else:
        if maxi == g:
            to_use = result_blue_red
            to_add = 120
        else:
            if maxi == b:
                to_use = result_red_green
                to_add = 240

    h = math.ceil(60*(to_use/(maxi-mini))+to_add)
    s = (maxi-mini)/maxi*100
    v = maxi*100

    return (h, s, v)

def hsv_to_rgb(hsv):
    h = float(hsv[0])
    s = float(hsv[1])
    v = float(hsv[2])
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    # r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def rgb_to_cmyk(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    if (red, green, blue) == (0, 0, 0):
        return 0, 0, 0, cmyk_scale

    c = 1 - red / 255
    m = 1 - green / 255
    y = 1 - blue / 255

    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    return c * 100, m * 100, y * 100, k * 100

def cmyk_to_rgb(cmyk):
    r = 255 * (1 - cmyk[0]/100) * (1 - cmyk[3]/100)
    g = 255 * (1 - cmyk[1]/100) * (1 - cmyk[3]/100)
    b = 255 * (1 - cmyk[2]/100) * (1 - cmyk[3]/100)
    return r,g,b

def rgb_to_gray_scale(rgb):
    messages.append(f'GRAY SCALE: {0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2]}')

def input_rgb():
    r = int(input("Informe o valor de r: "))
    g = int(input("Informe o valor de g: "))
    b = int(input("Informe o valor de b: "))
    return (r, g, b)

def input_hsv():
    h = int(input("Informe o valor de h: "))
    s = int(input("Informe o valor de s: "))
    v = int(input("Informe o valor de v: "))
    return (h, s, v)

def input_cmyk():
    c = int(input("Informe o valor de c: "))
    m = int(input("Informe o valor de m: "))
    y = int(input("Informe o valor de y: "))
    k = int(input("Informe o valor de k: "))
    return (c, m, y, k)

def print_rgb(result):
    messages.append(f"R: {result[0]}")
    messages.append(f"G: {result[1]}")
    messages.append(f"B: {result[2]}")

def print_hsv(result):
    messages.append(f"H: {result[0]}")
    messages.append(f"S: {result[1]}")
    messages.append(f"V: {result[2]}")

def print_cmyk(result):
    messages.append(f"C: {result[0]}")
    messages.append(f"M: {result[1]}")
    messages.append(f"Y: {result[2]}")    
    messages.append(f"K: {result[3]}")    

def read_messages():
    global messages
    for message in messages:
        print(message)
    messages = []
    print("\n")

def main():
    while True:
        chosen_option = user_menu()
        
        if None:
            print("A opção informada é inválida.")
        
        if chosen_option == 1:
            print_rgb(normalize_rgb(input_rgb()))
        elif chosen_option == 2:
            print_hsv(rgb_to_hsv(input_rgb()))
        elif chosen_option == 3:
            print_rgb(hsv_to_rgb(input_hsv()))
        elif chosen_option == 4:
            print_cmyk(rgb_to_cmyk(input_rgb()))
        elif chosen_option == 5:
            print_rgb(cmyk_to_rgb(input_cmyk()))
        elif chosen_option == 6:
            print(f'GRAY SCALE: {rgb_to_gray_scale(input_rgb())}')
        elif chosen_option == 0:
            break
main()