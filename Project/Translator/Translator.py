import json

def language_codes_display(lang_codes):
    print("\nLanguage Codes:")
    print('=' * 20)
    for k, v in lang_codes.items():
        print(f"{k}: {v}")
    print('=' * 20)


def read_from_dictionary(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


def add_word_to_dictionary(filename, dictionary, lang_codes):
    temp_dict = {}
    for code, lang in lang_codes.items():
        word = input(f"Please enter the new word in {lang} language: ").strip()
        temp_dict[lang] = word

    dictionary.append(temp_dict)

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(dictionary, file, indent=2, ensure_ascii=False)

    print("Word added successfully!\n")


def translate():
    filename = 'dictionary.json'

    lang_codes = {'ge': 'georgian', 'en': 'english', 'ru': 'russian'}
    language_codes_display(lang_codes)

    # language selection
    from_language = to_language = ""
    while from_language not in lang_codes or to_language not in lang_codes:
        from_language = input("\nFrom language ('ge', 'en', 'ru'): ").lower()
        to_language = input("To language ('ge', 'en', 'ru'): ").lower()

    # Load dictionary
    dictionary = read_from_dictionary(filename)

    # User enters a word
    word = input(f"Enter a {lang_codes[from_language]} word to translate: ").strip()

    # Auto-detect the actual language of the word (დაზღვევა იმის რომ მომხმარებელმა აირჩიოს მაგალითად ინგლისური (en)
    # და შეიყვანოს სიტყვა ქართულად
    detected_language = None
    for entry in dictionary:
        for lang_name in lang_codes.values():
            if entry[lang_name].lower() == word.lower():
                detected_language = lang_name
                break
        if detected_language:
            break

    # If word found but from a different language (თუ სიტყვა სხვა ენაზე იპოვნა ლექსიკონში)
    if detected_language and detected_language != lang_codes[from_language]:
        print(f"\n You selected '{lang_codes[from_language]}' but the word is actually {detected_language}.")
        from_language = [k for k, v in lang_codes.items() if v == detected_language][0]
        print(f"Auto-switching to from-language = '{from_language}' ({detected_language}).")

    # Build list of words from chosen source language
    word_list = [entry[lang_codes[from_language]].lower() for entry in dictionary]

    # Word not found. Ask to add
    if word.lower() not in word_list:
        add_word = ''
        while add_word not in ['yes', 'no']:
            add_word = input("Word not found. Add it? ('yes'/'no'): ").lower()

        if add_word == 'yes':
            add_word_to_dictionary(filename, dictionary, lang_codes)
        return

    # Word found. Translate
    for entry in dictionary:
        if entry[lang_codes[from_language]].lower() == word.lower():
            translated = entry[lang_codes[to_language]]
            print(f"\n{word} → {translated}\n")
            break



# Main Program

check_for_another_game = True
while check_for_another_game:
    translate()

    again = ""
    while again not in ['yes', 'no']:
        again = input("Translate another word? ('yes'/'no'): ").lower()

    if again == 'no':
        check_for_another_game = False
