

def arduino_map(read_val, max_val, max_output):
    return (read_val / max_val) * max_output

if __name__ == '__main__':
    try:
        reading = 1.364
        max_voltage = 2.50
        max_counting = 1023.0
        result = arduino_map(reading, max_voltage, max_counting)
        print(" ==> [TENSION SENSOR] read value: {:.3f}.".format(result))

        reading = 127.5
        max_voltage = 255.0
        max_counting = 1023.0
        result = arduino_map(reading, max_voltage, max_counting)
        print(" ==> [POTENTIOMETER] read value: {:.3f}.".format(result))
    except KeyboardInterrupt:
        print("\x1b[1;31m --> Program has been aborted! \x1b[0m")
