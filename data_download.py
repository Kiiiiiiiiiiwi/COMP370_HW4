# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "clean_dialog.csv"

# Load the latest version
df_raw = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "liury123/my-little-pony-transcript",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df_raw.head())

df_raw.to_csv("data/clean_dialog.csv", index=False)
