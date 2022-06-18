print("\n\nWELCOME TO YOUR UNIT CONVERTER\n")


def main():
    def units():
        unit = input(
            "choose an option please \n\n"
            "1. cm to inch \n"
            "2. inch to cm \n"
            "3. m to feet \n"
            "4. feet to m \n"
            "5. km to mile \n"
            "6. mile to km \n"
            "7. kg to pound \n"
            "8. pound to kg \n"
            "9. Celsius to Fahrenheit \n"
            "10. Fahrenheit to Celsius  \n"
            "11. Celsius to Kelvin \n"
            "12. Kelvin to Celsius \n"
            "13. Fahrenheit to Kelvin \n"
            "14. Kelvin to Fahrenheit \n\n"
            "your option: "
        )
        while unit not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"):
            print("Wrong choice, please choose again\n")
            units()

        number = float(input("enter the value you want to convert: "))

        if unit == "1":
            print(number / 2.54, "in")
        elif unit == "2":
            print(number * 2.54, "cm")
        elif unit == "3":
            print(number * 3.281, "ft")
        elif unit == "4":
            print(number / 3.281, "m")
        elif unit == "5":
            print(number / 1.609, "mile")
        elif unit == "6":
            print(number * 1.609, "km")
        elif unit == "7":
            print(number * 2.20462, "lb")
        elif unit == "8":
            print(number / 2.20462, "kg")
        elif unit == "9":
            print((number * 9 / 5) + 32, "F")
        elif unit == "10":
            print((number - 32) * 5 / 9, "C")
        elif unit == "11":
            print(number + 273.15, "K")
        elif unit == "12":
            print(number - 273.15, "C")
        elif unit == "13":
            print((number - 32) * 5 / 9 + 273.15, "K")
        elif unit == "14":
            print(((number - 273.15) * 9 / 5) + 32, "F")

        restart = input("Do you want to start again? y / n: ")
        if restart == "y":
            main()
        elif restart == "n":
            exit()
    units()
main()
