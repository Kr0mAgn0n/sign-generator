# -*- coding: utf-8 -*-

from flask import Flask, send_file, render_template, request
from StringIO import StringIO
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generar/")
def generar():
    titulo = request.args['titulo']
    apellidos = request.args['apellidos']
    nombres = request.args['nombres']
    labor = request.args['labor']
    telefono = request.args['telefono']
    correo = request.args['correo']
    area = request.args['area']
    oficina = request.args['oficina']

    #image_size = 310, 98
    image_size = 620, 196    
    
    img = Image.new( 'RGBA', image_size)
    
    logo = Image.open('logo.png')
    logo_size = logo.size
    
    correo_icono = Image.open('correo.png')
    telefono_icono = Image.open('telefono.png')
    
    box = 0, 0, logo_size[0], logo_size[1]


    img.paste(logo, box)
    
    text_box_left = logo_size[0]+10
    text_box_top = 10
    font_size = 22
    
    draw = ImageDraw.Draw(img)    
    font = ImageFont.truetype("fonts/ufonts.com_futura-condensed-extrabold.ttf", font_size)
    
    draw.text((text_box_left, text_box_top), titulo.upper() + ' ' + nombres.upper() + ' ' + apellidos.upper(), fill="gray", font=font)
    draw.line((text_box_left, text_box_top + font_size*1.5, 610, text_box_top + font_size*1.5), fill='#711610', width=3)
    
    draw.text((text_box_left, text_box_top + font_size*2), labor, fill='black', font=font)
    draw.text((text_box_left, text_box_top + font_size*3), area, fill='black', font=font)
    draw.text((text_box_left, text_box_top + font_size*4), oficina, fill='black', font=font)
    
    telefono_box = text_box_left, text_box_top + 4 + font_size*5, text_box_left + telefono_icono.size[0], text_box_top + font_size*5 + 4 + telefono_icono.size[1]    
    img.paste(telefono_icono, telefono_box)
    draw.text((text_box_left + telefono_icono.size[0] + 4, text_box_top + font_size*5), u'Teléfono: ' + telefono, fill='black', font=font)
    
    correo_box = text_box_left, text_box_top + 4 + font_size*6, text_box_left + correo_icono.size[0], text_box_top + font_size*6 + 4 + correo_icono.size[1]    
    img.paste(correo_icono, correo_box)
    draw.text((text_box_left + correo_icono.size[0] + 4, text_box_top + font_size*6), u'Correo: ' + correo, fill='black', font=font)
    
    draw.text((text_box_left, text_box_top + font_size*7), u'Av. Túpac Amaru 210, Rímac. Lima - Perú', fill='black', font=font)

    img_io = StringIO()
    img.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
