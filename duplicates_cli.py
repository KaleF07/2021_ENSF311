import sys
import hash_functions as hfcs
import dir_functions as dfcs
import argparse

def get_hash(filename):
    """ takes a filename and returns it's hash

    filename (str): name of the file

    returns: (str) the hash of the filename given
    """
    fin = open(filename, 'rb')
    message = fin.read()
    fin.close()
    return hfcs.hashmd5(message)


def get_all_hashes(dirname):
    """ Sorts files with similar hashes under the same dirname

    dirname (str): name of files to find

    returns: (dict) a dict conatining the files with similar hashes
    
    """

    #finds files with the same directory name
    file_names = dfcs.walk(dirname)
    
    d = {}

    ## this loop sorts files with same hash
    for name in file_names:

        ## call to get_hash creates a hash of the current file
        h = get_hash(name) 

        ## checks to see if hash already exists in dict
        if h in d:
            d[h].append(name) ## if it exists, it will add name of current file to hash
        else:
            d[h] = [name] ## if it doesn't, adds hash to dict
    return d

def get_hashes(dirname, ext):
    """ Sorts files with similar hashes under the same dirname and extension

    dirname (str): name of files to find
    ext (str): end of files to find

    returns: (dict) a dict conatining the files with similar hashes
    
    """
    #finds files with the same directory name
    file_names = dfcs.walk(dirname)

    files_with_ext = []
    ## this loop filters files with the same extension
    for names in file_names:
        if (names.endswith(ext)):
            files_with_ext.append(names)

    file_names = files_with_ext
    
    d = {}

    ## this loop sorts files with same hash
    for name in file_names:

        ## call to get_hash creates a hash of the current file
        h = get_hash(name) 

        ## checks to see if hash matches in dict
        if h in d:
            d[h].append(name) ## if it exists, it will add name of current file to hash
        else:
            d[h] = [name] ## if it doesn't, adds hash to dict
    return d

def print_duplicates(hash_dict):
    """ Prints names of all files with similar hashes under

    hash_dict (dict): contains all files with similar hashes under
    """

    ## loop to print all files with the same hash
    for h, names in hash_dict.items():
        if len(names)>1:
            print("These files have the same hash:")
            for name in sorted(names):
                print(f"\t{name}")

def cli(args=None):
    """ Creates a command line to interact with functions in duplicate_cli.py
    """
    ## This is needed to allow for testing command line interface with pytest
    if not args:
        args = sys.argv[1:]

    # add parser argument to create the CLI for users
    parser = argparse.ArgumentParser(description = 'Duplicate files search')
    parser.add_argument('dirname', help = "name of file to find duplicates of.")
    parser.add_argument('-e', '--extension', help = 'searches for files with given extension.')

    # set parser arguments
    args = parser.parse_args(args)
    dirname = args.dirname
    ext = args.extension

    ## checks to see if there is an extension argument
    if (ext == None):
        file_hashes = get_all_hashes(dirname)
    else:
        file_hashes = get_hashes(dirname, ext)
    
    print_duplicates(file_hashes)

if __name__ == '__main__':
    cli()