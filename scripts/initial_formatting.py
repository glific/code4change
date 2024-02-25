import pandas as pd

coding_dict = pd.read_excel("data/coding_dict.xlsx", sheet_name="work_doc")
price_data = pd.read_csv("data/PRICE_dataset.csv")

# check if all price data cols are present in coding dict or not
cols = price_data.columns
for price_data_col in cols:
    if price_data_col not in list(coding_dict["Variable Name"]):
        print(
            "This col from price data is not present in coding dict variable name "
            + price_data_col
        )

# Update Q10 related columns to match with coding dict
q10_map = {
    "Q10_1": "Q10_1A",
    "Q10_2": "Q10_2A",
    "Q10_3": "Q10_3A",
    "Q10_4": "Q10_4A",
    "Q10_5": "Q10_5A",
    "Q10_6": "Q10_6A",
    "Q10_7": "Q10_7A",
    "Q10_8": "Q10_8A",
    "Q10_9": "Q10_9A",
    "Q10_10": "Q10_10A",
    "Q10_11": "Q10_11A",
    "Q10_12": "Q10_12A",
}
price_data.rename(columns=q10_map, inplace=True)

# check if all price data cols are present in coding dict or not
cols = price_data.columns
print(
    "rechecking if all columns from price data are there in coding dict variable name or not"
)
for price_data_col in cols:
    if price_data_col not in list(coding_dict["Variable Name"]):
        print("This col is not present in raw data " + price_data_col)


# update price data; col names
rename_col_dict = {}
for old_col in list(price_data.columns):
    new_col = list(
        coding_dict.loc[coding_dict["Variable Name"] == str(old_col), "Code"]
    )[0]
    print("Mapping col name of raw data from " + old_col + " >> " + new_col)
    rename_col_dict[old_col] = new_col
price_data.rename(columns=rename_col_dict, inplace=True)


# save data to a csv
price_data.to_csv("output/PRICE_dataset_formatted.csv", index=False)
