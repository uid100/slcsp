#!/usr/bin/env python3

# Find second lowest cost silver plan (SLCSP) by ZIP code
#
# Usage:  
#   slcsp.py [-f | --file filename]
#   slcsp.py [filename]
#
# 1. Store rate_area and "silver" plan data to a collection to minimize disk access
# 2. loop through input data (from file or stdin)
#    3. find and validate slcsp
#    4. output to stdout

import sys
import rate_area as region
import health_plan as market

def main():
    ''' Read through input list of zip codes and output SLCSP if available '''

    DataHeaderRow = True

    try:
        # read data files once with local scope to those modules
        region.read_rate_area_data() # read from default file
        market.read_health_plan_data() # read from default file

        fname = input_filename() or './slcsp.csv'
        if( fname == '-'):
            input_file = sys.stdin
        else:
            input_file = open(fname,'r')

        for z in input_file:
            if DataHeaderRow:
                # first time: echo header to stdout
                DataHeaderRow = False
                print( f'{z}', end='' )
            else:
                # loop through remaining rows to EOF
                zip = z.split(',',1)[0]

                # lookup and validate rate area
                rate_area = region.get_rate_area(zip)
                if len(rate_area) == 2:
                    slcsp = market.get_slcsp(*rate_area)
                else:
                    slcsp = ''
                print( zip + ',' + slcsp )

    except(FileNotFoundError):
        print( f'error opening file {fname} for reading', file=sys.stderr)
    except:
        print( f'Unexpected Error: {sys.exc_info()[0]}', file=sys.stderr )


def input_filename():
    ''' Get filename from command line if given '''

    # TODO: rewrite command line parser to separate module and add support to specify rate_area (zips.csv) and plan data(plans.csv)
    n = 1
    while n<len(sys.argv):
        if len(sys.argv)>1:
            if sys.argv[n] == '-' :
                return '-'
            if sys.argv[n] in ['-f', '--file']:
                return sys.argv[n+1]
            if sys.argv[n][0] == '-':
                print( 'unsupported command line option', file=sys.stderr )
            else:
                return sys.argv[n]
        n+=1
    return ''


if (__name__ == '__main__'):
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print('NAME:\n' \
            + f'\t{sys.argv[0]} - find the second lowest cost silver plan (SLCSP) for a group of ZIP codes.' \
            + 'SYNOPSIS:\n' \
            + f'\t{sys.argv[0]} [-h | --help] | [[-f | --file] filename]\n' \
            + 'OPTIONS:\n' \
            + '\t-h | --help this usage statement\n' \
            + '\t-f | --file indicates ', file=sys.stderr )
    else:
        main()
