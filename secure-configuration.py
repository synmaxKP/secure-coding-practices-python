import os
import stat


def has_secure_permissions(file_path):
    # Check if the file has secure permissions
    try:
        # Get the file's current permissions
        file_permissions = stat.S_IMODE(os.lstat(file_path).st_mode)

        # Check if the file permissions restrict read access to owner only
        if file_permissions & stat.S_IRWXG or file_permissions & stat.S_IRWXO:
            return False
        else:
            return True
    except OSError:
        return False

def read_sensitive_file(file_path):
    # Check if the file has proper permissions before reading
    if has_secure_permissions(file_path):
        with open(file_path, 'r') as file:
            contents = file.read()

        return contents
    else:
        return "Unauthorized access."

# Usage:
contents = read_sensitive_file(file_path)
print(contents)



