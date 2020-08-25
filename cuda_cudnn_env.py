import os

def set_cuda_env(framework='tensorflow'):
	cuda_version = "v10.1"

	if framework == 'tensorflow':
		cuda_version = "v10.1"
		os.environ['PATH'] = os.environ['PATH'].replace("v10.0", "v10.1")

		if "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\bin" not in os.environ['PATH']:
			os.environ['PATH'] += "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\bin;"
		if "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\libnvvp" not in os.environ['PATH']:
			os.environ['PATH'] += "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\libnvvp;"

	elif framework == 'paddlepaddle':
		os.environ['PATH'] = os.environ['PATH'].replace("v10.1", "v10.0")
		cuda_version = "v10.0"

		if "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\bin" not in os.environ['PATH']:
			os.environ['PATH'] += "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\bin;"
		if "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\libnvvp" not in os.environ['PATH']:
			os.environ['PATH'] += "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.0\\libnvvp;"


	os.environ.update()

if __name__ == '__main__':
    set_cuda_env()
