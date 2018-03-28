import osa
import sys
import os

#INPUT_FILE = sys.argv[1]
#OPERATION = sys.argv[2]
#OUTPUT_FILE = sys.argv[3]

#if not os.path.exists(OUTPUT_FOLDER):
    #os.makedirs(OUTPUT_FOLDER)

    
pwd = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(pwd, 'files', 'temps.txt')
file2 = os.path.join(pwd, 'files', 'currencies.txt')
file3 = os.path.join(pwd, 'files', 'travel.txt')
OUTPUT_FILE = os.path.join(pwd, 'files', 'output.txt')

def read_temperatures_from_file(file):
    temperatures = []
    with open (file, 'r', encoding = 'utf-8') as f:
        for line in f:
            temperatures.append(tuple(line.split()))

    return temperatures


def convert_temperature(temp_list):
    temp_list_converted = []
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    temp_output_type = input('\nВведите обозначение температуры, в которую нужно перевести, из доступных: C, F, K, R, Re.\n').capitalize()    

    temps = {
    'C': 'degreeCelsius',
    'F': 'degreeFahrenheit',
    'K': 'kelvin',
    'R': 'degreeRankine',
    'Re': 'degreeReaumur'
    }

    temp_output = temps[temp_output_type]


    def convert(amount, temp_type, temp_output):
        return round(client.service.ConvertTemp(amount, temp_type, temp_output), 2)

    for value, temp_type in temp_list:
        temp_list_converted.append(convert(value, temps[temp_type], temp_output))

    return temp_list_converted


def convert_and_calculate_currencies(file):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    curr_to = 'rub' #input('\nВ какой валюте вывести результат? Пример: rub, eur, cny и т. д.\n').lower()
    list_converted = []

    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.split()
            curr_amount = line[1]
            curr_from = line[2]

            params = {
                'licence_key': '',
                'baseCurrency': curr_from,
                'toCurrency': curr_to,
                'rounding': 'true',
                'date': '',
                'type': ''
            }
            converted = client.service.RateNum(params)
            list_converted.append(converted)
           
    print(list_converted)


def convert_and_calculate_length(file):
    client = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    total_length = 0
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.replace(',', '')
            line = line.split()
            lenght = line[1]
            value_type = 'Miles'
            length_converted = client.service.ChangeLengthUnit(lenght, value_type, 'Kilometers')
            total_length += round(length_converted, 2)
            
    return total_length


def write_output(list):
    with open(OUTPUT_FILE, 'w', encoding='UTF-8') as f:
        for element in list:
            f.write(str(element) + '\n')


temp_list = read_temperatures_from_file(file)
converted_temps = convert_temperature(temp_list)
print('Средняя температура: ', round(sum(converted_temps)/len(temp_list)), 'градусов')
#print(convert_and_calculate_currencies(file2)) #Выдаёт ошибку "Non-nillable parameter rounding is not present"
print(convert_and_calculate_length(file3), 'километров')