from rdflib import Graph

input_rdf_file = r"C:\Users\mrudu\OneDrive\Desktop\Semantic Web\Mapped_Agri_Insight.rdf"  
output_ttl_file = r"C:\Users\mrudu\OneDrive\Desktop\Semantic Web\Mapped_Output.ttl"  

g = Graph()
try:
    g.parse(input_rdf_file, format="xml")  
    print(f"Successfully loaded RDF file: {input_rdf_file}")
except Exception as e:
    print(f"Error loading RDF file: {e}")


try:
    g.serialize(destination=output_ttl_file, format="turtle")
    print(f"RDF file successfully converted to Turtle format: {output_ttl_file}")
except Exception as e:
    print(f"Error converting RDF to Turtle: {e}")
