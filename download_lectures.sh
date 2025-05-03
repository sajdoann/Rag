#!/bin/bash
# download all deep learning lectures
# f.e. 1st lecture from:
# https://lectures.ms.mff.cuni.cz/video/rec/npfl138/2324/npfl138-2324-01-english.mp4

mkdir -p data

for i in $(seq -w 1 14); do
    url="https://lectures.ms.mff.cuni.cz/video/rec/npfl138/2324/npfl138-2324-${i}-english.mp4"
    output="data/npfl138-2324-${i}-english.mp4"
    echo "Downloading lecture $i..."
    wget -q --show-progress "$url" -O "$output"
done
