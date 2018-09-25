# Set up
import pandas as pd
import sys

# dataset
data_file = sys.argv[-1]
if sys.argv[-1] == 'age_adj.csv':
    df = pd.read_csv("../data/processed/age_adj.csv")
elif sys.argv[-1] == 'age_adj_CA.csv':
    df = pd.read_csv("../data/processed/age_adj_CA.csv")
else: 
    print("That's not one of the datasets.")

# data_cleaner

# level of education: 6 values
level_of_education = [val for val in df['education'].unique()]

for education_level in level_of_education:
    
    # create a dataset for that educational level
    education_level_data = df[df['education'] == education_level]
    
    # total population
    total_pop = education_level_data.groupby(['year', 'education', 'age_group'])[['weight']].sum().copy()
    
    # "rate" already has employment to population ratio
    ## drop unemployed obs
    education_level_data = education_level_data[education_level_data['employed'] == 'employed'].copy()
    
    # reset index to 0 for later merging
    education_level_data.index = list(range(education_level_data.shape[0]))
    
    # add total population column
    education_level_data['population'] = total_pop.reset_index()['weight'].copy()
    
    # create the pivot table from which the datasets will be created
    table = education_level_data.pivot_table(
        columns = ['age_group'],
        values = ['population', 'rate', 'weight'],
        index = ['year'],
    ).unstack().to_frame().unstack(1).T
    
    # drop one unnecessary index level
    table.index = table.index.droplevel()
    
    # write datasets
    table['rate'].to_csv(f"../data/processed/{education_level}_rate.csv",)
    table['population'].to_csv(f"../data/processed/{education_level}_population.csv",)
    table['weight'].to_csv(f"../data/processed/{education_level}_weight.csv",)