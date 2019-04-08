import os.path
import sys
import subprocess


DIR_HERE = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
DIR_PYTHON_MONOLITH = os.path.normpath(os.path.join(DIR_HERE, 'cpython2/build/monolith'))


# Lastest version of prebuilt binary can be downloaded from https://github.com/minibuild/minibuild/releases
MINIBUILD_EXECUTABLE = 'minibuild.exe' if sys.platform == 'win32' else 'minibuild'

if __name__ == '__main__':
    subprocess.check_call([MINIBUILD_EXECUTABLE, '--public', '--model', 'native', '--config', 'release', '--directory', DIR_PYTHON_MONOLITH, '--public-format', 'zip', '--public-layout', 'flat'])
