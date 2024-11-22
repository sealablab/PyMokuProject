import sys


def compute_voltage(v_in: float):
    ## Example of one way to convert a floating point voltage into an singed integer with 10mV precision
    i = 0
    while (v_in - 0.001) > 0:
        i += 1  # throw another .001v on the tally
        v_in -= 0.001
        # print(f":i({i:03d}),  vin: {v_in:.6f}")

    ret = i * 0x290  # Some known constant
    # print(f"i: {i}, Final computed ret: {ret}")
    return ret


def parse_args():
    ret = float(sys.argv[1])
    return ret


if __name__ == "__main__":
    v_in = parse_args()
    ret_v = compute_voltage(v_in)
    if ret_v > 0x7FFF:
        print("Warning: Not sure what this value will do!")

    print(f"ComputeVoltage({v_in:.6f}) returned: ({ret_v:#08X})")
