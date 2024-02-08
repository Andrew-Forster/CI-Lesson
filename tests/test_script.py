import subprocess
import sys

def test_script_output(capfd):

    subprocess.run([sys.executable, './script.py'])

    captured = capfd.readouterr()
    
    assert captured.out == "Hello, World!\r\n"