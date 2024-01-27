import random
import time
import numpy as np

def main():
    # generate random 20000 values
    NUMBER_OF_VALUES = 90000000

    # create a list of values from 0 do NUMBER_OF_VALUES
    values = list(range(NUMBER_OF_VALUES))


    CHOICE = 90000001

    # This is first way of checking if value is in list
    start = time.time()
    for_finding_value(values, CHOICE)
    end = time.time()
    print(f"Time for finding value in list: {end - start}")


    # This is second way of checking if value is in list
    start = time.time()
    for_finding_value_numpy(values, CHOICE)
    end = time.time()
    print(f"Time for finding value in list: {end - start}")

    start = time.time()
    for_finding_value_weird_way(values, CHOICE)
    end = time.time()
    print(f"Time for finding value in list: {end - start}")


def for_finding_value(values, CHOICE):
    found_status = False
    for value in values:
        if value == CHOICE:
            print(f"Found value {value}")
            found_status = True
            break
        else:
            found_status = False

    if not found_status:
        print(f"Value {CHOICE} not found")

def for_finding_value_numpy(values, CHOICE):
    np_values = np.array(values)
    if CHOICE in np_values:
        print(f"Found value {CHOICE}")
    else:
        print(f"Value {CHOICE} not found")

def for_finding_value_weird_way(values, CHOICE):
    len_before = len(values)
    values.append(CHOICE)
    len_after = len(set(values))

    if len_before != len_after:
        print(f"Found value {CHOICE}")
    else:
        print(f"Value {CHOICE} not found")


if __name__ == "__main__":
    main()