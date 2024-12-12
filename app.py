import os
from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, flash, session
from semantic_search import SemanticSearch
from lexical_search import LexicalSearch
from hybrid_search import reciprocal_rank_fusion
import pandas as pd
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/send_query', methods=['POST'])
def send_query():
    query = request.form.get('query')
    is_loading = True
    if query:
        df = pd.read_csv('data_halodoc_ordered.csv', sep=';')
        corpus = df['uses'].to_list()
        name = df['name'].to_list()
        indikasi_umum = df['Indikasi Umum'].to_list()
        aturan_pakai = df['Aturan Pakai'].to_list()
        range_harga = df['price'].to_list()
        dosis = df['Dosis'].to_list()
        efek_samping = df['Efek Samping'].to_list()
        perhatian = df['Perhatian'].to_list()

        # Membaca hasil scraping gambar
        scraping_df = pd.read_csv('data_img_halodoc.csv')
        image_urls = dict(zip(scraping_df['name'], scraping_df['Image URL']))

        # Proses query menggunakan model pencarian
        lexical_model = LexicalSearch()
        lexical_rank = lexical_model.rank(corpus, query)

        semantic_model = SemanticSearch()
        semantic_model.load_pretrained()
        semantic_rank = semantic_model.rank(corpus, query)

        fusion_rank = reciprocal_rank_fusion(semantic_rank, lexical_rank, 60)
        corpus_id = list(fusion_rank.keys())

        # Ambil hasil pencarian dengan semua data terkait
        results = []
        for id in corpus_id[:1]:
            hasil = {
                'name': name[id],
                'uses': corpus[id],
                'indikasi_umum': indikasi_umum[id],
                'aturan_pakai': aturan_pakai[id],
                'price': range_harga[id],
                'dosis': dosis[id],
                'efek_samping': efek_samping[id],
                'perhatian': perhatian[id]
            }
        
            # Menambahkan URL gambar jika ada
            obat_name = name[id]
            if obat_name in image_urls:
                hasil['image_url'] = image_urls[obat_name]
            else:
                hasil['image_url'] = None

            results.append(hasil)

        is_loading = False

        # Kirim hasil ke halaman 'search.html'
        return render_template('search.html', query=query, results=results, is_loading=is_loading)
    return redirect(url_for('search'))

@app.route('/listObat')
def list_obat():
    # Membaca data obat dari CSV
    df_obat = pd.read_csv('data_halodoc_ordered.csv', sep=';')
    
    # Membaca data gambar obat dari CSV
    df_img = pd.read_csv('data_img_halodoc.csv')
    
    # Mengubah data gambar menjadi dictionary {nama_obat: image_url}
    image_urls = dict(zip(df_img['name'], df_img['Image URL']))
    
    # Menyiapkan data yang akan dikirim ke template
    obat_data = []
    for index, row in df_obat.iterrows():
        obat_name = row['name']
        
        # Ambil URL gambar dari dictionary jika ada, jika tidak None
        image_url = image_urls.get(obat_name, None)
        
        # Menambahkan informasi obat ke dalam list obat_data
        obat_data.append({
            'name': obat_name,
            'indikasi_umum': row['Indikasi Umum'],
            'image_url': image_url
        })
    
    # Kirim data obat ke template
    return render_template('list_obat.html', obat_data=obat_data)

if __name__ == "__main__":
    app.run(debug=True)