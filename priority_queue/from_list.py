from time import sleep

employees = []
employees.append((1, 'Andrew'))

# sort it every time a new element is added
employees.append((4, 'John'))
employees.sort(reverse = True)

employees.append((3, 'Jane'))
employees.sort(reverse = True)

employees.append((2, 'Matt'))
employees.sort(reverse = True)

employees.append((5, 'Beniamin'))
employees.sort(reverse = True)

if __name__ == '__main__':
    try: 
        while employees:
            print(employees.pop())
            sleep(0.4)

    except KeyboardInterrupt:
        print(" Program stopped. Goodbye!")