from flask import Flask, render_template
import git 


app = Flask(__name__, static_folder='./templates/img')

@app.route('/')
def scraping_api():
    back_pic = './img/background.png'
    img_path = './img/star.png'
    return render_template('index.html', img_path = img_path, back_pic = back_pic)

@app.route('/results', methods=['POST'])
def do_scraping():
    univers_img = './img/univers.png'
    results = git.git_api()
    urls = git.link_url()
    
    return render_template('results.html', univers_img = univers_img, git_links=zip(results,urls))


if __name__ == ('__main__'):
    app.run(debug=True)
  