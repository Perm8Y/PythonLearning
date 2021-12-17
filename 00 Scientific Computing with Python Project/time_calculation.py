def add_time(start_time: str, duration: str, *day: str):

    #screen and categorize input
    start_hr = start_time.split(":")[0]
    duration_hr = duration.split(":")[0]
    if int(start_hr) > 12:
        print("Error: maximum hr is 12")
        return

    start_min = start_time.split(":")[1][:2]
    duration_min = duration.split(":")[1][:2]
    if int(start_min) > 60 or int(duration_min
    ) > 60:
        print("Error: maximum min is 60")
        return

    start_meridiem = start_time.split()[1]
    meridiem = ["AM", "PM"]
    if start_meridiem != meridiem[0] and start_meridiem != meridiem[1]:
        print("Error: please specify AM or PM")
        return
    
    #calculate time
    final_min = (int(start_min) + int(duration_min)) % 60
    if final_min < 10:
        final_min = "0" + str(final_min)
    else:
        final_min = str(final_min)

    final_hr = start_hr
    hr_add = (int(start_min) + int(duration_min)) // 60
    if hr_add > 0:
        final_hr = (int(final_hr) + int(duration_hr) + hr_add) % 12
    else:
        final_hr = (int(final_hr) + int(duration_hr)) % 12

    final_meridium = start_meridiem
    m_add = (int(start_hr) + int(duration_hr) + hr_add) % 12
    if m_add % 2 != 0:
        if final_meridium == meridiem[0]:
            final_meridium = meridiem[1]
        else:
            final_meridium = meridiem[0]
    final_time = f"{final_hr}:{final_min} {final_meridium}"

    #day count
    d_add = int(start_hr) + int(duration_hr) + hr_add
    hr_left = 24
    if start_meridiem == meridiem[0]:
        hr_left = 24 - int(start_hr)
    else:
        hr_left = 12 - int(start_hr)
    
    hr_sum = int(duration_hr) + hr_add - hr_left
    later = ""
    if hr_sum > 1 and hr_sum < 24 :
        later = "(next day)"
    elif hr_sum >= 24:
        later = f"({(hr_sum//24)+1} days later)"
    
    #day specify
    day_list = ["monday", "tuesday", "wendesday", "thursday", "friday", "saturday", "sunday"]
    day_init = str(day[0]).lower()
    for i in range(len(day_list)):
        if day_init == day_list[i]:
            day_init_index = i

    day_add_index = (hr_sum//24)+1

    sum_day_index = day_init_index + day_add_index
    if sum_day_index < 7:
        final_day_index = sum_day_index
    elif sum_day_index >= 7:
        final_day_index = sum_day_index % 7

    print(final_time, ",", day_list[final_day_index], later)
