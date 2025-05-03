#!/bin/bash

module add python/3.10.4-gcc
module add ffmpeg

# 👀 UNCOMMENT THIS FOR 1st time (setting up venv)
#  # Set up virtualenvs directory if it doesn't exist
#  #mkdir -p ~/.virtualenvs
#
#  python3 -m venv ~/.virtualenvs/whisper_env


# Activate the environment
source ~/.virtualenvs/whisper_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Whisper and dependencies
pip install git+https://github.com/openai/whisper.git

# Optional: Install CUDA-enabled torch if you're on GPU node
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



# Done
echo "✅ Whisper environment setup complete. Run: source ~/.virtualenvs/whisper_env/bin/activate"
