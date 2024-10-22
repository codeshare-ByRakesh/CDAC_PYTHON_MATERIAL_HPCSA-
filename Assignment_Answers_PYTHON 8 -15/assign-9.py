#   Assignment 1: Convert Celsius to Fahrenheit

celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(f"Fahrenheit temperatures: {fahrenheit_temps}")


#  Assignment 2: Add Two Lists Element-wise

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum of lists: {sum_lists}")



# Assignment 3: Capitalize Words in a List

words = ['apple', 'banana', 'cherry']
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(f"Capitalized words: {capitalized_words}")



#  Assignment 4: Find the Length of Strings


strings = ['hello', 'world', 'python']
lengths = list(map(lambda s: len(s), strings))
print(f"Lengths of strings: {lengths}")


#   Assignment 5: Daily Temperature Tracker


def temperature_tracker():
    temperatures = {
        'Monday': 30,
        'Tuesday': 32,
        'Wednesday': 29,
        'Thursday': 31,
        'Friday': 30,
        'Saturday': 28,
        'Sunday': 27
    }

    day = input("Enter the day to update the temperature: ")
    new_temp = float(input(f"Enter the new temperature for {day}: "))
    if day in temperatures:
        temperatures[day] = new_temp
    else:
        print(f"{day} is not a valid day.")

    avg_temp = sum(temperatures.values()) / len(temperatures)
    print(f"Average temperature: {avg_temp:.2f}°C")


    temperature_tracker()



#  Assignment 6: Bird Species Observation Tracker


def bird_tracker():
    sightings = {
        'sparrow': 10,
        'eagle': 5,
        'hawk': 7
    }

    new_species = input("Enter the new bird species: ")
    count = int(input(f"Enter the number of sightings for {new_species}: "))
    sightings[new_species] = count

    existing_species = input("Enter an existing species to update: ")
    if existing_species in sightings:
        new_count = int(input(f"Enter the new sighting count for {existing_species}: "))
        sightings[existing_species] = new_count

    top_bird = max(sightings, key=sightings.get)
    print(f"The bird with the highest sightings is '{top_bird}'.")

    bird_tracker()
