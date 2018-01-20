from wsgiref.simple_server import make_server

# def application (environ, start_response):
#
#     # Sorting and stringifying the environment key, value pairs
#     response_body = [
#         '%s: %s' % (key, value) for key, value in sorted(environ.items())
#     ]
#     response_body = '\n'.join(response_body)
#
#     status = '200 OK'
#     response_headers = [
#         ('Content-Type', 'text/plain'),
#         ('Content-Length', str(len(response_body)))
#     ]
#     start_response(status, response_headers)
#
#     return [response_body]
#
# # Instantiate the server
# httpd = make_server (
#     'localhost', # The host name
#     8051, # A port number where to wait for the request
#     application # The application object name, in this case a function
# )
#
# # Wait for a single request, serve it and quit
# httpd.handle_request()

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from WSGI import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()