from test import app
if __name__=="__main__":
    app.run('0.0.0.0',debug=True, port=443, ssl_context=('/root/projects/Nginx/1_bigseriouslee.top_bundle.crt','/root/projects/Nginx/2_bigseriouslee.top.key'))
