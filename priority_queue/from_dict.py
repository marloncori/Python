
countries = {
    7: "Japan", 
    5: "Brazil", 
    6: "Hungary", 
    2: "Poland", 
    4: "Spain", 
    3: "Korea", 
    1: "Israel"
}

if __name__ == '__main__':
    try:
        nations = countries.items()
        print(sorted(nations))
    except KeyboardInterrupt:
        print(" Program has ended. Bye-bye.")