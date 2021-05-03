while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter an age higher than 0 ')
        break
    else:
        print('Thank you')
    finally:
        print('Ok, I am finally done')
    print('Can you hear me?')
