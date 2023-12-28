import PySimpleGUI as Psg
layout = [
    [Psg.Text('Convertion'), Psg.Spin(['KM-to-MILES','KG-to-POUNDS','SEC-to-MIN'] , key='-CONVERTTYPE-')],
    [Psg.Text('Enter : '), Psg.Input(key="-USERINPUT-") , Psg.Button('Convert', key='-CONVERTBUTTON-')],
    [Psg.Text('',key='-TEXTOUTPUT-')]
]
window = Psg.Window("Converter",layout)
while True:
    event, values = window.read()
    if event == Psg.WIN_CLOSED:
        break
    if event == '-CONVERTBUTTON-':
        input_value = values['-USERINPUT-']
        if  input_value.isnumeric():

            choosed_unit = values['-CONVERTTYPE-']
            copyinput = input_value
            if choosed_unit == "KM-to-MILES":
                input_value = float(input_value)*0.621
                window['-TEXTOUTPUT-'].Update(f"The {copyinput} Kilometers are {input_value} Miles.")

            elif choosed_unit == 'KG-to-POUNDS':
                input_value = float(input_value)*2.204
                window['-TEXTOUTPUT-'].Update(f"The {copyinput} Kilograms are {input_value} Pounds.")

            elif choosed_unit == "SEC-to-MIN":
                input_value = float(input_value)*(1/60)
                window['-TEXTOUTPUT-'].Update(f"The {copyinput} Seconds are {input_value} Minutes.")
        else:
            window['-TEXTOUTPUT-'].Update("Enter a valid number")
    else:
        pass
window.close()

# A More Better Approch.
# import PySimpleGUI as Psg
#
# def convert_units(choosed_unit, input_value):
#     try:
#         input_value = float(input_value)
#         if choosed_unit == "KM-to-MILES":
#             return f"The {input_value} Kilometers are {input_value * 0.621} Miles."
#         elif choosed_unit == 'KG-to-POUNDS':
#             return f"The {input_value} Kilograms are {input_value * 2.204} Pounds."
#         elif choosed_unit == "SEC-to-MIN":
#             return f"The {input_value} Seconds are {input_value / 60} Minutes."
#     except ValueError:
#         return "Enter a valid number"
#
# layout = [
#     [Psg.Text('Conversion'), Psg.Spin(['KM-to-MILES', 'KG-to-POUNDS', 'SEC-to-MIN'], key='-CONVERTTYPE-')],
#     [Psg.Text('Enter : '), Psg.Input(key="-USERINPUT-"), Psg.Button('Convert', key='-CONVERTBUTTON-')],
#     [Psg.Text('', key='-TEXTOUTPUT-')]
# ]
#
# window = Psg.Window("Converter", layout)
#
# while True:
#     event, values = window.read()
#     if event == Psg.WIN_CLOSED:
#         break
#     if event == '-CONVERTBUTTON-':
#         input_value = values['-USERINPUT-']
#         choosed_unit = values['-CONVERTTYPE-']
#         result = convert_units(choosed_unit, input_value)
#         window['-TEXTOUTPUT-'].Update(result)
#
# window.close()
#
