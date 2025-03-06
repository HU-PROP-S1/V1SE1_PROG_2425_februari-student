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
de functie smart app controller voldoet aan de opdrachteisen.
"""


def aantal_dagen(inputFile):
    # Zie canvas voor opdracht
    return 0


def auto_bereken(inputFile, outputFile):
    # Zie canvas voor opdracht
    # Deze functie leest van een inputFile, en schrijft naar een outputFile. Er is verder geen return waarde.
    return


def overwrite_settings(outputFile):
    # Zie canvas voor opdracht
    # Deze functie schrijft naar een outputFile. Zie Canvas voor de mogelijke return waardes.
    return


def smart_app_controller():
    # Hier komt het menuutje. Zie canvas voor opdracht
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
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0)), '10-10-2024;100;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, 17, 0.0)), '10-10-2024;0;1;True\n'),
        case((('date', 'numPeople', 'tempSetpoint', 'tempOutside', 'precip'), ('10-10-2024', 0, 21, -10, 0.0), ('11-10-2024', 0, 21, 6, 10.0)), '10-10-2024;100;1;True\n11-10-2024;50;1;False\n')
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
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "1", "66"], 0, ['10-10-2024;66.0;1;True\n', '10-10-2024;66;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["09-10-2024", "1", "66"], -1, ['10-10-2024;100;1;True\n']),
        case((('10-10-2024', 100, 1, True),), ["10-10-2024", "42", "66"], -3, ['10-10-2024;100;1;True\n'])
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
