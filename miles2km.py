#!/usr/bin/env python3

"""
miles2km

Converts miles to kilometers. This script takes a mileage input from the user via command-line arguments and converts
it to kilometers, displaying the result.

Usage: python miles-to-km.py <miles>

Author: Fearghal Hayes
Date: October 8th, 2019
"""

import argparse


def convert_miles_to_km(miles):
    """Converts miles to kilometers."""
    return miles * 1.60934


def main():
    parser = argparse.ArgumentParser(description="Convert miles to kilometers.")
    parser.add_argument("miles", type=float, help="Miles to be converted to kilometers.")
    args = parser.parse_args()

    km = convert_miles_to_km(args.miles)
    print(f"{args.miles} miles is equivalent to {km:.2f} kilometers.")


if __name__ == "__main__":
    main()
