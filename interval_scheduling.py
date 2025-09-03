def interval_scheduling():
    number_of_intervals = input()
    intervals = []
    for i in range(int(number_of_intervals)):
        s, f = map(int, input().split())
        intervals.append((s, f))

    sorted_intervals = sorted(
        intervals, 
        key=lambda x: x[1]
    )
    optimal_schedule = []
    end_time_value = 0
    for interval in sorted_intervals:
        if interval[0] >= end_time_value:
            end_time_value = interval[1]
            optimal_schedule.append(interval)
        
    print(len(optimal_schedule))

interval_scheduling()