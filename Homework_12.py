

import os, json

# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, ფაილის სახელს და შემქნის მას.
# def func1(filename, chess_players):
#   os.makedirs(path, exist_ok=True)
#   with open(filename, 'w') as f:
#     json.dump(chess_players, f, indent=2)

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.
def func2(filename):
  with open(filename, 'r') as f:
    json_file = json.load(f)
  return json_file

# 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და დაამატებს ფაილის კონტენტს.
def func3(filename, data):
  # file_content = func2(filename)


  with open(filename, 'r+') as f:
      f.seek(0, 2)
      # f.seek(f.tell() - 1, 0)
      file_pos = f.tell()
      f.seek(file_pos - 2)
      last_char = f.read(2)
      print(last_char)
      f.seek(file_pos - 3)
      for i in data:
        json_string = json.dumps(i, indent=2)
        f.write(',\n  ' + json_string)
      f.write(last_char)




# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.




#-----------------MAIN--------------------

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

data = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

path = "files"
filename = "chess_players.json"
filename = os.path.join(path, filename)


# func1(filename, chess_players)

# json_file = func2(filename)
# for line in json_file:
#   print(line)

func3(filename, data)

