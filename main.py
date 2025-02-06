#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    print("Start...")

def read_files():
    with open('data/data_lec.csv', 'r') as file:
        next(file) # Skip the first line
        data = file.readlines()
    return data

def get_lap(data):
    last_value = None
    for line in data:
        columns = line.strip().split(',')
        if len(columns) > 1:
            last_value = columns[0]
    if last_value:
        print(last_value)
    return last_value

def get_laptime(data):
    for line in data:
        columns = line.strip().split(',')
        if len(columns) > 1:
            print(columns[1])

def convert_to_seconds(time_str):
    minutes, seconds = time_str.split(':')
    return int(minutes) * 60 + float(seconds)

def convert_to_time_format(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:.3f}"

def average_time(data):
    total_time = 0
    count = 0
    for line in data:
        columns = line.strip().split(',')
        if len(columns) > 1:
            try:
                lap_time = convert_to_seconds(columns[1])
                total_time += lap_time
                count += 1
            except ValueError:
                print(f"Invalid time format: {columns[1]}")
    if count > 0:
        average = total_time / count
        average_formatted = convert_to_time_format(average)
        print(f"Average lap time: {average_formatted}")
        return average
    else:
        print("No lap times found.")
        return None

def graph_laptime(data):
    laps = []
    laptimes = []
    for line in data:
        columns = line.strip().split(',')
        if len(columns) > 1:
            laps.append(columns[0])
            laptimes.append(convert_to_seconds(columns[1]))
    plt.bar(laps, laptimes)
    plt.xlabel('Lap')
    plt.ylabel('Lap Time (seconds)')
    plt.show()

if __name__ == "__main__":
    main()
    data = read_files()
    get_laptime(data)
    get_lap(data)
    average_time(data)
    graph_laptime(data)
