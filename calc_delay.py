
#-----------------------------------------------------------------------------#    
params = {
        'movlw' : 1,
        'movwf' : 1,
        'ret' : 2,
        'retlw' : 2,
        'call' : 2,
        'goto' : 2,
        'decf': 1,
        'decfsz': 1,
    }
#-----------------------------------------------------------------------------#
def get_user_data():
    global params
    opcodes = []   
    print("*" * 30)
    print(" * PIC DELAY CALCULATOR *")
    print("*" * 30)

    print(" Let us count how many cycles your delay routine takes:")
    print("""
            number of 'movlw' : """)
    movlw = int(input())
    opcodes.append(movlw)
    
    print("""
            number of 'movwf' : """)
    movwf = int(input())
    opcodes.append(movwf)
    print("""
            number of 'retlw' : """)
    retlw = int(input())
    opcodes.append(retlw)
    print("""
            number of 'ret' : """)
    ret = int(input())
    opcodes.append(ret)
    print("""
            number of 'call' : """)
    call = int(input())
    opcodes.append(call)
    print("""
            number of 'goto' : """)
    goto = int(input())
    opcodes.append(goto)
    print("""
            number of 'decf' : """)
    decf = int(input())
    opcodes.append(decf)
    print("""
            number of 'decfsz' : """)
    decfsz = int(input())
    opcodes.append(decfsz)

    print("""
            how many counters have been used? """)
    counters = int(input())
    if counters == 1:
            print("""
                type its value here: """)
            count1 = int(input())
            opcodes.append(count1)
    elif counters == 2:
            print("""
                type first value here: """)
            count1 = int(input())
            opcodes.append(count1)
            print("""
                type second value here: """)
            count2 = int(input())
            opcodes.append(count2)
    elif counters == 3:
            print("""
                type 1. value here: """)
            count1 = int(input())        
            opcodes.append(count1)
            print("""
                type 2. value here: """)
            count2 = int(input())        
            opcodes.append(count2)
            print("""
                type 3. value here: """)
            count3 = int(input())        
            opcodes.append(count3)
            
    return opcodes
#-----------------------------------------------------------------------------#
def calc_delay_time(data):
    global params
    result = 0
    if len(data) == 9:
        result = params['movlw']*data[0] + params['movwf']*data[1] + params['ret']*data[2] + params['retlw']*data[3] + params['call']*data[4] + params['goto']*data[5]*data[8] + params['decf']*data[6] + params['decfsz']*data[7]
    elif len(data) == 10:
        result = params['movlw']*data[0] + params['movwf']*data[1] + params['ret']*data[2] + params['retlw']*data[3] + params['call']*data[4] + params['goto']*data[5]*data[8]*data[9] + params['decf']*data[6] + params['decfsz']*data[7]
    elif len(data) == 11:
        result = params['movlw']*data[0] + params['movwf']*data[1] + params['ret']*data[2] + params['retlw']*data[3] + params['call']*data[4] + params['goto']*data[5]*data[8]*data[9]*data[10] + params['decf']*data[6] + params['decfsz']*data[7]

    result = result * 0.0000001
    return result
#-----------------------------------------------------------------------------#    

if __name__ == '__main__':
    
    data = get_user_data()
    result = calc_delay_time(data)
    print(" The total time is: {} second.".format(result))

#-----------------------------------------------------------------------------#    
