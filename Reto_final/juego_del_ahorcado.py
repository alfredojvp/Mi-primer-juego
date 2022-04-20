import random
import os
import time





title = """ /$$$$$$$$ /$$        /$$$$$$  /$$                                                     /$$          
| $$_____/| $$       /$$__  $$| $$                                                    | $$          
| $$      | $$      | $$  \ $$| $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$ 
| $$$$$   | $$      | $$$$$$$$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$ /$$__  $$
| $$__/   | $$      | $$__  $$| $$  \ $$| $$  \ $$| $$  \__/| $$        /$$$$$$$| $$  | $$| $$  \ $$
| $$      | $$      | $$  | $$| $$  | $$| $$  | $$| $$      | $$       /$$__  $$| $$  | $$| $$  | $$
| $$$$$$$$| $$      | $$  | $$| $$  | $$|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/
|________/|__/      |__/  |__/|__/  |__/ \______/ |__/       \_______/ \_______/ \_______/ \______/
                                               By Alfred Chiken"""



logo = """   |/|
   | |
   |/|
   | |
   |/|
  (___)
  (___)
  (___)
  (___)
  (___)
  // \\
 //   \\
||     ||
||     ||
||     ||
 \\___//
  -----"""

win = """
                                                   .''''.
                                                  /,.--. )
                             .'``.        __   __((\- -(\)
                    _______.'     \_.-''''  ``'  /)) - .\|
   __....::::::::::'''''''/    .   \.'''''''::::::(/ `-'`.)
.:'::.  .  o ~ .  ~  o ~ /    /     '.o ~ . _.....--- `  \.
 ':. ':::::.___.____,___/   ,'_\      \ _.-'___..___..._,'
   ':.  o~  `::::::::::::::::::::::::::::::::::::::::'  (\.
    `':.  o ~  o   ..   o  ,  ~  \ . o~   -.  ~   .'.:'\.'(
       ':.  ,..   o  ~   o  . ,  'o.    ~ o   ~ o'.:'  \(/
         '.   o   ~   .    ~    o ~ ',o :  :  .' .' ('\/ |
           '-._    ~    o  , o  ,  .  ~._ _.o_.-'  \/ ) (
               '- .._  .    ~    ~      _.. -'
                     ''' - .,.,. - '''
                          (:' .:)
                           :| '|
                           |. ||
                           || :|
                           :| |'
                           || :|
                           '| ||
                           |: ':
                           || :|
                     __..--:| |'--..__
               _...-'  _.' |' :| '.__ '-..._
             / -  ..---    '''''   ---...  _ \ 
             \  _____  ..--   --..     ____  /
              '-----....._________.....-----'   """



lost = """
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
 _______  _______  _______  ______  _________ _______  _________ _______ 
(  ____ )(  ____ \(  ____ )(  __  \ \__   __/(  ____ \ \__   __/(  ____ \.
| (    )|| (    \/| (    )|| (  \  )   ) (   | (    \/   ) (   | (    \/
| (____)|| (__    | (____)|| |   ) |   | |   | (_____    | |   | (__    
|  _____)|  __)   |     __)| |   | |   | |   (_____  )   | |   |  __)   
| (      | (      | (\ (   | |   ) |   | |         ) |   | |   | (      
| )      | (____/\| ) \ \__| (__/  )___) (___/\____) |   | |   | (____/\.
|/       (_______/|/   \__/(______/ \_______/\_______)   )_(   (_______/
                                                                        """


lost2 = """⠘¡Seguro eres de los que compró⡜⠀⠀⠀
⠀⠀⠀⠑⡀⠀⠀⠀⠀           ⠀⠀⠀⠀⠀⠀⠀         ⠀⡔⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀BTC en 69K!⠀⠀          ⣀⠴⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠒⠒⠒⠒⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡰⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠙⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⢠⠂⠀⠀⠘⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⢤⡀⢂⠀⢨⠀⢀⡠⠈⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⢀⡖⠒⠶⠤⠭⢽⣟⣗⠲⠖⠺⣖⣴⣆⡤⠤⠤⠼⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡈⠃⠀⠀⠀⠘⣺⡟⢻⠻⡆⠀⡏⠀⡸⣿⢿⢞⠄⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⡀⠤⡀⡀⡔⠉⣏⡿⠛⠓⠊⠁⠀⢎⠛⡗⡗⢳⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢱⠀⠨⡇⠃⠀⢻⠁⡔⢡⠒⢀⠀⠀⡅⢹⣿⢨⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠠⢼⠀⠀⡎⡜⠒⢀⠭⡖⡤⢭⣱⢸⢙⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠸⢁⡀⠿⠈⠂⣿⣿⣿⣿⣿⡏⡍⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠸⢢⣫⢀⠘⣿⣿⡿⠏⣼⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⠊⠀⣀⠎⠁⠀⠀⠀⠙⠳⢴⡦⡴⢶⣞⣁⣀⣀⡀⠀⠀⠀⠀⠀
⠀⠐⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢀⠤⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀"""


