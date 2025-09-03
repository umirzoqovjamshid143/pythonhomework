## Homework

1. Task: JSON Parsing
    - write a Python script that reads the students.jon JSON file and prints details of each student.

import json

# students.json faylini ochamiz va o'qiymiz
with open('students.json', 'r', encoding='utf-8') as fayl:
    talabalar = json.load(fayl)

# Har bir talaba haqida ma'lumot chiqaramiz
for talaba in talabalar:
    ism = talaba.get('ism', 'Noma\'lum')
    yosh = talaba.get('yosh', 'Noma\'lum')
    mutaxassislik = talaba.get('mutaxassislik', 'Noma\'lum')

    print(f"Ismi: {ism}, Yoshi: {yosh}, Mutaxassisligi: {mutaxassislik}")


2. Task: Weather API
   1. Use this url : https://openweathermap.org/
   2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

def get_weather(city):
    try:
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=uz"
        response = requests.get(URL)
        data = response.json()

        if data.get("cod") != 200:
            print("Xatolik:", data.get("message"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"\n{city} shahrining hozirgi ob-havosi:")
        print(f"Harorat: {temp}°C")
        print(f"Namlik: {humidity}%")
        print(f"Bosim: {pressure} hPa")
        print(f"Havo holati: {weather_desc.capitalize()}")
        print(f"Shamol tezligi: {wind_speed} m/s")

    except Exception as e:
        print("Xatolik yuz berdi:", e)



3. Task: JSON Modification
   1. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json

FILENAME = 'books.json'

def load_books():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book():
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1

    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Nashr yili: ")

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(new_book)
    save_books(books)
    print("Kitob qo'shildi!")

def update_book():
    books = load_books()
    book_id = int(input("Yangilamoqchi bo'lgan kitob ID sini kiriting: "))

    for book in books:
        if book['id'] == book_id:
            print(f"Hozirgi nomi: {book['title']}")
            book['title'] = input("Yangi nom (bo'sh qoldirsangiz o'zgarmaydi): ") or book['title']

            print(f"Hozirgi muallifi: {book['author']}")
            book['author'] = input("Yangi muallif (bo'sh qoldirsangiz o'zgarmaydi): ") or book['author']

            print(f"Hozirgi nashr yili: {book['year']}")
            book['year'] = input("Yangi yil (bo'sh qoldirsangiz o'zgarmaydi): ") or book['year']

            save_books(books)
            print("Kitob yangilandi!")
            return

    print("Kitob topilmadi!")

def delete_book():
    books = load_books()
    book_id = int(input("O'chirmoqchi bo'lgan kitob ID sini kiriting: "))

    new_books = [book for book in books if book['id'] != book_id]

    if len(new_books) == len(books):
        print("Kitob topilmadi!")
    else:
        save_books(new_books)
        print("Kitob o'chirildi!")

def main():
    while True:
        print("\n1. Kitob qo'shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o'chirish")
        print("4. Chiqish")
        tanlov = input("Tanlovingiz: ")

        if tanlov == '1':
            add_book()
        elif tanlov == '2':
            update_book()
        elif tanlov == '3':
            delete_book()
        elif tanlov == '4':
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()



4. Task: Movie Recommendation System
   1. Use this url http://www.omdbapi.com/ to fetch information about movies.
   2. Create a program that asks users for a movie genre and recommends a random movie from that genre.
    
import requests
import random

API_KEY = "YOUR_API_KEY"  # O'zingizning API kalitingizni shu yerga qo'ying

def get_movies_by_keyword(keyword):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={keyword}"
    response = requests.get(url)
    data = response.json()

    if data.get('Response') == 'True':
        return data.get('Search', [])
    else:
        return []

def main():
    genre = input("Qaysi janrdan film tavsiya qilishimni xohlaysiz? (masalan: Action, Comedy, Drama): ").strip()

    print(f"\n'{genre}' janriga mos keladigan filmlar qidirilmoqda...")

    # Janr bo'yicha emas, lekin foydalanuvchi kiritgan so'z bo'yicha qidiramiz
    movies = get_movies_by_keyword(genre)

    if not movies:
        print(f"Janr '{genre}' bo'yicha film topilmadi yoki API cheklovlari mavjud.")
        return

    # Tasodifiy film tanlaymiz
    movie = random.choice(movies)

    # Qo'shimcha: Film haqida to'liq ma'lumot olish uchun alohida so'rov qilish mumkin
    movie_id = movie.get('imdbID')
    detail_url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}"
    detail_response = requests.get(detail_url).json()

    print("\nSizga tavsiya qiladigan film:")
    print(f"Nomi: {detail_response.get('Title')}")
    print(f"Yili: {detail_response.get('Year')}")
    print(f"Janri: {detail_response.get('Genre')}")
    print(f"Rejissyor: {detail_response.get('Director')}")
    print(f"IMDb reytingi: {detail_response.get('imdbRating')}")
    print(f"Poster: {detail_response.get('Poster')}")

if __name__ == "__main__":
    main()
