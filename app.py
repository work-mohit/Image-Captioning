from flask import Flask, render_template, redirect,request
import Caption_generator

app = Flask(__name__)
@app.route('/')
def caption():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        path = './static/' + f.filename
        f.save(path)
        caption = Caption_generator.caption_it(path)
        result_dic = {
        'caption' :caption ,
        'image' :path
        }

    return render_template('index.html', results = result_dic)



if __name__ =='__main__':
    app.run(debug=False,threaded=False)



