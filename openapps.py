import subprocess

def open_application(app_name):
    
    apps = {
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }
    if app_name in apps:
        subprocess.Popen(apps[app_name])
        return f"Opening {app_name}"
    return "Application not supported."