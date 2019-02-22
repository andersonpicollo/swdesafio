# -*- coding: utf-8 -*-

# Apps
from apps import create_app

# instancia nossa função factory criada anteriormente
app = create_app('development')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['PORT']
    debug = app.config['DEBUG']

    # executa o servidor web do flask
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )