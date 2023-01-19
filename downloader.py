import ftplib
import requests

class Downloader:
    def __init__(self):
        pass
    def download_from_ftp(self, server, username, password, file_path, local_path):
        ftp = ftplib.FTP(server)
        ftp.login(username, password)
        ftp.cwd(file_path)
        ftp.retrbinary("RETR " + file_path, open(local_path, 'wb').write)
        ftp.quit()
        print("File downloaded successfully from ftp")
        
    def download_from_http(self, url, local_path):
        response = requests.get(url)
        open(local_path, "wb").write(response.content)
        print("File downloaded successfully from http")
