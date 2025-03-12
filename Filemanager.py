import os

def add_file(filename, content=""):
    
    with open(filename, "w") as file:
        file.write(content)
    return f"File '{filename}' created successfully."

def delete_file(filename):
    
    if os.path.exists(filename):
        os.remove(filename)
        return f"File '{filename}' deleted successfully."
    return "File not found."

def open_file(filename):
    
    if os.path.exists(filename):
        os.system(f"start {filename}")
        return f"Opening '{filename}'"
    return "File not found."