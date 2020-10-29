import argparse
import numpy as np


def pow_two_plus_one(n):
    return (2 ^ n) + 1


def diamond_square(n):
    size = pow_two_plus_one(n)
    image = np.ndarray((size, size))
    return image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Verbose output',
                        action='store_true')
    parser.add_argument('-s', '--size', help='Power of 2 to initialise array',
                        type=int, default=8)
    args = parser.parse_args()
    image = diamond_square(args.size)


if __name__ == '__main__':
    # execute only if run as a script
    main()
