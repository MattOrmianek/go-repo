import time
import numpy as np

def main():
    avg_time = run_multiple_times(2)
    avg_time_numpy = run_multiple_times_numpy(10)
    time_for_go = 0.003264804569999999
    print(f"GO is {avg_time / time_for_go } times faster than python - without numpy")
    print(f"GO is {avg_time_numpy / time_for_go } times faster than python - with numpy")

def run_multiple_times(number_of_times):
    time_array = []
    for i in range(number_of_times):
        time_array.append(run_me_loop_and_time_it(10000000, 50))
    return sum(time_array) / len(time_array)

def run_multiple_times_numpy(number_of_times):
    time_array = []
    for i in range(number_of_times):
        time_array.append(run_me_loop_and_time_it_numpy(10000000, 50))
    return sum(time_array) / len(time_array)


def run_me_loop_and_time_it(number_of_times, number_to_calculate):
    start = time.time()
    for i in range(number_of_times):
        calcualte_me_something(i, number_to_calculate)
    end = time.time()
    return end - start

def run_me_loop_and_time_it_numpy(number_of_times, number_to_calculate):
    start = time.time()
    np.arange(number_of_times) * number_to_calculate
    end = time.time()
    return end - start

def calcualte_me_something(number1, number2):
    return number1 * number2

if __name__ == "__main__":
    main()