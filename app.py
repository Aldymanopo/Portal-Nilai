from flask import Flask, render_template, jsonify
from rdflib import Graph, Namespace, Literal, URIRef

app = Flask(__name__)

# --- DATABASE RDF (Format Turtle) ---
# Data ini disimpan di memori Python saat dijalankan
rdf_data = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/kampus/> .

# Data Mahasiswa
ex:AldyManoppo rdf:type ex:Mahasiswa ;
    ex:namaDepan "Aldy" ;
    ex:namaBelakang "Manoppo" ;
    ex:memilikiNilai ex:NilaiInggris, ex:NilaiPemrograman, ex:NilaiBasisData .

# Data Nilai dan Grade
ex:NilaiInggris ex:namaMatkul "Bahasa Inggris" ; ex:nilaiAngka 85 ; ex:grade "A" .
ex:NilaiPemrograman ex:namaMatkul "Pemrograman" ; ex:nilaiAngka 90 ; ex:grade "A" .
ex:NilaiBasisData ex:namaMatkul "Basis Data" ; ex:nilaiAngka 88 ; ex:grade "A-" .
"""

@app.route('/')
def home():
    # Flask akan mencari file ini di dalam folder 'templates'
    return render_template('index.html')

@app.route('/api/get-nilai')
def get_nilai():
    # 1. Siapkan Graph RDF
    g = Graph()
    g.parse(data=rdf_data, format="turtle")

    # 2. Query SPARQL untuk mengambil data
    query_sparql = """
        PREFIX ex: <http://example.org/kampus/>
        SELECT ?matkul ?nilai ?grade
        WHERE {
            ?mhs ex:namaDepan "Aldy" ;
                 ex:memilikiNilai ?hasil .
            ?hasil ex:namaMatkul ?matkul ;
                   ex:nilaiAngka ?nilai ;
                   ex:grade ?grade .
        }
    """
    
    results = g.query(query_sparql)
    
    # 3. Ubah hasil SPARQL jadi JSON biar bisa dibaca JavaScript
    data_list = []
    for row in results:
        data_list.append({
            "matkul": str(row.matkul),
            "angka": str(row.nilai),
            "grade": str(row.grade)
        })
    
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
