# -*- coding: utf-8 -*-


from apps import create_app

# instancia função factory em modo 'development'
app = create_app('development')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['PORT']
    debug = app.config['DEBUG']

    
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )