import seqlog
import logging
import ftplib
import settings
import subprocess


def run():
    try:
        compress(settings.derivatives_file_path)
        send(settings.derivatives_file_path, settings.derivatives_file_name)

        compress(settings.equities_file_path)
        send(settings.equities_file_path, settings.equities_file_name)
    except Exception as err:
        raise err


def compress(file_path):
    try:
        subprocess.call([file_path])
    except Exception as err:
        raise err


def send(file_path, file_name):
    try:
        session = ftplib.FTP(settings.ftp_uri, settings.ftp_username, settings.ftp_password)
        file_bytes = open(file_path, 'rb')
        session.login()
        session.cwd(settings.ftp_dir)
        session.storbinary('STOR ' + file_name, file_bytes)
        file_bytes.close()
        session.quit()
    except Exception as err:
        raise err


if __name__ == '__main__':
    run()
