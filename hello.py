import time
import numpy as np

def print_progress_bar(iteration, total, length=100, fill="▓", barfill="░", decimals=1):
    """
    Print progress bar.

    Parameters:
    - iteration (int): Current iteration (counter_temp_for_testing).
    - total (int): Total iterations (length of answer_dict).
    - length (int): Character length of the bar (default 100).
    - fill (str): Bar fill character (default "▓").
    - barfill (str): Bar background fill character (default "░").
    - decimals (int): Precision of percentage (default 2).
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + barfill * (length - filledLength)
    print(f'\r {bar} {percent}%', end='\r')
    if iteration == total:
        print()

def main():
    avg_time = run_multiple_times(2)
    avg_time_with_printing = run_multiple_times_with_printing(2)
    avg_time_numpy = run_multiple_times_numpy(10)
    time_for_go = 0.003264804569999999
    print(f"Python without printing is {avg_time_with_printing / avg_time } times faster than python with printing")
    print(f"GO is {avg_time / time_for_go } times faster than python - without numpy")
    print(f"GO is {avg_time_numpy / time_for_go } times faster than python - with numpy")

def run_multiple_times(number_of_times):
    time_array = []

    for i in range(number_of_times):
        time_array.append(run_me_loop_and_time_it(10000000, 50))
    return sum(time_array) / len(time_array)

def run_multiple_times_with_printing(number_of_times):
    time_array = []

    for i in range(number_of_times):
        time_array.append(run_me_loop_and_time_it_with_printing(10000000, 50))
    return sum(time_array) / len(time_array)

def run_multiple_times_numpy(number_of_times):
    time_array = []
    for i in range(number_of_times):
        time_array.append(run_me_loop_and_time_it_numpy(10000000, 50))
    return sum(time_array) / len(time_array)


def run_me_loop_and_time_it_with_printing(number_of_times, number_to_calculate):
    start = time.time()
    for i in range(number_of_times):
        print_progress_bar(i, number_of_times)
        calcualte_me_something(i, number_to_calculate)
    end = time.time()
    return end - start

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