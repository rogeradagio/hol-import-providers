from downloader import Downloader

download = Downloader()

@app.route('/download', methods=['POST'])
def download_file():
    protocol = request.form['protocol']
    if protocol == 'ftp':
        server = request.form['server']
        username = request.form['username']
        password = request.form['password']
        file_path = request.form['file_path']
        local_path = request.form['local_path']
        download.download_from_ftp(server, username, password, file_path, local_path)
    else:
        url = request.form['url']
        local_path = request.form['local_path']
        download.download_from_http(url, local_path)
