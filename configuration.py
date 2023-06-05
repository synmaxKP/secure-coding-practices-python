import stat
import os

def has_secure_permissions(file_path):
    try:
        file_permissions = stat.S_IMODE(os.lstat(file_path).st_mode)
        if file_permissions & stat.S_IRWXG or file_permissions & stat.S_iRWXO:
            return False
        else:
            return True
    except OSError:
        return False


def read_sensitive_file(file_path):
    # Read the contents of a sensitive file
    if has_secure_permissions(file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    else:
        return "Unauthorized Access."

print(read_sensitive_file('/Users/meenalbhansali/Dropbox/Rooms/Course Room/Secure Coding/3-Secure Coding Practices/Secure Coding Practices/secure-authentication.py'))