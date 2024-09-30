import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('10-words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
                return f'Common match: {match} (#{i})'
        
def brute_force(word: str, length: int, digits:bool = False, symbols:bool = False):   
    chars: str = string.ascii_lowercase

    if digits:
         chars += string.digits
    
    if symbols:
         chars += string.punctuation
    
    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word: 
            return f'"{word}" was cracked in {attempts}'
    
        print(guess, attempts)

def main():
    print('Searching...')
    password: str ='xbc1'

    strart_time: float = time.perf_counter()

    if common_match:=common_guess(password):
        print(common_guess)
    else:
        if cracked := brute_force(password, length=4, digits=True, symbols=False):
            print(cracked)
        else:
            print('There was no match...')

    end_time: float = time.perf_counter()
    print(round(end_time - strart_time, 2))


if __name__ == '__main__':
    main()
         
    


