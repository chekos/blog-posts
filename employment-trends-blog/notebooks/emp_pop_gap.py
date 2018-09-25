# Set up
import pandas as pd
import sys

# creating the GAP values
levels = ['less than hs', 'high school', 'some college', 'associate', "bachelor's", 'advanced degree']

gaps_data = pd.DataFrame(index = list(range(2007, 2019)))

for education_level in levels:
    # datasets
    rates = pd.read_csv(f"../data/processed/{education_level}_rate.csv", index_col = 0)
    population = pd.read_csv(f"../data/processed/{education_level}_population.csv", index_col = 0)
    employed = pd.read_csv(f"../data/processed/{education_level}_weight.csv", index_col = 0)
    
    # actual_1 - rates to compare to
    actual_1 = rates['2007']
    
    # counterfactual - if the 2007 rates stayed constant, how would the emp-to-pop ratio would have been?
    counterfactual = pd.DataFrame(index = population.index)
    
    for col in population.columns:
        counterfactual[col] = population[col] * actual_1

    # weighted by age_cohort
    weighted_counterfactual = (counterfactual * counterfactual.apply(lambda x: x / x.sum())).mean()
    weighted_actual = (employed * employed.apply(lambda x: x / x.sum())).mean()
    weighted_population = (population * population.apply(lambda x: x / x.sum())).mean()
    
    # creating the GAP value
    gap = pd.DataFrame()
    
    gap['actual'] = weighted_actual
    gap['counterfactual'] = weighted_counterfactual
    gap['population'] = weighted_population
    
    gap['actual_rate'] = gap['actual'] / gap['population']
    gap['counter_rate'] = gap['counterfactual'] / gap['population']
    
    gap['gap'] = gap['actual_rate'] - gap['counter_rate']
    gap['gap'] = gap['gap'].round(4)
    
    gap = gap.reset_index().melt(id_vars = 'index', value_vars = 'gap')
    
    gap.columns = ['year', 'gap', f"{education_level}"]
    gap['year'] = gap['year'].astype(int)
    gap.set_index('year', inplace = True)
    
    gaps_data[f"{education_level}"] = gap[f"{education_level}"]
    
# after getting all levels
dataset = gaps_data.reset_index().melt(id_vars = ['index'])
dataset.columns = ['year', 'educ_level', 'gap']

dataset['educ_level'] = dataset['educ_level'].str.replace("'", "")
dataset['educ_level'] = dataset['educ_level'].str.title()

if sys.argv[-1] == "US":
    dataset.to_csv("../data/processed/gaps_alleduc_USA.csv", index = False,)
elif sys.argv[-1] == "CA":
    dataset.to_csv("../data/processed/gaps_alleduc_CA.csv", index = False,)