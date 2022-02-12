
import os
import sys

from flask import (
    Flask, render_template
)


volume_file = 'example.nii.gz'
surface_file = 'example.vtk'

app = Flask(__name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='templates',
)

@app.route('/volume')
def volume():
    return render_template("volume.html",
        myfile=volume_file
    )

@app.route('/isosurface')
def isosurface():
    return render_template("isosurface.html",
        myfile0=volume_file,
        myfile=surface_file
    )

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=5000)
    args = parser.parse_args()
    app.run(debug=True,host="0.0.0.0",port=args.port)