display_board = """

Bienvenido al beta test del juego del ahorcado

Desarrollado por Alfred Chicken

Presiona enter para comenzar: """

os.system("clear")
print(title)
print(logo)

tap = input(display_board)
if len(tap) > 0:
    os.system("clear")
    print("\nVerga...¿¿¿es que eres marica o que es la vaina????")
else:
    os.system("clear")
    print("...El juego está en cronstrucción amigo, esperate...")
    time.sleep(2)
    os.system("clear")
    print("De todas maneras, te dire cuales serán las condiciones del juego para cuando este listo...")
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    print("El objetivo del juego es adivinar la palabra secreta, letra por letra.")
    time.sleep(2)
    print("Tienes 6 vidas, pierdes una vida por cada intento fallido en adivinar la letra.")
    time.sleep(2)
    print("Con cada intento fallido se irá dibujando al hombre ahorcado.")
    time.sleep(2)
    print("Si te quedas sin vidas, el hombre ahorcado se habrá dibujado en su totalidad y perderás.")
    time.sleep(2)
    os.system("clear")
    


   
    def read_data():
        with open("./archivos/data.txt", "r") as f:
            repo = [line.strip("\n") for line in f]
            
        dic_words = {key:value for key, value in enumerate(repo)}
        return dic_words

    def normalize(s): #Esto removerá el acento de las vocales
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s





def run():
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    dic_words = read_data()
    choosed_word = dic_words.get(random.randint(1, len(dic_words) + 1))
    guessing_word = len(choosed_word) * ["_"]

        

    ##La cantidad de vidas disponible:
    lives = -6
    ##En esta lista se introducen los intentos de letras adivinadas
    try_letters_list = []
    ##En esta lista se introducen las letras adivinadas
    discover_letters_list = []
    ##En esta lista indice se introducen los indices de cada elemento de la lista letras adivinadas
    #letter_index_letter = {}
    ##Estrucutura para la imprimir la palabra a adivinar sin letra
    ##print("_" *len())




        
    while True:
        for character in guessing_word:
            print(character, end=" ")
        print(HANGMANPICS[lives])
        try_letter = input("\nAdivina las letras: ")
        if len(try_letter) != 1:
            print("Por favor, introduce solo una letra")
        if try_letter.lower() in try_letters_list:
            print("Ya haz intentado con esta letra")
            time.sleep(0.5)
            os.system("clear")
        else:
            try_letters_list.append(try_letter)
            if try_letter.lower() in choosed_word:
                try_letter.join(discover_letters_list)
                guessing_word = list(guessing_word)
                for idx, character in enumerate(choosed_word):
                    if character == try_letter:
                        guessing_word[idx] = try_letter
                        os.system("clear")
                #print("Adivinaste una letra")
                    else:
                        if "_" not in guessing_word:
                            print("¡Ganaste, la palabra era " + choosed_word + "!")
                            print(win)
                            try_again = int(input("¿Quieres jugar una partida más?: \n1-> Si \n2-> No \nElige una opción: "))
                            if try_again == 1:
                                run()
                            else:
                                if try_again == 2:
                                    exit()
                            break
                
            else:
                lives = lives + 1
                print("\nTe equivocaste")
                print("Te quedan " + str(-1 * lives) + " vidas" )
                time.sleep(1)
                os.system("clear")
                if lives == 0:
                    print("¡Perdiste!. La palabra secreta era " + choosed_word)
                    print(lost)
                    try_again = int(input("¿Quieres volver a intentarlo?: \n1-> Si \n2-> No \nElige una opción: "))
                    if try_again == 1:
                        run()
                    elif try_again == 2:
                        print("\n")
                        print(lost2)
                        exit()

                

    


if __name__ == '__main__':
    run()