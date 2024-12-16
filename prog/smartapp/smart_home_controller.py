#Nodig voor testraamwerk
import builtins
import collections
import sys
import traceback

##############################################################
#           PROJECT SMART APP
#           SPRINT 2: Smart Home Controller
#
##############################################################

# In dit tweede opdracht zal je een applicatie ontwikkelen waarbij je een txt  file leest met
# allerlei informatie per dag over de temperatuur, vochtigheid, neerslag (in mm), setpoint thermostaat, aantal mensen thuis

# Maak een menuutje met
# 1. Welke dagen zijn er? (welke dagen+ hoeveel in totaal)
# 2. Autobereken alles actuatotoren, schrijven naar een json
# 3. Overschrijf een berekende waarde
# 4. exit

# aande hand van deze data zullen de volgende smart home systemen aangestuurd moeten worden
# - cv ketel/warmtepompp (100% aan bij temp. verschil > 20, 0% aan bij verschil <= 0, evenredig ertussen)
# - ventilatie
# - bewatering van planten
# - wasmachine (afh. van zonneopwek)

# Geef ook een mogelijkheid om de automatisch berekende aansturingen van de smart home systemen manueel overschreven kunen worden door de gebruiker.
# Dit kan door bijv. de gebruiker eerst een datum (bijv. 08-10-2024) en daarna te laten selecteren, daarna een van de systemen, en als laatst de waarmee waarmee te overschrijven.
# SMART HOME XL TIP: Gebruik van GUI om dit makkelijker te maken

# Het input txt bestand ziet er als volgt uit:


'''
date numPeople tempSetpoint tempOutside precip
05-10-2024 2 19 8 7
06-10-2024 2 19 8 7
07-10-2024 1 19 9 3
08-10-2024 1 19 11 0
09-10-2024 1 19 10 3
10-10-2024 3 21 6 0
11-10-2024 3 21 4 0
'''

#Voorbeeld van output txt:

'''
05-10-2024;50;3;False
06-10-2024;50;3;False
07-10-2024;0;2;False
08-10-2024;0;2;True
09-10-2024;0;2;False
10-10-2024;50;4;True
11-10-2024;50;4;True
'''

################## UITWERKING


def aantal_dagen(inputFile):
  # Zie canvas voor opdracht
    pass
   

def auto_bereken(inputFile, outputFile):
  # Zie canvas voor opdracht
    pass


def overwrite_settings(inputFile, outputFile):
  # Zie canvas voor opdracht
    pass


def smart_home_controller():
  # Zie canvas voor opdracht
  pass

def development_code():
    smart_home_controller()

def module_runner():
    development_code()  # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()       # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def __out_of_input_error():
    raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")


def __my_test_file_input():
    return "smart_home_input_test.txt"

def __my_test_file_output():
    return "smart_home_output_test.txt"

def __check_line_in_testfile(line, testfile=__my_test_file_input()):
    with open(testfile, 'r') as dummy_file:
        for file_line in dummy_file.readlines():
            if line.strip() == file_line.strip():
                return True

    return False


def __create_test_file(input_lines, testfile=__my_test_file_input()):
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(input_lines)} regels... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            print(input_lines)
            for date, numPeople, tempSetpoint, tempOutside, precip in input_lines:
                dummy_file.write(f"{date} {numPeople} {tempSetpoint} {tempOutside} {precip}\n")
    except:
        print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("Klaar.")


def __create_fake_open(original_open):
    def fake_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        return original_open(__my_test_file_input(), mode=mode, buffering=buffering, encoding=encoding, errors=errors,
                             newline=newline, closefd=closefd, opener=opener)
    return fake_open


def test_aantal_dagen():
    function = aantal_dagen

    case = collections.namedtuple('case', 'input_lines expected')
    testcases = [
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', '0', '21', '-10', '0.0')), 1),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'),), 0),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', '0', '21', '-10', '0.0'), ('11-10-2024', '0', '20', '5', '0.0')), 2),

    ]

    for test in testcases:
        __create_test_file(test.input_lines)

        try:
            actual_num_lines = function(__my_test_file_input())
            expected_output = test.expected
            assert expected_output == actual_num_lines, f'Expected {expected_output} lines, but got {actual_num_lines}'
        finally:
            pass

def test_autobereken():
    function = auto_bereken

    case = collections.namedtuple('case', 'input_lines expected_output_in_file')
    testcases = [
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)), '10-10-2024;100;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 17, 0.0)), '10-10-2024;0;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0), ('11-10-2024', 0, 21, 6, 10.0)), '10-10-2024;100;1;True\n11-10-2024;50;1;False\n')
    ]

    for test in testcases:
        __create_test_file(test.input_lines)

        try:
            function(__my_test_file_input(),__my_test_file_output())
            with open(__my_test_file_output()) as output_test_file:
                all_lines_output = ''.join(output_test_file.readlines())
                assert all_lines_output == test.expected_output_in_file, 'Verwachte uitvoer van auto_bereken klopt niet'
        finally:
            pass

def test_overwrite_settings():
    function = overwrite_settings
    case = collections.namedtuple('case', 'input_lines simulated_input expected_return_code expected_output_in_file')

    testcases = [
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)),
             ["10-10-2024", "1", "66"], 0, '10-10-2024;66.0;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)),
             ["9-10-2024", "1", "66"], -1, ''),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)),
             ["10-10-2024", "42", "66"], -3, '')
    ]

    for test in testcases:
        __create_test_file(test.input_lines)

        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()

        try:
            output = function(__my_test_file_input(),__my_test_file_output())

            assert isinstance(output, int), f"Fout: {function.__name__}() geeft {type(output).__name__} in plaats van int. Check evt. {__my_test_file_input()}"
            assert output == test.expected_return_code, f"Fout: {function.__name__}() geeft {output}, maar mogelijke outputs is: {test.expected_return_code}"


        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
        finally:
            builtins.input = original_input

def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_aantal_dagen,
                       test_autobereken,
                       test_overwrite_settings
                     ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()
