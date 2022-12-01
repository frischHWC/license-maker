import logging
import datetime
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='Set up an Apache LICENSE project for a non-licensed project',
                                     epilog="This program is intent to help developer's life." +
                                            "It comes with no warranty, always SAVE & BACKUP your files before")
    # Required arguments
    parser.add_argument('--folder', required=True, type=str,
                        help="Absolute path of the folder where to apply license")