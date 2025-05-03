
module add python/3.10.4-gcc
module add ffmpeg

python3 -m venv /storage/brno11-elixir/home/sajdokova/.virtualenvs/whisper_env --without-pip
# Activate the environment
source /storage/brno11-elixir/home/sajdokova/.virtualenvs/whisper_env/bin/activate

# Download get-pip.py
curl -O https://bootstrap.pypa.io/get-pip.py

# Install pip manually
python get-pip.py

#source /storage/brno11-elixir/home/sajdokova/.virtualenvs/whisper_env/bin/activate
#pip install --upgrade pip
#
## Install Whisper and dependencies
#pip install git+https://github.com/openai/whisper.git
