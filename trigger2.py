import os

def create_file(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)

create_file("/etc/password", "root:x:0:0:root:/root:/bin/bash")
