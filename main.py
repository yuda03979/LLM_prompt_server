# import http.server
# import socketserver
# import webbrowser
#
# PORT = 8000
#
# # Define the handler to serve files from the current directory
# Handler = http.server.SimpleHTTPRequestHandler
#
# # Open the browser automatically
# webbrowser.open(f'http://localhost:{PORT}')
#
# # Create the server
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Serving at http://localhost:{PORT}")
#     httpd.serve_forever()
#
from app import *
app.run(host="0.0.0.0", port=8000, debug=True)