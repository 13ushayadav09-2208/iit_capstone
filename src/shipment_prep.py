import numpy as np
import pandas as pd
hubs_df=pd.read_csv("/content/data/hubs.csv")
hubs_df.head()
hubs_df.shape
new_ship_df = pd.read_csv("/content/data/new_shipments.csv")
new_ship_df.head()
raw_shipments_df=pd.read_csv("/content/data/raw_shipments.csv")
raw_shipments_df.head()
raw_shipments_df.shape
raw_shipments_df.duplicated()
raw_shipments_df.duplicated().sum()
raw_shipments_df["service_type"].unique()
raw_shipments_df["declared_value_inr"] = (
    raw_shipments_df["declared_value"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
raw_shipments_df
raw_shipments_df.info()
raw_shipments_df["dispatch_time"] = pd.to_datetime(
    raw_shipments_df["dispatch_time"]
)
raw_shipments_df.info()
sentinel_count = (
   raw_shipments_df["parcel_weight_kg"] > 100
).sum()

raw_shipments_df.loc[
      raw_shipments_df["parcel_weight_kg"] > 100,
    "parcel_weight_kg"
] = np.nan
sentinel_count
raw_shipments_df.info()
toy_weights = pd.Series([
    1.0, 2.0, np.nan, 3.0, 4.0
])

print("Mean:", toy_weights.mean())
print("Median:", toy_weights.median())

filled = toy_weights.fillna(
    toy_weights.median()
)
toy_weights = pd.Series([
    1.0, 2.0, np.nan, 3.0, 4.0, 100.0
])

print("Mean:", toy_weights.mean())
print("Median:", toy_weights.median())
