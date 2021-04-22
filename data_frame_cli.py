# Author: Kale Fordham
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

def print_heading(text):
    """Prints text with special formatting.

        text(str): Text to be printed as heading
    """
    print('\n{} {} {}\n'.format('*'*3, text, '*'*3) )

def print_shape(csv_filename, df):
    """Prints csv filename and shape of df.

        csv_filename(str): File name corresponding to df
        df (pandas.DataFrame): DataFrame to get the shape of
    """
    print_heading('df.shape')
    print('{} loaded with shape {}'.format(csv_filename, df.shape))

def print_head(head, df):
    """Prints first five rows of csv file.

        head(bool): checks to see if head was called
        df (pandas.DataFrame): DataFrame to get the head of
    """

    # Head argument might not be called
    if(head):
        print('\n{} {} {}\n'.format('*'*3, 'df.head()', '*'*3))
        print(df.head())

def print_info(info, df):
    """Prints info with special formatting.

        info (bool): checks to see if info was called
        df (pandas.DataFrame): DataFrame to get the info of
    """

    # Info argument might not be called
    if(info):
        print('\n{} {} {}\n'.format('*'*3, 'df.info()', '*'*3))
        df.info()

def print_describe(describe, df):
    """Prints statistics of the data in file.

    describe(str): the column which is asked to describe
    df (pandas.DataFrame): DataFrame to describe
    """

    # Describe argument might not be called
    if(describe == 0):
        pass
    # Describe might be called without a column argument
    if(describe == None):
        print('\n{} {} {}\n'.format('*'*3, 'df.describe()', '*'*3))
        print(df.describe())
    # Describe might be called with a column argument
    if((describe != 0) and (describe != None)):
        # Column might not exist
        try:
            print('\n{} {} {}\n'.format('*'*3, 'df.describe()', '*'*3))
            print(df[describe].describe())
        except:
            print('{} not found'.format(describe))

def cli(args=None):
    """Main function: Connects argument parser to functions

        The csv file is a mandatory argument and is opened and read into a 
        pandas.DataFrame here. Handles file errors.

        Arguments and DataFrame are passed to corresponding functions for printing.

        args(list(str)): List of strings to be parsed as arguments.
                         If None, sys.argv is used.
    """
    if args is not None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Inspecting csv files with Pandas DataFrame methods.")
    parser.add_argument('csv_filename', help='A (nice) csv file.')
    parser.add_argument('-t', '--head', action='store_true', help='print dataframe head.')
    parser.add_argument('-i', '--info', action='store_true', help='print dataframe info.')
    parser.add_argument('-d', '--describe', nargs='?', default=0, help="""Print dataframe statistics. If COLUMN_NAME provided,
                                                             print statistics of selected column only.""")

    args = parser.parse_args(args)

    # File might not exist, be of wrong format
    try:
        df = pd.read_csv(args.csv_filename)
    except:
        print('There was an error reading {}'.format(args.csv_filename))
        print('Make sure file is present, readable, and formatted as csv.')
        exit()

    print_shape(args.csv_filename, df)
    print_head(args.head, df)
    print_info(args.info, df)
    print_describe(args.describe, df)

if __name__ == '__main__':
    cli()
