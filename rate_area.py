#!/usr/bin/env python3

# class rate_area
# rate area is indicated by state and index id

import sys
import csv

DEV = True

areas = []

class rate_area:
    def __init__(self, zipcode, state, id):
        ''' Create new object of type rate_area '''
        self.zipcode = zipcode
        self.state = state
        self.id = id


def read_rate_area_data(datafile='./zips.csv'):
    ''' Build list of rate area data from available source '''

    HeaderRow = True
    n = 0
    try:
        with open(datafile) as zip_csv:
            zips = csv.reader(zip_csv, delimiter=',')
            for zip_data in zips:
                if HeaderRow:
                    HeaderRow = False
                else:
                    areas.append( rate_area( zip_data[0], zip_data[1], zip_data[4] ) )
                    n += 1
    except:
        print( f'error reading rate area data from {datafile}', file=sys.stderr )
    

def get_rate_area(zip):
    count = sum(1 for rec in areas if rec.zipcode == zip)
    rate_area = ''
    if count > 0:
        # get state and rate_area_id
        state = next( x.state for x in areas if x.zipcode == zip  )
        id = next( x.id for x in areas if x.zipcode == zip  )
        rate_area = (state, id)

        # if not distinct, validate not ambiguous
        if count > 1:
            if any( a.state != state for a in areas if a.zipcode == zip):
                return ''
            if any( a.id != id for a in areas if a.zipcode == zip):
                return ''
    return rate_area


if __name__ == '__main__':
    ''' test module separately '''

    # TODO: develop formal unit tests

    print( '\n\t>>> COMPONENT TEST for rate_area.py ONLY <<<' + \
            '\n\tUsage: ./rate_area.py [-f filename | -z zipcode]\n' + \
            '\tdefault filename = ''./zips.csv''\n' + \
            '\t and zipcode = ''64148''\n',  file=sys.stderr)

    
    if len(sys.argv) > 1 and sys.argv[1] == '-f':
        zipcode_data = sys.argv[2]
        read_rate_area_data(zipcode_data)
    else:
        read_rate_area_data()
    print( f'\t{len(areas)} rate areas stored', file=sys.stderr )


    zip = '64148'
    if len(sys.argv) > 1 and sys.argv[1] == '-z':
        zip = sys.argv[2]
    print( f'\tZIPcode: {zip} --> {get_rate_area( zip )}\n' )