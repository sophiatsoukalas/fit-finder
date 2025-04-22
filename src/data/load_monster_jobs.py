import pandas as pd
import os

def load_and_clean_monster_jobs():
    print(os.getcwd())
    path = "data/raw/monster_jobs.csv"
    df = pd.read_csv(path)

    print("Original shape:", df.shape)

    # Drop rows with empty job descriptions
    df = df.dropna(subset=["job_description", "job_title", "organization"])

    # # Optional: keep only relevant columns
    # df_filtered = df[["job_title", "company_name", "job_description", "location", "industry"]]
    # df_filtered = df_filtered.rename(columns={
    #     "job_title": "title",
    #     "company_name": "company",
    #     "job_description": "description"
    # })

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/monster_jobs_clean.csv", index=False)

    print(f"✅ Saved cleaned job listings ({len(df)} entries) to data/processed/monster_jobs_clean.csv")
    return df

if __name__ == "__main__":
    load_and_clean_monster_jobs()