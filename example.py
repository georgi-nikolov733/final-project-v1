import time

for i in range(1, 100):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        time.sleep(2)
    elif i % 3 == 0:
        print('Fizz')
        time.sleep(2)
    elif i % 5 == 0:
        print('Buzz')
        time.sleep(2)
    else:
        print(i)
