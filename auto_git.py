import subprocess
import os
command = [
    'git add ',
    'git commit -m ',
    'git push origin '
]
def print_stdout_err(result):
    print(result.stdout)
    print(result.stderr)
def auto_push(update_content = '更新文档', repositorty = 'main'):
    abs_filepath = os.path.abspath(__file__)
    rel_filepath = os.path.relpath(abs_filepath)
    result_add = subprocess.run(command[0] + rel_filepath,capture_output=True,text=True)
    print_stdout_err(result_add)
    result_commit = subprocess.run(command[1] + update_content,capture_output=True  ,text=True)
    print_stdout_err(result_commit)
    result_push  = subprocess.run(command[2] + repositorty,capture_output=True,text=True)
    print_stdout_err(result_push)

