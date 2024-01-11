import random

logo = '''                                                                                                                               
     ***** **                               *                 ***** **              *          *                               
  ******  **** *                          **               ******  ***      *     **         **                                
 **   *  *  ***                           **             **    *  * ***    ***    **         **                                
*    *  *    *                            **            *     *  *   ***    *     **         **                                
    *  *         **   ****                **                 *  *     ***         **         **                   ***  ****    
   ** **          **    ***  *    ****    **  ***           ** **      ** ***     ** ****    ** ****       ***     **** **** * 
   ** **          **     ****    * ***  * ** * ***          ** **      **  ***    *** ***  * *** ***  *   * ***     **   ****  
   ** ******      **      **    *   ****  ***   *           ** **      **   **    **   ****  **   ****   *   ***    **         
   ** *****       **      **   **         **   *            ** **      **   **    **    **   **    **   **    ***   **         
   ** **          **      **   **         **  *             ** **      **   **    **    **   **    **   ********    **         
   *  **          **      **   **         ** **             *  **      **   **    **    **   **    **   *******     **         
      *           **      **   **         ******               *       *    **    **    **   **    **   **          **         
  *****            ******* **  ***     *  **  ***         *****       *     **    **    **   **    **   ****    *   ***        
 *  *****           *****   **  *******   **   *** *     *   *********      *** *  *****      *****      *******     ***       
*    ***                         *****     **   ***     *       ****         ***    ***        ***        *****                
*                                                       *                                                                      
 **                                                      **                                                                                                                       
                                                                                                                     
'''
print(logo)
choice = random.randint(1, 100)

mode = 0
if input("Easy or Hard ").lower() == "easy":
    mode = 10
    print("You have 10 attempts")
else:
    mode = 5
    print("You have 5 attempts")


while mode > 0:
    guess = int(input("Guess a number "))
    if guess == choice:
        print("Correct! You win!")
        break
    elif guess > choice:
        mode -= 1
        print("Too high")
        print(f"{mode} attempts left.")
    else:
        mode -= 1
        print("Too Low")
        print(f"{mode} attempts left.")

else:
    print("GG shitter, you lost")
    print(f"It was {choice}")

