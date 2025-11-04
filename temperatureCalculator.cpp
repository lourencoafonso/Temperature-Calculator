#include <iostream>
#include <string>
#include <stdexcept>
#include <chrono>
#include <thread>
#include <cmath>

#define RESET   "\033[0m"
#define RED     "\033[31m"
#define YELLOW  "\033[33m"

using namespace std;

void printMenu() {
    cout << "\nOur provided operations are: "
        "\n 1. Celsius to Fahrenheit "
        "\n 2. Fahrenheit to Celsius "
        "\n 3. Celsius to Kelvin "
        "\n 4. Kelvin to Celsius "
        "\n 5. Fahrenheit to Kelvin "
        "\n 6. Kelvin to Fahrenheit "
        "\n 7. Exit\n" ;
}

float celsiusToFahrenheit(float temp){return ((temp * 9/5) + 32);}

float fahrenheitToCelsius(float temp){return ((temp - 32) * 5/9);}

int main(){
    cout << "Welcome to the Temperature Calculator";
    printMenu();

    string userOption;
    cout << "\nWhich calculation would you like to do? "; cin >> userOption;

    bool endLoop = false;

    while (!endLoop) {
        int option;

        try {
            option = stoi(userOption); // convert string to int
            if ((option < 1) || (option > 7)) {
                throw out_of_range("Number is out of range.");
            }
        }
        catch (invalid_argument&) {
            cout << RED << "\nInvalid Input. Please enter a whole number (1-7)." << RESET << endl;

            this_thread::sleep_for(chrono::seconds(2));

            printMenu();

            cout << "\nWhich calculation would you like to do? "; cin >> userOption;

            continue;
            // You can handle re-prompting the user here if needed
        }
        catch (out_of_range&) {
            cout << YELLOW << "\nNumber is out of range. Please enter a valid option (1-7)." << RESET << endl;

            this_thread::sleep_for(chrono::seconds(2));

            printMenu();

            cout << "\nWhich calculation would you like to do? "; cin >> userOption;

            continue;
        }

        if (option == 7){
            endLoop = true;
            cout << "Thank you for using Temperature Calculator";
            continue;
        }

        bool end = false;
        float temp;

        while (!end) {
            string stringTemp;
            cout << "Please input your original temperature: ";
            cin >> stringTemp;
            try {
                temp = stof(stringTemp);
                end = true;
            } catch(invalid_argument&) {
                cout << RED << "\nInvalid Temperature. Please try again.\n" << RESET;
            }
        }

        string unit;

        if (option == 1) {
            unit = "Fahrenheit";
            temp = celsiusToFahrenheit(temp);
        } else if (option == 2) {
            unit = "Celsius";
            temp = fahrenheitToCelsius(temp);
        } else if (option == 3) {
            unit = "Kelvin";
            temp += 273.15;
        } else if (option == 4) {
            unit = "Celsius";
            temp -= 273.15;
        } else if (option == 5) {
            unit = "Kelvin";
            temp = fahrenheitToCelsius(temp) + 273.15;
        } else {
            unit = "Fahrenheit";
            temp = celsiusToFahrenheit(temp - 273.15);
        }

        double result;

        if (temp == static_cast<int>(temp)) {
            // value has no decimal portion (ex: 36.0 → 36)
            result = static_cast<int>(temp);
        } else {
            // round to 4 decimal places
            result = round(temp * 10000.0) / 10000.0;
        }

        cout << "Your temperature is " << result << " degrees " << unit << "\n";

        this_thread::sleep_for(chrono::milliseconds(1500));

        printMenu();

        cout << "\nWhich calculation would you like to do? "; cin >> userOption;

    }

    return 0;
}