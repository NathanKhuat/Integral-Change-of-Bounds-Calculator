from os import listdir
from os.path import isfile, join
from sympy.parsing.latex import parse_latex
from src.latex_printer import LatexConverter
from flask import render_template, Flask, request, url_for
import src.algorithm as algorithm

app = Flask(__name__)
app.secret_key = "my mom makes magnificent mustard"
compiled = None


def compile_files():
    path = 'static/mathquill'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    i = 0
    all_files = []
    for file in files:
        file_name = 'mathquill/' + file
        all_files = url_for('static', filename=file_name)
        i += 1
    global compiled
    compiled = all_files


@app.route('/')
def homepage():
    if compiled is None:
        compile_files()
        return render_template('index.html', js_files=compiled)
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if compiled is None:
        compile_files()
    upper_outer = request.form['upper_outer']
    lower_outer = request.form['lower_outer']
    upper_inner = request.form['upper_inner']
    lower_inner = request.form['lower_inner']
    try:

        output = algorithm.run([str(parse_latex(upper_outer)), 
        str(parse_latex(lower_outer)), str(parse_latex(upper_inner)), 
        str(parse_latex(lower_inner))])               

        data = ''
        for i in range(len(output)):
            upper_outer = LatexConverter.convert(output[i].x_2)
            lower_outer = LatexConverter.convert(output[i].x_1)
            upper_inner = LatexConverter.convert(output[i].g_2)
            lower_inner = LatexConverter.convert(output[i].g_1)
            data += ('\\int ^ { %s } _ { %s } \\int ^ { %s } _ { %s } f(x,y) dxdy' %
            (upper_outer, lower_outer, upper_inner, lower_inner))
            if i != len(output) - 1:
                data += '+ '

        return data
    except Exception as e:
        return '\\text{ %s} ' % (str(e))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
