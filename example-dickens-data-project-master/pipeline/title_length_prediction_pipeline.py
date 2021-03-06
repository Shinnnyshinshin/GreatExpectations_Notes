#!/usr/bin/env python3

import json
import pandas as pd
import statsmodels.formula.api as sm
import uuid
import sys

def load_data(filepath):
    df = pd.read_csv(filepath)

    return df


def add_columns(df):
    new_df = df.copy()

    new_df["title_len"] = df.Title.map(len)
    new_df["year"] = df["Year completed"]
    new_df["is_novel"] = df.Type == "Novel"

    return new_df


def compute_model_parameters(df):
    result = sm.ols(formula="title_len ~ year", data=df).fit()

    return {
        "r_squared": result.rsquared,
        "year_beta": result.params["year"],
    }


def __main__():
    run_id = str(uuid.uuid1())
    if len(sys.argv) <= 1:
        print("Please specify a filepath to process.")
    df = load_data(sys.argv[1])
    df = add_columns(df)
    params = compute_model_parameters(df)

    print("processed run {run_id}.format(run_id)")
    print( json.dumps(params, indent=2) )

if __name__=="__main__":
    __main__()
