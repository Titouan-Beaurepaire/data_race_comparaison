#!/usr/bin/env python3

def main():
    print("Start...")

def read_files():
    with open('data/data_lec.csv', 'r') as file:
        next(file) # Skip the first line
        data = file.readlines()
    return data

def get_laptime(data):
    for line in data:
        columns = line.strip().split(',')
        if len(columns) > 1:
            print(columns[1])

if __name__ == "__main__":
    main()
    data = read_files()
    get_laptime(data)
