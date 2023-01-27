from time import sleep

my_food = (
    (1, 'bread'), 
    (5, 'mango'), 
    (3, 'arepa'), 
    (2, 'oranges'), 
    (0, 'rice'), 
    (6, 'chicken')
)

if __name__ == '__main__':
    try: 
        print("\t", sorted(my_food))

    except KeyboardInterrupt:
        print(" Program stopped. Goodbye!")