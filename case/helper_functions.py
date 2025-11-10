import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter


def create_duration_table(assets: pd.DataFrame):
    """
    Create duration table from assets table given

    Parameters: asset (a dataframe cointaining columns used for creation of a duration table aimed for time to payment analysis.
     In this function this field are needed in the input dataframe
     ['asset_id', 'seller_tax_id', 'face_value' ,'created_at', 'settled_at' ,'due_date',  'reference_date'] )
     It returns a duration table ready for use for survival analysis and modeling

    """

    assets["maturity_date"] = pd.to_datetime(assets["maturity_date"])
    assets["due_date"] = pd.to_datetime(assets["due_date"])
    assets["reference_date"] = pd.to_datetime(assets["reference_date"])

    assets = assets.loc[~assets.created_at.isnull()]
    assets = assets.loc[~(assets["settled_at"] < assets["created_at"])]
    assets = assets.loc[~(assets["created_at"] > assets["reference_date"])]

    duration_table = assets[
        [
            "asset_id",
            "seller_tax_id",
            "face_value",
            "created_at",
            "settled_at",
            "due_date",
            "reference_date",
        ]
    ]

    duration_table["duration_days"] = np.where(
        duration_table["settled_at"].isnull(),
        (duration_table["reference_date"] - duration_table["created_at"]).dt.days,
        (duration_table["settled_at"] - duration_table["created_at"]).dt.days,
    )

    duration_table["paid"] = np.where(duration_table["settled_at"].isnull(), 0, 1)

    duration_table["late_payment"] = np.where(
        (duration_table["paid"] == 1)
        & (duration_table["settled_at"] > duration_table["due_date"]),
        1,
        0,
    )

    duration_table["cohort_month"] = (
        duration_table["created_at"].dt.to_period("M").astype("str")
    )
    duration_table["cohort_quarter"] = (
        duration_table["created_at"].dt.to_period("Q").astype("str")
    )
    duration_table["cohort_year"] = (
        duration_table["created_at"].dt.to_period("Y").astype("str")
    )

    return duration_table


def plot_km_curve_category(col, df):
    """
    Plot Kaplan-Meier survival curves for each category in the specified column.

    Parameters:
    - col: str, column name to group by
    - df: DataFrame, data to use (default: assets_duration_company)
    - min_count: int, minimum number of samples per category to plot (default: 1000)
    """
    kmf = KaplanMeierFitter()
    plt.figure(figsize=(12, 7))
    labels = []
    for cat, grp in df.groupby(col):
        kmf.fit(
            grp["duration_days"],
            event_observed=grp["paid"],
            label=f"{cat} (n={len(grp)})",
        )
        kmf.plot(ci_show=False)
        labels.append(cat)
    plt.title(f"Kaplan–Meier: Time to Payment by {col}")
    plt.xlabel("Duration (days)")
    plt.ylabel("Survival probability (not yet paid)")
    plt.legend()
    plt.grid(True)
    plt.show()
    return labels


def add_company_info(duration, company):
    """
    Add company info information to duration table.
    Converts company-related columns to object dtype,
    fills missing with 'NULL', and adds 'has_company_info'
    indicating whether at least one company field was originally present.
    If no information about the seller is present than 'has_company_info' gets 0, 1 otherwise
    """
    df = duration.rename(columns={"seller_tax_id":"tax_id"})
    df = df.merge(company, how='left')
    company_cols = [
        "company_status",
        "company_status_date",
        "company_creation_date",
        "company_size",
        "main_cnae",
        "main_cnae_description",
        "secondary_cnae_array",
        "legal_nature",
        "is_mei",
        "city",
        "state",
        "zipcode",
    ]

    df = df.copy()


    existing_cols = [col for col in company_cols if col in df.columns]

    df["has_company_info"] = df[existing_cols].notna().any(axis=1).astype(int)

    for col in existing_cols:
        df[col] = df[col].astype(object).fillna("NULL")

    return df

def add_quod_info(duration, quod): 
    """
    This function adds quod_score in the durations dataframe, after deduplication, then create flags for missing values in score_quod and presumed_revenue
    fields (labeled -1)
    """    
    quod = quod.loc[quod.groupby("tax_id")["created_at"].idxmax()].drop('created_at', axis=1)
    df = duration.merge(quod, on='tax_id', how='left')
    for i in ['quod_score', 'presumed_revenue']:
        df['quod_score'] = np.where(df['quod_score'].isna(), -1, df['quod_score'])
        df['presumed_revenue'] = np.where(df['presumed_revenue'].isna(), -1, df['presumed_revenue'])
    df['has_quod_info'] = np.where ((df['quod_score'] == -1) & (df['presumed_revenue'] == -1) , 0, 1)
    return df

def group_rare_categories(df, column_name):
    """
    Group categories with low frequency (less than 1000 records by default)
    
    Parameters:
    -----------
    df : DataFrame
        DataFrame s
    column_name : str
       column to be processed

    Returns:
    --------
    DataFrame
        DataFrame com a coluna modificada
    """
    
    df = df.copy()    
   
    counts = df[column_name].value_counts()
    rare_categories = counts[counts <= 1000].index
    
    df.loc[df[column_name].isin(rare_categories), column_name] = 'Demais'
    
    return df


if __name__ == "__main__":
    pass
