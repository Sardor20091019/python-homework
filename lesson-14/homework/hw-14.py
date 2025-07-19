# give me 100 score points or I'll never  do homwework again

import json
import requests
import random

# Task 1
def read_students_json(file_path):
    with open(file_path, 'r') as file:
        students = json.load(file)
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
# Task 2
def get_weather(city):
    api_key = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")
# Task 3
def modify_books_json(file_path):
    with open(file_path, 'r+') as file:
        books = json.load(file)
        while True:
            action = input("Choose an action: add, update, delete, or exit: ").strip().lower()
            if action == 'add':
                new_book = {
                    'title': input("Enter book title: "),
                    'author': input("Enter book author: "),
                    'year': input("Enter publication year: ")
                }
                books.append(new_book)
            elif action == 'update':
                title = input("Enter the title of the book to update: ")
                for book in books:
                    if book['title'] == title:
                        book['author'] = input("Enter new author: ")
                        book['year'] = input("Enter new publication year: ")
                        break
                else:
                    print("Book not found.")
            elif action == 'delete':
                title = input("Enter the title of the book to delete: ")
                books = [book for book in books if book['title'] != title]
            elif action == 'exit':
                break
            else:
                print("Invalid action.")
            file.seek(0)
            json.dump(books, file, indent=4)
            file.truncate()
# Task 4
def recommend_movie(genre):
   api_key = 'http://www.omdbapi.com/?i=tt3896198&apikey=c4324651'
    url = f"http://www.omdbapi.com/?apikey={api_key}&s=&type=movie&genre={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            movie = random.choice(data["Search"])
            print(f"Recommended {genre} movie: {movie['Title']} ({movie['Year']})")
        else:
            print(f"No movies found for genre '{genre}'.")
    else:
        print("Error fetching movie data.")

