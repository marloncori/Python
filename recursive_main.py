from time import sleep

################## recursion

def main():
    user = str(input("Enter something below: "))
    print("  You have type: ", user)
    if user != "stop":
        main()
    else:
        print("\t Ok. Bye, bye!")

main()

################## recursion
        
def num_main(m, n):
    if m <= n:
        print(m)
        sleep(0.3)
        num_main(m+1, n)
    else:
        print("  We are done couting.")
        
num_main(2, 20)
