import time

for i in range(1, 100):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        time.sleep(5)
    elif i % 3 == 0:
        print('Fizz')
        time.sleep(5)
    elif i % 5 == 0:
        print('Buzz')
        time.sleep(5)
    else:
        print(i)
