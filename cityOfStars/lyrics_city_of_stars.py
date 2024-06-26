import sys 
import time 
from time import sleep
import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def print_lyrics():
  lines = [
      ('★ ★ ★ ★ ★ ★ ★', 0.55),
      ('City of stars', 0.18),
      ('★ ★ ★ ★', 0.2),
      ('Are you shining just for me?', 0.1),
      ('★ ★ ★ ★ ★ ★ ★ ★ ★', 0.20),
      ('City of stars', 0.18),
      ('★ ★ ★ ★', 0.2),
      ('There\'s so much that I can\'t see', 0.07),
      ('★ ★ ★ ★', 0.5),
      ('Who knows?', 0.04),
      ('★ ★ ★ ★', 0.5),
      ('Is this the start of something wonderful and new?', 0.07),
      ('★ ★ ★ ', 0.5),
      ('Or one        more    dream                           that★★★ I cannot make true?', 0.09),
      ('Preguiça de escrever o resto, então fique com essas estrelas =)', 0.1),
      ("""\033[33m
       .                                                            .                               
      .+-   -                 .                  .                  =                   .           
     .=%#-. *                 -:                :*+.                #.                 .-.          
       -...:%...              +=             :   -.              ...%- :           .    .           
       .  =*@*-               ##             .      .             ++@**.           .                
      .-+#%@@@%#+-.      .:-=*@@*+=-:          .   :=        .:-=+*@@@#+=-:.              :         
         .=%@%-.         .:-=+%@+=:.          .+.    .        .:-=*@@@#=-:..         ..             
         .::@.-.              *%                    .*:          .+=@++:                   ::       
           .#                 -*             -.      .           .  %- .            .               
            =  .=             .=            :*=.   :.               #.             :-.    .         
            . .=*:             .             .                      =                               
                .                                                   .                               
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
       :    :                                    .              :    .                 :            
     .:+:. .-                 .+.                *            .:#-.  :                 -.           
       :   :=                 .-                -@.             :   .=                 =:           
           -+             ..                   .#@*.               ::+:.               +-           
     .::-==*#==--:.              -.         .-+%@@@%=:.        .::-=%@*--:.      .:--==#*==-::.     
        ...=*:..            .-             .=+#@@@@@#+=.          .:#%+.            ..:*=:..        
           :+                .    :=           -%@%:               ..+..               +:           
           .=              .       .            =@:                  =                 =:           
           .-  .          :+.    .              .#                   :  ..             :.           
            . .-:          .     .               -                     .-=.            .            
               .                                                         .                          
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
            .             -.   :                 :                                 ..               
           -#:          .-#+:  *                 -                  :=.           .++.  .           
       .   .+             -.  .%.                +                  .:            -##-  *           
       :                      -@-              :.#.:            .                  :.  :@-          
              +.          :=+#%@%%*+-.       ..-%@#:..                 -             .-%@%=.        
         --               ..:-+@*-.        .:--=%@%=--:.          -.               .+#@@@@@%+:      
               ==             .@-              -:#-:                    -.            :#@%-         
        :      ..              #.                +              ..      .              :@-          
       =#.   .:                =   :             =             .=-    ..                *           
        .     .                   -+.            :              .                       .  :*.      
                                   .                                                       :*.      
                                                                                                    
                                                                                                    
                                                         \033[0m""", 0.005),
      ("""\033[35m
       .                                                            .                               
      .+-   -                 .                  .                  =                   .           
     .=%#-. *                 -:                :*+.                #.                 .-.          
       -...:%...              +=             :   -.              ...%- :           .    .           
       .  =*@*-               ##             .      .             ++@**.           .                
      .-+#%@@@%#+-.      .:-=*@@*+=-:          .   :=        .:-=+*@@@#+=-:.              :         
         .=%@%-.         .:-=+%@+=:.          .+.    .        .:-=*@@@#=-:..         ..             
         .::@.-.              *%                    .*:          .+=@++:                   ::       
           .#                 -*             -.      .           .  %- .            .               
            =  .=             .=            :*=.   :.               #.             :-.    .         
            . .=*:             .             .                      =                               
                .                                                   .                               
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
       :    :                                    .              :    .                 :            
     .:+:. .-                 .+.                *            .:#-.  :                 -.           
       :   :=                 .-                -@.             :   .=                 =:           
           -+             ..                   .#@*.               ::+:.               +-           
     .::-==*#==--:.              -.         .-+%@@@%=:.        .::-=%@*--:.      .:--==#*==-::.     
        ...=*:..            .-             .=+#@@@@@#+=.          .:#%+.            ..:*=:..        
           :+                .    :=           -%@%:               ..+..               +:           
           .=              .       .            =@:                  =                 =:           
           .-  .          :+.    .              .#                   :  ..             :.           
            . .-:          .     .               -                     .-=.            .            
               .                                                         .                          
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
            .             -.   :                 :                                 ..               
           -#:          .-#+:  *                 -                  :=.           .++.  .           
       .   .+             -.  .%.                +                  .:            -##-  *           
       :                      -@-              :.#.:            .                  :.  :@-          
              +.          :=+#%@%%*+-.       ..-%@#:..                 -             .-%@%=.        
         --               ..:-+@*-.        .:--=%@%=--:.          -.               .+#@@@@@%+:      
               ==             .@-              -:#-:                    -.            :#@%-         
        :      ..              #.                +              ..      .              :@-          
       =#.   .:                =   :             =             .=-    ..                *           
        .     .                   -+.            :              .                       .  :*.      
                                   .                                                       :*.      
                                                                                                    
                                                                                                    
                                                         \033[0m""", 0.005),
      ("""\033[34m
       .                                                            .                               
      .+-   -                 .                  .                  =                   .           
     .=%#-. *                 -:                :*+.                #.                 .-.          
       -...:%...              +=             :   -.              ...%- :           .    .           
       .  =*@*-               ##             .      .             ++@**.           .                
      .-+#%@@@%#+-.      .:-=*@@*+=-:          .   :=        .:-=+*@@@#+=-:.              :         
         .=%@%-.         .:-=+%@+=:.          .+.    .        .:-=*@@@#=-:..         ..             
         .::@.-.              *%                    .*:          .+=@++:                   ::       
           .#                 -*             -.      .           .  %- .            .               
            =  .=             .=            :*=.   :.               #.             :-.    .         
            . .=*:             .             .                      =                               
                .                                                   .                               
                                                                                                    
                                                                                                    
                                                                                 \033[0m""", 0.005)

  ]

  
  for i, (line, char_delay) in enumerate(lines):
    for char in line:
      print(char, end='')
      sys.stdout.flush()
      sleep(char_delay)
    print('')

if __name__ == "__main__":
    music_file = "cityOfStars.mp3"
    play_music(music_file)
    print_lyrics()

print("") 
