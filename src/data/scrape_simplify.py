import requests
import pandas as pd
import os
import json


def fetch_jobs_from_search_api(url):
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data))
    # Navigate into results[1]['hits'] (where the real jobs are)
    hits = data.get('hits', [])
    print(hits[0]['document'])

    job_docs = [hit["document"] for hit in hits]
    df = pd.DataFrame(job_docs)
    #df.to_csv("data/processed/simplify_search_jobs.csv", index=False)

    print(f"✅ Extracted and saved {len(df)} jobs.")
    return df

# Example usage — you'll need the real URL from your browser's Network tab
if __name__ == "__main__":
    url = "https://xv95tgzrem61cja4p.a1.typesense.net/collections/jobs/documents/search?q=&query_by=functions&facet_by=functions&max_facet_values=9999999&x-typesense-api-key=sUjQlkfBFnglUFcsFsZVcE7xhI8lJ1RG"
    fetch_jobs_from_search_api(url)