package main

import (
	"fmt"
	"time"
)

func main() {
    //value_of_string := get_me_string()
	//value_of_calcualtions := calculate_me_something(1, 2)
	//fmt.Println(value_of_calcualtions, value_of_string)

	avg_time := run_multiple_times(10)
	fmt.Println("Average time:", avg_time)
}

func run_multiple_times(number_of_times int) float64 {
	// Define array for calculations avg time of function
	var time_slice []float64
	for i := 0; i < number_of_times; i++ {
		start := time.Now()
		run_me_loop_and_time_it(10000000, 50)
		time_elapsed := timeTack(start, "run_me_loop_and_time_it")
		time_slice = append(time_slice, time_elapsed)
	}
	// Calculate average time
	var sum float64
	for _, val := range time_slice {
        sum += val
    }
    avg_time := sum / float64(number_of_times)
    return avg_time
}


func timeTack(start time.Time, functionName string) float64 {
	elapsed := time.Since(start)
	return elapsed.Seconds()
}

func get_me_string() string {
	return "Hello, World!"
}

func calculate_me_something(number1 int, number2 int) int {
	return number1 * number2
}

func run_me_loop_and_time_it(number_of_times int, number_to_calcualte int) int {
	//fmt.Println("I am running")
	for i := 0; i < number_of_times; i++ {
		calculate_me_something(i, number_to_calcualte)
		//temp_value := calculate_me_something(i, number_to_calcualte)
		//fmt.Println(temp_value)
	}
	return 1
}