import numpy as np
import pandas as pd

def calculate(numbers_list):
    if len(numbers_list) != 9:
        raise ValueError("List must contain nine numbers.")

    narr = np.array_split(numbers_list,3)
    df = pd.DataFrame(narr)

    flatten_matrix = df.to_numpy().flatten()

    calculations = {}

    all_partials = []
    all_partials.append(list( df.mean(axis=0).values))
    all_partials.append(list( df.mean(axis=1).values))
    all_partials.append(flatten_matrix.mean())
    calculations['mean'] = all_partials

    all_partials = []
    all_partials.append(list( df.var(axis=0,ddof=0).values))
    all_partials.append(list( df.var(axis=1,ddof=0).values))
    all_partials.append(flatten_matrix.var(ddof=0))
    calculations['variance'] = all_partials

    all_partials = []
    all_partials.append(list( df.std(axis=0,ddof=0).values))
    all_partials.append(list( df.std(axis=1,ddof=0).values))
    all_partials.append(flatten_matrix.std(ddof=0))
    calculations['standard deviation'] = all_partials

    all_partials = []
    all_partials.append(list( df.max(axis=0).values))
    all_partials.append(list( df.max(axis=1).values))
    all_partials.append(flatten_matrix.max())
    calculations['max'] = all_partials

    all_partials = []
    all_partials.append(list( df.min(axis=0).values))
    all_partials.append(list( df.min(axis=1).values))
    all_partials.append(flatten_matrix.min())
    calculations['min'] = all_partials

    all_partials = []
    all_partials.append(list( df.sum(axis=0).values))
    all_partials.append(list( df.sum(axis=1).values))
    all_partials.append(flatten_matrix.sum())
    calculations['sum'] = all_partials


    return calculations