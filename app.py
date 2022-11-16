from flask import Flask, render_template
import git 


app = Flask(__name__)

@app.route('/')
def scraping_api():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def do_scraping():
    results = git.git_api()
    return render_template('results.html', results=results)

if __name__ == ('__main__'):
    app.run()