from math import pi


def calculate():
    while True:
        try:
            selector = input(
                "Please type '1' for circle or '2' for a home. Or type 'Quit' to quit.")
        except ValueError:
            print("Please type either a '1', '2', or 'Quit'.")
            continue
        if selector.lower() == 'quit':
            print('Good luck with you project!')
            break
        if selector == '1':
            while True:
                try:
                    radius = float(
                        input('What\'s the radius of your circle? (Please enter numbers only)'))
                except ValueError:
                    print('Please enter a number.')
                    continue
                if type(radius) == float:
                    # user input was a number
                    circumfrence = pi*(radius*2)
                    print(
                        f'The circumfrence of your circle is {circumfrence}.')
                    break

        if selector == '2':
            while True:
                try:
                    length = float(
                        input('What\'s the length of your house? (Please enter numbers only)'))
                except ValueError:
                    print('Please enter a number.')
                    continue
                try:
                    width = float(
                        input('What\'s the width of your house? (Please enter numbers only)'))
                except ValueError:
                    print('Please enter a number.')
                    continue
                if type(length) == float and type(width) == float:
                    # user input was a number
                    area = length * width
                    print(f'The area of your home is {area}.')
                break


calculate()
