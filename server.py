# -*- coding: utf-8 -*-
import os
import socket

from flask import Flask, render_template


app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), 'static'),
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_url_path=''
)
PORT = 5556

def get_url_path(base, root, name):
    '''get url path'''
    full_path = os.path.join(root, name)
    return full_path[len(base):].replace('\\', '/').lstrip('/')

def get_file_list(static_folder):
    '''get file list in static folder'''
    exclude = ['favicon.ico', 'favicon.png', 'robots.txt']
    ret_list = []
    for root, dirs, files in os.walk(static_folder):
        for name in files:
            if name not in exclude:
                url_path = get_url_path(static_folder, root, name)
                ret_list.append(url_path)
    return ret_list

@app.route('/cdn')
def view_cdn():
    lan_ip = socket.gethostbyname(socket.gethostname())
    url_base = 'http://{0}:{1}'.format(lan_ip, PORT)
    file_list = get_file_list(app.static_folder)
    # file_list = sorted(file_list, reverse=False)
    return render_template('cdn.html', url_base=url_base, file_list=file_list)

if __name__ == '__main__':
    cfg = dict(
        port=PORT,
        host='0.0.0.0',
        debug=True,
        threaded=True
    )
    app.run(**cfg)