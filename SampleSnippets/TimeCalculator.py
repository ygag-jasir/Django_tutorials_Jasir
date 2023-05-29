# method to calculate total time spend with checkin and checkout time



from datetime import datetime, timedelta


time_array = [
    # {
    #     "checkin": "2019-08-24T09:50:22Z",
    #     "checkout": "2019-08-24T10:21:22Z",
    # },
    # {
    #     "checkin": "2019-08-24T10:35:22Z",
    #     "checkout": "2019-08-24T12:46:22Z",
    # },
    # {
    #     "checkin": "2019-08-24T13:23:22Z",
    #     "checkout": "2019-08-24T18:50:22Z",
    # }
    
    {
        "checkin": "2019-08-24T09:00:22Z",
        "checkout": "2019-08-24T15:00:22Z",
    },
    # {
    #     "checkin": "2019-08-24T15:30:22Z",
    #     "checkout": "2019-08-24T16:30:22Z",
    # },
    
]

def calculate_total_time(time_array):
    total_time = 0
    for time in time_array:
        checkin = datetime.strptime(time["checkin"], "%Y-%m-%dT%H:%M:%SZ")
        checkout = datetime.strptime(time["checkout"], "%Y-%m-%dT%H:%M:%SZ")
        total_time += (checkout - checkin).total_seconds()
        
    # convert total time to hours
    total_time = total_time/3600
    print("total_time : ",total_time)
    
    return total_time

total_time = calculate_total_time(time_array)

# hours to spend is 8h
hours_to_spend = 8


# print the time when you can leave
# leave_time = (datetime.strptime(
#     time_array[0]["checkin"], "%Y-%m-%dT%H:%M:%SZ") + 
#               timedelta(hours=hours_to_spend))

# print("leave_time : ",leave_time)


remaining_time = hours_to_spend - total_time

# leaving time after adding remaining time with current time 
leave_time = datetime.now() + timedelta(hours=remaining_time)

print("leave_time : ",leave_time)