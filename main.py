from flask import Flask, render_template, request
from file_proc import read_file, write_file

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>Hi!</a>"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html', active_page = 'about')

@app.route('/contact')
def contact():
  # Pieslegtsanas DB
  return render_template('contact.html', phone = 778787)

@app.route('/params')
def params():
  return render_template('params.html', args = request.args.to_dict())

@app.route('/post', methods = ['POST'])
def post ():
  return request.get_json()

@app.route('/read_from_file')
def read_from_file():
  content = read_file
  return content

@app.route ('/write_into_file')
def write_into_file():
  request_type = request.content_type
  if (request_type == "application/json"):
    contentJSON = request.get_json
    write_file(contentJSON)
    return contentJSON
  else:
    return f"Request type {request_type} not supported!"

@aoo.route('/file', methods = ['POST', 'GET'])
def file():
  if request.method == 'GET':
    return read_from_file()
  if request.method == 'POST':
    return write_into_file()



if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)