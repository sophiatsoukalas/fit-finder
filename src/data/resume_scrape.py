import spacy
from bs4 import BeautifulSoup
import pandas as pd

nlp = spacy.load("en_core_web_lg")

def extract_ner_from_html(html_str):
    soup = BeautifulSoup(html_str, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    doc = nlp(text)

    orgs = list(set(ent.text for ent in doc.ents if ent.label_ == "ORG"))
    dates = list(set(ent.text for ent in doc.ents if ent.label_ == "DATE"))
    gpes = list(set(ent.text for ent in doc.ents if ent.label_ == "GPE"))

    return {
        "orgs": orgs,
        "dates": dates,
        "locations": gpes
    }
df = pd.read_csv('data/raw/resumes/Resume/Resume.csv')
parsed = df["Resume_html"].apply(extract_ner_from_html)
parsed_df = pd.DataFrame(parsed.tolist())
parsed_df.to_csv('data/processed/parsed_resume_features.csv', index=False)