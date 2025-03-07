#Nodig voor testraamwerk
import builtins
import collections
import os
import sys
import traceback

"""
Propedeuse Semester
Opdracht SD2: Smart App Controller 
(c) 2025 Hogeschool Utrecht,
Hasan Kurt (hasan.kurt@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen en 
de functies smart_app_controller, aantal_dagen, auto_bereken en overwrite_settings voldoen aan de opdrachteisen.
"""


def aantal_dagen(input_file):
    """
    Deze functie leest  het txt bestand wat je meekrijg als argument en geeft het aantal dagen terug wat er in deze file zit.

    Args:
        input_file (string): Bestandsnaam van de input file
    Returns:
        int: Het aantal dagen wat er in de input file is
    """
    return 0


def auto_bereken(input_file, output_file):
    """
        Deze functie leest  het txt bestand wat je meekrijg als argument (input_file)
        en berekent de waardes van de actuatoren volgens de volgende regels:

    * CV ketel:
        100% aan als het temperatuur verschil tussen setpoint en buiten groter dan of gelijk is aan 20 graden Celsius
        50% aan als het temperatuur verschil tussen setpoint en buiten groter dan of gelijk is aan 10 en  kleiner is dan 20  graden Celsius is
        0% als het verschil kleiner is dan 10
    * Ventilatie:
        op stand berekend door: aantal mensen thuis +1, maar maximaal op stand 4
    * Bewatering van planten:
        wel/niet aan: planten moeten bewaterd worden als er op een dag minder dan 3 mm aan neerslag valt

    De resultaten worden dan per dag op een regel geschreven naar een file die wordt aangemaakt (output_file),
    in de formaat dd-mm-yyyy;<waarde-cv>;<waarde-ventilatie>;<waarde-bewatering>.
    Bijvoorbeeld: 11-12-2024;100;1;True

        Args:
            input_file (string): Bestandsnaam van de input file
            output_file (string): Bestandsnaam van de output file
        Returns:
            None: De functie heeft geen return waarde
        """
    return


def overwrite_settings(outputFile):
    '''
    Automatisch berekende waardes kunnen overschreven worden door de gebruiker. Dit kan door de gebruiker eerst een datum (bijv. 08-10-2024) te laten selecteren, vervolgens een van de geldige systemen (1: CV ketel, 2: ventilatie, 3: bewatering), en als laatst de waarde waarmee het overschreven moet worden, bijv. 70, zodat de CV ketel op 70% wordt gezet). Het output file outputFile wat eerder bij auto_bereken al was aangemaakt, moet vervolgens aangepast worden.

    De functie retourneert de volgende waarden:
        0, als alles goed gaat
        -1, als het gekozen datum niet kan worden gevonden
        -3, als het gekozen systeem niet bestaat (dus, als er een andere waarde van 1, 2 of 3 wordt gegeven), of als de input voor het systeem ongeldig is. Geldige waardes voor de verschillende systemen:
            Bewatering waarde is '0' of '1' voor resp. uit en aan.  In de output file komt dit als resp. False en True.
            CV ketel waarde is een geheel getal van minimaal 0 en maximaal 100.
            Ventilatie systeem waarde is een geheel getal van minimaal 0 en maximaal 4.


    Args:
        output_file (string): Bestandsnaam van de outputfile
    Returns:
        int: De berekende return waarde
    '''
    return


def smart_app_controller():
    '''
    Binnen deze functie komt het menuutje waarin de gebruiker uitleg krijgt over het programma werkt, en wat de verschillende menu opties zijn.
    SMART APP XL TIP: Gebruik van GUI om dit makkelijker te maken
    '''
    return


def development_code():
    smart_app_controller()


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
    return "smart_app_input_test.txt"


def __my_test_file_output():
    return "smart_app_output_test.txt"


def __check_line_in_testfile(line, testfile=__my_test_file_input()):
    with open(testfile, 'r') as dummy_file:
        for file_line in dummy_file.readlines():
            if line.strip() == file_line.strip():
                return True

    return False


