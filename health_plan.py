#!/usr/bin/env python3

# class health_plan
# marketplace health plans by rate area

import sys
import csv

health_plans = []

class health_plan:
    def __init__(self, plan_id, state, metal_level,rate,rate_area):
        ''' Create new object of type rate_area '''

        self.plan_id = plan_id
        self.state = state
        self.metal_level = metal_level
        self.rate = rate
        self.rate_area = rate_area


def read_health_plan_data(datafile='./plans.csv'):
    ''' Read list of health plan data from available source '''

    HeaderRow = True
    n = 0
    try:
        with open(datafile) as plan_csv:
            market = csv.reader(plan_csv, delimiter=',')

            for plan_data in market:
                if HeaderRow:
                    HeaderRow = False
                else:
                    if plan_data[2] == 'Silver':
                        health_plans.append( health_plan( plan_data[0], plan_data[1], plan_data[2], plan_data[3], plan_data[4] ) )
                        n += 1
    except:
        print( f'error reading plan data from {datafile}', file=sys.stderr )
    
    return health_plans


def get_slcsp( state, rate_area ):
    ''' Find second lowest cost silver plan (SLCSP) for a given rate area '''

    rates = [float(x.rate) for x in health_plans if x.state == state and x.rate_area == rate_area]

    if len(rates) > 1:
        rates.sort()
        lowest = rates[0]
        for next_rate in rates:
            if next_rate > lowest:
                return f'{next_rate:.2f}'
    return ''


if __name__ == '__main__':
    ''' test module separately '''

    # TODO: develop formal unit tests

    print( '\n\t>>> COMPONENT TEST for health_plan.py ONLY <<<' + \
            '\n\tUsage: ./rate_area.py [-f filename | -s state -a area]\n' + \
            '\tdefault filename = ''./plans.csv''\n' + \
            '\tdefault state = ''MO''\n' + \
            '\t and rate_area = ''3''\n',  file=sys.stderr)

    # TODO: rewrite command-line parser

    if len(sys.argv) > 1 and sys.argv[1] == '-f':
        read_health_plan_data(sys.argv[2])
    else:
        read_health_plan_data()
    print( f'\t{len(health_plans)} silver plans read', file=sys.stderr )

    state = 'MO'
    area = '3'
    if len(sys.argv) > 4 and sys.argv[1] == '-s' and sys.argv[3] == '-a':
        state = sys.argv[2]
        area = sys.argv[4]
    print( f'\t{state} {area} {float(get_slcsp( state, area )):.2f}\n' )