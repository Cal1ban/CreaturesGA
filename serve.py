import subprocess

subprocess.Popen('python3 kafka_stream.py', cwd=r'Mapping/EndPoints')
subprocess.Popen('python3 kafka_stream.py', cwd=r'People/Storage')
