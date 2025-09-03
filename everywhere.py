def everywhere(cities):
    unique_cities = [] #

    for city in cities:
        if city not in unique_cities:
            unique_cities.append(city)
    return len(unique_cities)

number_of_test_cases = input().strip()

for n in range(int(number_of_test_cases)):
    number_of_trips = input().strip()
    
    visited_cities = []

    for trip in range(int(number_of_trips)):
        visited_cities.append(input().strip())
    
    print(everywhere(visited_cities))
