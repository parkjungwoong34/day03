guess_me = 7
number = 1

while True:
    if guess_me > number:
        print('too low')
        break
    elif guess_me < number:
        print('oops')
        break
    else:
        print('found out')
        break