def __create_test_file(input_lines, item_separator, testfile=__my_test_file_input()):
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(input_lines)} regels... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            print(input_lines, end="... ")
            for line_items in input_lines:
                dummy_file.write(f'{item_separator.join(map(str, line_items))}\n')
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
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'),
              ('10-10-2024', '0', '21', '-10', '0.0'), ('11-10-2024', '0', '20', '5', '0.0')), 2),
    ]

    for test in testcases:
        __create_test_file(test.input_lines, item_separator=" ")
        __my_assert_args(function, (__my_test_file_input(),), test.expected)


def test_autobereken():
    function = auto_bereken

    case = collections.namedtuple('case', 'input_lines expected_output_in_file')
    testcases = [
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)),
             '10-10-2024;100;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 17, 0.0)),
             '10-10-2024;0;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 11, 0.0)),
             '10-10-2024;50;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 10, 0.0)),
             '10-10-2024;50;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 2, 0.0)),
             '10-10-2024;50;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 1, 0.0)),
             '10-10-2024;100;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 5, 21, 1, 0.0)),
             '10-10-2024;100;4;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 3, 21, 1, 0.0)),
             '10-10-2024;100;4;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0),
              ('11-10-2024', 0, 21, 6, 10.0)), '10-10-2024;100;1;True\n11-10-2024;50;1;False\n')
    ]

    for test in testcases:
        __create_test_file(test.input_lines, item_separator=" ")

        args = __my_test_file_input(), __my_test_file_output()
        argstr = str(args).replace(',)', ')')

        function(*args)
        assert os.path.exists(__my_test_file_output()), f'Fout: uitvoerbestand {__my_test_file_output()} ontbreekt!'

        with open(__my_test_file_output()) as output_test_file:
            all_lines_output = ''.join(output_test_file.readlines())

            msg = (f"Aanroepen van {function.__name__}{argstr} resulteert in "
                   f"'{all_lines_output.encode("unicode_escape").decode("utf-8")}'"
                   f" in '{__my_test_file_output()}', maar dat moet zijn: "
                   f"'{test.expected_output_in_file.encode("unicode_escape").decode("utf-8")}'")

            assert all_lines_output == test.expected_output_in_file, msg


def test_overwrite_settings():
    function = overwrite_settings
    case = collections.namedtuple('case', 'input_lines simulated_input expected_return_code possible_output_in_file')

    testcases = [
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "1", "66"], 0,
             ['10-10-2024;66.0;1;True\n', '10-10-2024;66;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["09-10-2024", "1", "66"], -1, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "42", "66"], -3, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "4", "66"], -3, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "2", "5"], -3, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "2", "2"], 0, ['10-10-2024;100;2;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "3", "2"], -3, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "3", "0"], 0, ['10-10-2024;100;1;False\n']),
    ]

    for test in testcases:
        __create_test_file(test.input_lines, ";", __my_test_file_output())

        original_input = builtins.input
        simulated_input = test.simulated_input.copy()
        simulated_input.reverse()
        builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()

        try:
            args = __my_test_file_output(),
            argstr = str(args).replace(',)', ')')

            __my_assert_args(function, args, test.expected_return_code)

            with open(__my_test_file_output()) as output_test_file:
                all_lines_output = ''.join(output_test_file.readlines())

                msg = (f"Aanroepen van {function.__name__}{argstr} resulteert in "
                       f"'{all_lines_output.encode("unicode_escape").decode("utf-8")}'"
                       f" in '{__my_test_file_output()}', maar toegestaan is/zijn: {test.possible_output_in_file}")

            assert all_lines_output in test.possible_output_in_file, msg

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

        print("\nGefeliciteerd, 3 van de 4 functies werken goed!")
        print("Je moet nog de smart_app_controller functie implementeren en die zelf handmatig testen")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()
