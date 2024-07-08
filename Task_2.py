from collections import deque


def is_palindrome(characters):

    characters2 = characters.upper().replace(" ", "")

    character_deque = deque(characters2)

    
  

    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return False

    return characters2 


print(is_palindrome('lsdkjfskf') )  
print(is_palindrome(' radar'))

