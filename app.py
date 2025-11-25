from flask import Flask, render_template, jsonify
from rdflib import Graph

app = Flask(__name__)

# --- DATABASE RDF (Turtle Format) ---
# Disimpan di sini agar tidak perlu menyalakan server Fuseki/XAMPP
rdf_data = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.org/kampus/> .

# Data Mahasiswa
ex:AldyManoppo rdf:type ex:Mahasiswa ;
    ex:namaDepan "Aldy" ;
    ex:namaBelakang "Manoppo" ;
    ex:memilikiNilai ex:NilaiInggris, ex:NilaiPemrograman, ex:NilaiBasisData .

# Data Nilai
ex:NilaiInggris ex:namaMatkul "Bahasa Inggris" ; ex:nilaiAngka 85 .
ex:NilaiPemrograman ex:namaMatkul "Pemrograman" ; ex:nilaiAngka 90 .
ex:NilaiBasisData ex:namaMatkul "Basis Data" ; ex:nilaiAngka 88 .
"""

@app.route('/')
def home():
    # Mengirim file HTML ke browser
    return render_template('index.html')

@app.route('/api/get-nilai')
def get_nilai():
    # Proses Query SPARQL
    g = Graph()
    g.parse(data=rdf_data, format="turtle")

    query = """
        PREFIX ex: <http://example.org/kampus/>
        SELECT ?namaDepan ?namaBelakang ?matkul ?nilai
        WHERE {
            ?mhs ex:namaDepan ?namaDepan ;
                 ex:namaBelakang ?namaBelakang ;
                 ex:memilikiNilai ?hasil .
            ?hasil ex:namaMatkul ?matkul ;
                   ex:nilaiAngka ?nilai .
        }
    """
    results = g.query(query)
    
    # Ubah hasil SPARQL menjadi format JSON untuk JavaScript
    data_list = []
    for row in results:
        data_list.append({
            "nama": f"{row.namaDepan} {row.namaBelakang}",
            "matkul": str(row.matkul),
            "nilai": str(row.nilai)
        })
    
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
