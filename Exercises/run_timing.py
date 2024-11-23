def run_timing():
    """
    Calculate and display the average time for 10km runs.
    """
    all_time = 0
    runs = 0

    while True:
        time = input("Enter 10km run time: ")
        
        """Checks if the input is empty (user pressed Enter).
        If true, exits the loop.
        """
        if not time:
            break

        runs += 1
        all_time += float(time)

    avg = all_time / runs
    print(f"Avg time for your {runs} runs is {avg:.2f}")


run_timing()
