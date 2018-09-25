import os

# educational levels used to create files
levels = ['less than hs', 'high school', 'some college', 'associate', "bachelor's", 'advanced degree']

for value in levels:
    try: 
        os.remove(f"../data/processed/{value}_rate.csv")
        os.remove(f"../data/processed/{value}_population.csv")
        os.remove(f"../data/processed/{value}_weight.csv")
    except NotImplementedError:
        print(f"Could not delete file for: {value}")