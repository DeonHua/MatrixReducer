__author__ = 'Deon Hua'
from flask import *
import os
import json
from sympy import *
init_printing()


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/getReducedMatrix/", methods = ["POST"])
def getMatrix():
    entries = request.get_json()
    matrix = Matrix(entries)
    rrefmatrix = matrix.rref()[0]
    app.logger.debug(rrefmatrix)
    if (matrix.shape[0] == matrix.shape[1]):
        array = [latex(matrix, mode="equation", itex = True), latex(rrefmatrix, mode="equation", itex = True), str(matrix.det()), str(rrefmatrix.det())]
    else:
        array = [latex(matrix, mode="equation", itex = True), latex(rrefmatrix, mode="equation", itex = True)]

    response = json.dumps(array, sort_keys=True,indent=4, separators=(',', ': '))
    return response

if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5001)))