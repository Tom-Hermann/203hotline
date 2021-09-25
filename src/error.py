##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-203hotline-tom.hermann
## File description:
## error
##

from sys import argv, stderr
from src.constante import EXIT_SUCCESS, EXIT_FAILURE

def usage(exit_value):
    print("USAGE\n\t./203hotline [n k | d]\n")
    print("DESCRIPTION")
    print("\tn\tn value for the computation of C(n, k)")
    print("\tk\tk value for the computation of C(n, k)")
    print("\td\taverage duration of calls (in seconds)")
    exit(exit_value)

def error_case(argc):
    if (argc == 2 and (argv[1] == "-h" or argv[1] == "--help")):
        usage(EXIT_SUCCESS)
    if (argc < 2 or argc > 3):
        usage(EXIT_FAILURE)
    try:
        int(argv[1])
    except ValueError:
        print("%s must be an number", ("n", "d")[argc == 3], file = stderr)
        exit(EXIT_FAILURE)
    if (int(argv[1]) < 0):
        print("k must be postiv", file = stderr)
        exit(EXIT_FAILURE)
    if (argc == 3):
        try:
            int(argv[2])
        except ValueError:
            print("k must be an number", file = stderr)
            exit(EXIT_FAILURE)
        if (int(argv[2]) < 0):
            print("k must be postiv", file = stderr)
            exit(EXIT_FAILURE)
        if int(argv[1]) < int(argv[2]):
            print("k must be superior than n", file = stderr)
            exit(EXIT_FAILURE)

