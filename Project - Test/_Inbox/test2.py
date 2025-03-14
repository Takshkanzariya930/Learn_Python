def Cost_of_trip(return_flight,hotel_per_day,weekly_car_rental,no_of_days):
    
    if no_of_days <= 7:
        return return_flight + (hotel_per_day*no_of_days) + (weekly_car_rental)
    else:
        return return_flight + (hotel_per_day*no_of_days) + (weekly_car_rental*(1 + int(no_of_days/7)))

Cost_for_mumbai = Cost_of_trip(return_flight=200,hotel_per_day=20,weekly_car_rental=50,no_of_days=12)

print(Cost_for_mumbai)