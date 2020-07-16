"""
============================================================================
    Author : Mouli Bheemaneti
    Last Updated : 16 July 2020
    Description: This program converts your JSON text or JSON file into
                 your desired language in JSON file format.
----------------------------------------------------------------------------
    PROFILE SECTION
    ---------------
    Github Profile: https://www.github.com/moulibheemaneti
    LinkedIn Profile: https://www.linkedin.com/in/moulibheemaneti
    Google Site: https://sites.google.com/view/moulibheemaneti
============================================================================
"""

from googletrans import Translator
import json
import httpcore


def welcome_text():
    print("=====================================================")
    print("Welcome to MB json text Translator".upper().center(50))
    print("=====================================================")


def section_break():
    print("-----------------------------------------------------")


def translate_file(filename, dest_lang):
    output_dict = {}
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)

    for key, value in data.items():
        result = translate.translate(data[key], dest=dest_lang)
        translated_value = result.text
        output_dict.update({key: translated_value})

    return output_dict


def translate_text(input_dict, dest_lang):
    output_dict = {}
    data = json.loads(input_dict)

    for key, value in data.items():
        result = translate.translate(data[key], dest=dest_lang)
        translated_value = result.text
        output_dict.update({key: translated_value})

    print(output_dict)

    return output_dict


if __name__ == "__main__":
    translate = Translator()

    welcome_text()

    # noinspection PyProtectedMember
    try:
        lang_code = input("Enter output language code : ")
        section_break()

        n = int(input("1) Enter filename \n2) paste json code \nChoose your option to convert : "))
        section_break()

        if n == 1:
            file_name = input("Enter input filename(.json) : ")
            data = translate_file(file_name, lang_code)

        else:
            user_dict = input("Paste your json code : \n")
            data = translate_text(user_dict, lang_code)

        with open(lang_code + ".json", "w", encoding="utf-8") as handle:
            handle.write(json.dumps(data, ensure_ascii=False, indent=4))

    # Exception Handling
    except json.decoder.JSONDecodeError:
        print("\nOOPS...!!! Your input text is not in JSON format. Please check and try again")

    except httpcore._exceptions.ConnectError:
        print("\nOOPS...!!! Please ensure your internet connection and try again")

    except httpcore._exceptions.TimeoutException:
        print("\nOOPS...!!! Your internet connection is Timed Out")
