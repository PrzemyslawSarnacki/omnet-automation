import os
import subprocess

RESULTS = "/mnt/c/Users/Przemyslaw/omnet/omnetpp-5.2.1/samples/flora-0.8/simulations/results/results"

for directory in os.listdir(RESULTS):
    inner_dir = f"{RESULTS}/{directory}"
    print(inner_dir)
    os.chdir(inner_dir)
    bashCommand = "scavetool x *.sca -o measurements.csv"
    process = subprocess.run(bashCommand, shell=True)
