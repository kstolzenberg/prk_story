from flask import Flask 
from flask import render_template
import requests
import json
import time

start = time.time()

from plotdevice import * 
print "time to import drawing library: %g" % (time.time()-start)


app = Flask(__name__)
@app.route('/parking')

def parking():
    r = requests.get("https://data.sfgov.org/resource/uupn-yfaw.json") # these are offstreet from 2011
    p = requests.get("https://data.sfgov.org/resource/3gg2-z57m.json") # these are on-street from 2008 - onward

    data_off = json.loads(r.text)
    data_on = json.loads(p.text)

    reg_stallct = []
    valet_stallct = []
    street_sply = []

    def isolate(data_stream, new_list, key):
        for i in range(len(data_stream)):
            new_list.append(float(data_stream[i][key]))

    isolate(data_off, reg_stallct, 'regcap')
    isolate(data_off, valet_stallct, 'valetcap')
    isolate(data_on, street_sply,'prkng_sply')

    # calc the ratios
    total_stallct = sum(reg_stallct) + sum(valet_stallct) + sum(street_sply) # tidy this num
    total_prk_sf = total_stallct * (162) # 9'* 18' avg prk spot = 162 sq.ft // SF Planning 154: min offstreet size = 8x18=144sf. ADA:9x18  Onstreet:20*8
    total_prk_area = total_prk_sf / 27878400 # 1sq mile is 27878400 sq ft
    sf_area = 46.87 # sq miles per census bureau // you could subtract out remaining area of streets? not sure how that would overlap?
    prk_ratio = (total_prk_area / sf_area) # tidy this number to 0.05?
    possible_apt = (total_prk_sf / 511) # average studio size is 511 sf per Paragon

    # plotdevice drawing
    size(600,600)
    color(mode=RGB, range=255)
    background(None)

    svg = ximport("svg")
    # it can only find full path? how will this scale for heroku?
    sf_paths = svg.parse(open('/Users/karen/pyprojects/prk_story/prk_story/static/sf36.svg').read())
    sf_path = sf_paths[0]

    def sf_correction(path, x, y):
        x_offset = 0
        y_offset = -30
        return x-path.center.x+x_offset, y-path.center.y+y_offset

    sf_path.translate(*sf_correction(sf_path, WIDTH/2, HEIGHT/2))
    sf_path.scale(3)

    drawpath(sf_path.copy(), fill=("white", 1))

    with clip(sf_path):
        geometry(PERCENT)
        total_ratio = prk_ratio
        rotate(.17)
        arc(WIDTH/2, (HEIGHT/2)+30, 275, range=total_ratio, fill=('red',.5), close=True)

    reset()
    color(mode=RGB, range=255)
    fill(90)
    text("The Rest of San Francisco",140,450,fontsize=16,family="Hammersmith One")
    text("Parking",392,190,fontsize=12,family="Hammersmith One")

    export("/Users/karen/pyprojects/prk_story/prk_story/static/diagram.png")

    return render_template('layout.html',
                            total_stallct = total_stallct,
                            total_prk_area = total_prk_area,
                            prk_ratio = prk_ratio,
                            possible_apt = possible_apt
                            ) 

if __name__ == "__main__":
    app.run(debug=True)