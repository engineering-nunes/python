from random import randint

if __name__ == '__main__':
    print('Welcome, you have 3 trials to guess the int number between 1 and 10.')
    number = randint(1,10)
    for i in range(3):  
         try:
          usuary_number = int(input('Guess the number: '))
         except ValueError:
            print(f'Please enter a valid integer, you can try again {2-i} times.')
            continue
         if usuary_number == number:
             print ('You won it.')
             break
         else:
             print(f'You lost this trial, you can try again {2-i} times.')
    
    else:
        print(f'Sorry, you lost. The correct number was the number {number}.')
         
    
    
    



