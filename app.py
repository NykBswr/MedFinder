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
        aturan_pakai = df['Aturan Pakai'].to_list()
        range_harga = df['price'].to_list()
        dosis = df['Dosis'].to_list()
        efek_samping = df['Efek Samping'].to_list()

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
            results.append({
                'name': name[id],
                'uses': corpus[id],
                'aturan_pakai': aturan_pakai[id],
                'price': range_harga[id],
                'dosis': dosis[id],
                'efek_samping': efek_samping[id]
            })

        is_loading = False

        # Kirim hasil ke halaman 'search.html'
        return render_template('search.html', query=query, results=results, is_loading=is_loading)
    return redirect(url_for('search'))

if __name__ == "__main__":
    app.run(debug=True)