# example-dickens-data-project
A toy data project based on the collected works of Charles Dickens.

## Motivating question

Dickens is known for being long-winded. (He basically got paid by the word.)

Did his _titles_ get longer as his career progressed?

## Manifest

1. A small dataset on the works of Charles Dickens: `data/notable_works_by_charles_dickens.csv`
2. An exploratory ML model showing that Dickens' titles got longer as his career progressed: `notebooks/explore_and_predict_stuff_about_dickens_novels.ipynb`
3. A raw script, exported from the notebook: `pipeline/explore_and_predict_stuff_about_dickens_novels.py`
4. A cleaned up, productionizable version of the script: `title_length_prediction_pipeline.py`
5. A version of the script with integrated GE validation, *built assuming that the relevant GE files have been added using `great_expectations init` and `create_expectations_for_csv_files` notebook*.

Note: the "productionized" script retrains the model and exports a few parameters of interest.

```
.
├── README.md
├── data
│   └── notable_works_by_charles_dickens.csv
├── notebooks
│   └── explore_and_predict_stuff_about_dickens_novels.ipynb
└── pipeline
    ├── explore_and_predict_stuff_about_dickens_novels.py
    └── title_length_prediction_pipeline.py
```

## FAQ

1. Why would anyone want to retrain a model based on Dickens' works? Dude is dead.

    What part of "toy example" don't you understand?
