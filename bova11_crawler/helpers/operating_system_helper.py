import os
from shutil import copyfile

if os.name == 'nt':
    import ctypes
    from ctypes import windll, wintypes
    from uuid import UUID

    # ctypes GUID copied from MSDN sample code
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            self.Data1, self.Data2, self.Data3, \
                self.Data4[0], self.Data4[1], rest = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest>>(8-i-1)*8 & 0xff

    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]

    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value

    FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'

    def get_download_folder():
        """
        Returns the Downloads folder for windows os.
        :return: A string representation of the downloads folder.
        """
        return _get_known_folder_path(FOLDERID_Download)
else:
    def get_download_folder():
        """
        Returns the Downloads folder for non-windows os's.
        :return: A string representation of the downloads folder.
        """
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")


def move_file(source, destination):
    """
    Copies the file to the destination path.
    :param source: The source of the downloaded file
    :param destination: The destination folder where the file will be copied to
    :return:
    """
    try:
        copyfile(source, destination)
    except Exception as err:
        raise err


def delete_file(path):
    """
     Deletes the file from downloads folder so that the
     next day's download won't generate the (1) file.
    """
    try:
        os.remove(path)
    except Exception as err:
        raise err
