#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import traceback

"""
Propedeuse Semester
Opdracht SD1: Weerstation 
(c) 2025 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen en 
de functie weerstation voldoet aan de opdrachteisen.
"""


def fahrenheit(temp_celsius):
    """
    Deze functie berekent de temperatuur in fahrenheit, aan de hand
    van de gegeven temperatuur in Celsius. De formule hiervoor is:

        T(F) = T(C) × 1.8 + 32

    Args:
        temp_celcius (float): De temperatuur in graden Celsius
    Returns:
        float: de berekende temperatuur in graden Fahrenheit
    """
    return


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    """
    De gevoelstemperatuur wordt berekend aan de hand van de daadwerkelijke
    temperatuur (temp_celcius), de windsnelheid en de luchtvochtigheid. De
    formule hiervoor is:

        gevoelstemperatuur = T(C) - luchtvochtigheid / 100 * windsnelheid

    Args:
        temp_celcius (float): De temperatuur in graden Celsius
        windsnelheid (float): De windsnelheid in meter per seconde
        luchtvochtigheid (int): luchtvochtigheidspercentage als waarde van 0..100
    Returns:
        float: de gevoelstemperatuur in graden Celcius
    """
    return


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    """
    Het weerrapport wordt opgesteld aan de hand van de gegeven temperatuur,
    windsnelheid en luchtvochtigheid. De gevoelstemperatuur wordt berekend
    met behulp van de functie 'gevoelstemperatuur(..)'.

    Het rapport kent zes varianten:

        * Als de gevoelstemperatuur onder nul is en de windsnelheid is groter dan 10:
            'Het is heel koud en het stormt! Verwarming helemaal aan!'

        * Als de gevoelstemperatuur onder nul is en de windsnelheid is 10 of lager:
            'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!'

        * Als de gevoelstemperatuur tussen 0 (inclusief) en 10 (exclusief) is, en de windsnelheid groter dan 12:
            'Het is best koud en het waait; verwarming aan en roosters dicht!'

        * Als de gevoelstemperatuur tussen 0 (inclusief) en 10 (exclusief) is, en de windsnelheid 12 of lager:
            'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!'

        * Als de gevoelstemperatuur tussen 10 (inclusief) en 22 (exclusief) is:
            'Heerlijk weer, niet te koud of te warm.'

        * In andere gevallen: 'Warm! Airco aan!'

    Args:
        temp_celcius (float): De temperatuur in graden Celsius
        windsnelheid (float): De windsnelheid in meter per seconde
        luchtvochtigheid (int): luchtvochtigheidspercentage als waarde van 0..100
    Returns:
        str: het opgestelde rapport
    """
    return


def weerstation():
    """
    Het weerstation vraagt de gebruiker de weersinformatie voor 7 dagen in
    te voeren. Per dag worden temperatuur (in Celsius), windsnelheid (in meter
    per seconde) en luchtvochtigheid (als geheel percentage van 0..100) gevraagd.

    Het weerstation print (direct) per ingevoerde dag de temperatuur in Celcius
    en Fahrenheit, het weerrapport (gebruik de gelijknamige functie) en de
    gemiddelde temperatuur van de tot dan toe ingevoerde dagen. Voorbeeld:

        Het is 15.0C (59.0F)
        Heerlijk weer, niet te koud of te warm.
        Gem. temp tot nu toe is 15.0

    Zodra de gebruiker een lege string invoert, stopt het programma direct.
    """
    return


def development_code():
    # De aanroep naar jouw SmartApp weerstation:
    weerstation()


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


def test_fahrenheit():
    function = fahrenheit

    case = collections.namedtuple('case', 'celcius fahrenheit')
    testcases = [case(25, 77.0), case(100, 212.0), case(-40, -40.0), case(-100, -148.0),
                 case(-273.15, -459.67), case(1, 33.8), case(-1, 30.2), case(1000, 1832.0)]

    for test in testcases:
        __my_assert_args(function, (test.celcius,), test.fahrenheit, check_type=True)


def test_gevoelstemperatuur():
    function = gevoelstemperatuur

    case = collections.namedtuple('case', 'celcius windsnelheid vochtigheid gevoel')
    testcases = [
        case(25, 10, 50, 20.0), case(0, 0, 0, 0.0), case(15, 5, 40, 13.0), case(0, 10, 100, -10.0),
        case(30, 0, 50, 30.0), case(-10, 10, 50, -15.0), case(50, 20, 0, 50.0), case(10, 10, 100, 0.0),
        case(-273.15, 0, 0, -273.15), case(100, 50, 100, 50.0), case(0, 20, 100, -20.0), case(10, 5, 100, 5.0),
    ]

    for test in testcases:
        __my_assert_args(function, (test.celcius, test.windsnelheid, test.vochtigheid), test.gevoel, check_type=True)


def test_weerrapport():
    function = weerrapport

    case = collections.namedtuple('case', 'celcius windsnelheid vochtigheid, rapport')
    testcases = [
        # Als de gevoelstemperatuur onder nul is en de windsnelheid is groter dan 10:
        case(1, 10.1, 10, 'Het is heel koud en het stormt! Verwarming helemaal aan!'),  # -0.01 gt
        # Als de gevoelstemperatuur onder nul is en de windsnelheid is 10 of lager:
        case(0, 10, 10, 'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!'),  # -1.0 gt
        # Als de gevoelstemperatuur tussen 0 (inclusief) en 10 (exclusief) is, en de windsnelheid groter dan 12:
        case(3, 20, 15, 'Het is best koud en het waait; verwarming aan en roosters dicht!'),  # 0.0 gt
        case(13, 21, 15, 'Het is best koud en het waait; verwarming aan en roosters dicht!'),  # 9.85 gt
        case(13, 12.1, 25, 'Het is best koud en het waait; verwarming aan en roosters dicht!'),  # 9.975 gt
        # Als de gevoelstemperatuur tussen 0 (inclusief) en 10 (exclusief) is, en de windsnelheid 12 of lager:
        case(1, 10, 10, 'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!'),  # 0.0 gt
        case(11, 10, 11, 'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!'),  # 9.9 gt
        # Als de gevoelstemperatuur tussen 10 (inclusief) en 22 (exclusief) is:
        case(10, 0, 0, 'Heerlijk weer, niet te koud of te warm.'),  # 10.0 gt
        case(21.9, 0, 0, 'Heerlijk weer, niet te koud of te warm.'),  # 21.9 gt
        case(23, 30, 5, 'Heerlijk weer, niet te koud of te warm.'),  # 21.5 gt
        # In andere gevallen:
        case(30, 32, 25, 'Warm! Airco aan!'),  # 22.0 gt
        case(22, 0, 0, 'Warm! Airco aan!'),  # 22.0
    ]

    for test in testcases:
        __my_assert_args(function, (test.celcius, test.windsnelheid, test.vochtigheid), test.rapport, check_type=True)


def __run_tests():
    """ Test alle functies. """
    test_functions = [test_fahrenheit, test_gevoelstemperatuur, test_weerrapport]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd! Drie functies zijn getest, en lijken te werken!")
        print("Let op: de functie weerstation werd niet getest, controleer goed of deze voldoet aan de opdrachteisen!")
        print("Ben je daarmee klaar? Lever dan je werk in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()
