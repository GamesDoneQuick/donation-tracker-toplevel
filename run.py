import subprocess
import os
import shutil

if not os.access('local.py', os.R_OK):
    os.mkdir('db')
    shutil.copy('example_local.py', 'local.py')

cwd = os.getcwd()
if cwd[1] == ':':
    cwd = '//' + cwd[0].lower() + cwd[2:].replace('\\', '/')

subprocess.check_call(['docker', 'build', '-t', 'donation-tracker', '.'])
container = subprocess.check_output(['docker', 'run', '-d',
                                     '-v', cwd + '/tracker:/usr/src/app/tracker:ro',
                                     '-v', cwd + '/tracker_ui/static:/usr/src/app/tracker_ui/static:ro',
                                     '-p', '8080:8080',
                                     'donation-tracker'])
subprocess.check_call(['docker', 'exec', '-d', container.strip(), 'python', 'webpack-dev-server.py'])
