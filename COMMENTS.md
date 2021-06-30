# COMMENTS

Attached is _a_ solution for the SLCSP method.


## Source files

- health_plan.py
   - __class health_plan__ is the data model for reading the CSV
   - __read_health_plan_data()__ reads the (filtered _silver_) plan data (default './plans.csv') into memory (no return value)
   - __get_slcsp()__ returns second lowest cost silver plan, if available given rate_area tuple, and formatted with 2 decimal places
   - if invoked independently, contains minimal unit testing  
- rate_area.py
   - __class rate_area__ is the data model for reading the CSV
   - __read_rate_area_data()__ reads only the subset of data required to determine rate_area (default './plans.csv') into memory (no return)
   - __get_rate_area()__ finds rate_area and returns (as tuple) if available and unambiguous
   - if invoked independently, contains minimal unit testing  
- slcsp.py
   - __main()__ entry point


## Assumptions


---------------

(optional:)
(_includes minimal unit testing for the class module_)
``` 
chmod +x health_plan.py
    ./health_plan.py
    ./health_plan.py -f ./my_plans.csv
    ./health_plan.py -s TX -a 5
```

---------------

(optional:)
```
chmod +x rate_area.py
    ./rate_area.py

```

---------------
