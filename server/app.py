from flask import Flask, request, make_response, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/articles/<int:id>', methods=['GET'])
def view_article(id):
    if 'page_views' not in session:
        session['page_views'] = 0

    session['page_views'] += 1

    if session['page_views'] <= 3:
        # Render a JSON response with the article data
        article_data = {
            'id': id,
            'title': 'Article Title',
            'content': 'Article Content',
        }
        return jsonify(article_data)
    else:
        # Render a JSON response with the error message and status code 401
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

@app.route('/clear', methods=['GET'])
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(port=5555)
