
#-----------------------------------------------------------------------------
def split_16_bits_to_2_bytes(bits: int) -> tuple:
    """Split 16 bts into two bytes, returns tutple with bytes split into
    high and low bytes respectively, ex: (high_byte, low_byte).
    bits: 16 bit integer to split into two bytes"""

    # using bitwise AND operator to mask 8 bits with 255
    return ((bits >> 8) & 0xFF, bits & 0xFF)
#-----------------------------------------------------------------------------
def twos_compliment(val: int, bits: int) -> int:
    """calculate two's compliment using a specified number of bits and
    return as an integer

    val: the value to take the two's compliment
    bits: the number of bits appropriate for the value"""

    # if the value is positive (or zero), there is no need
    # to apply twos compliment, we only need it for negative values

    comp = 0

    if val >= 0:
        comp = val

    else:
        # applying twos compiment by shiting 1 number of bits to the left
        # and adding the value to take the compliment
        comp = (1 << bits) + val

    return comp
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    try:

        velocity = -200
        result = twos_compliment(velocity, 16)
        print(" The velocity was {}, after conversion: {}.".format(velocity, result))
        data = split_16_bits_to_2_bytes(result)
        print(" 16 bits split into 2 bytes: {}.".format(data))
        radius = 500
        data2 = split_16_bits_to_2_bytes(radius)
        print("\n The radius was {} mm, after its 16 bits being split into 2 bytes -->: {}.".format(radius, data2))
        
    except (KeyboardInterrupt, SystemExit):
        print("\x01[1;31m {WARNING} User has stopped program.\x01[0m")
