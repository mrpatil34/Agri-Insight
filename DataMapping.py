import pandas as pd
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

rdf_file_path = r"C:\Users\mrudu\OneDrive\Desktop\Semantic Web\Plain_Agri_Insight.rdf"
csv_file_path = r"C:\Users\mrudu\OneDrive\Desktop\Semantic Web\FinalCombined.csv"
output_rdf_file = r"C:\Users\mrudu\OneDrive\Desktop\Semantic Web\Mapped_Agri_Insight.rdf"

g = Graph()
try:
    g.parse(rdf_file_path, format="xml")
    print(f"Successfully loaded RDF file: {rdf_file_path}")
except Exception as e:
    print(f"Error loading RDF file: {rdf_file_path}")
    print(e)


EX = Namespace("http://example.org/ontology#")
SCHEMA = Namespace("http://schema.org/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
g.bind("ex", EX)
g.bind("schema", SCHEMA)
g.bind("owl", OWL)

data = pd.read_csv(csv_file_path)

data.columns = data.columns.str.strip().str.lower()

columns = [
    "crop", "year", "country", "region", "avgtemp", "precipitation", "co2",
    "yield", "extremeevents", "pesticideuse", "fertilizeruse", "soilhealth",
    "strategies", "economicimpact", "irrigationtype", "soiltype", "season", "soilimpact"
]

def generate_subject(row, index):
    return URIRef(f"http://example.org/resource/{row['crop'].replace(' ', '_')}_{index}")

for index, row in data.iterrows():
    subject = generate_subject(row, index)
    
    for col in columns:
        if col in data.columns and not pd.isna(row[col]):
            value = row[col]    
            if isinstance(value, float):
                g.add((subject, EX[col], Literal(value, datatype=XSD.float)))
            elif isinstance(value, int):
                g.add((subject, EX[col], Literal(value, datatype=XSD.integer)))
            else:
                g.add((subject, EX[col], Literal(str(value), datatype=XSD.string)))

g.serialize(destination=output_rdf_file, format="xml")
print(f"RDF file updated and saved to {output_rdf_file}")
