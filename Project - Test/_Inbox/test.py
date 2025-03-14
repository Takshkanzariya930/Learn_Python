return_flight=200
hotel_per_day=20
weekly_car_rental=50
no_of_days=12

print(return_flight + (hotel_per_day*no_of_days) + (weekly_car_rental*(1 + int(no_of_days/7))))