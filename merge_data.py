import os
import pandas as pd

data_folder = "data"
files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

merged = None

for file in files:
    file_path = os.path.join(data_folder, file)
    ticker = file.replace(".csv", "")

    try:
        df = pd.read_csv(file_path)

        # Identify date column (first column)
        first_col = df.columns[0]
        df.rename(columns={first_col: "Date"}, inplace=True)

        # Determine price column (Close or Price)
        if "Close" in df.columns:
            price_col = "Close"
        elif "Price" in df.columns:
            price_col = "Price"
        else:
            print(f"❌ No price column in {file}, skipping")
            continue

        # Parse dates & clean rows
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.dropna(subset=["Date"])

        # Keep only Date + one price column
        df = df[["Date", price_col]]
        df.rename(columns={price_col: ticker}, inplace=True)

        # Merge
        if merged is None:
            merged = df
        else:
            merged = pd.merge(merged, df, on="Date", how="outer")

        print(f"✅ Processed {file}")

    except Exception as e:
        print(f"❌ Error processing {file}: {e}")

# Save final data
if merged is not None:
    merged = merged.sort_values("Date")
    merged.to_csv("data/prices.csv", index=False)
    print("\n✅ Merged price file saved → data/prices.csv")
else:
    print("\n❌ No valid data to merge.")
