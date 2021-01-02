import os
import shutil
import time
import sys
import pyautogui
from itertools import islice


pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

RESULTS = 'C:/Users/Przemyslaw/omnet/omnetpp-5.2.1/samples/flora-0.8/simulations/results' 

def get_n_items(d,f,n):
    """
    return sliced dictionary 
    f - means from (first element in the sliced array)
    n - means to (last element in the sliced array) if n exceeds size of array nothing 
    serious happens (last element is treated as n)
    """
    return dict(islice(d.items(),f, n))

def copy_results(dir, scenario, numberOfNodes):
    files = os.listdir(dir)
    foldername = f"{dir}/results/scenario-{scenario}-{numberOfNodes}"
    os.mkdir(foldername)
    for file in files:
        srcpath = f"{dir}/{file}"
        dstpath = f"{foldername}/{file}"
        if os.path.isfile(srcpath):
            shutil.copyfile(srcpath, dstpath)

def gui_interaction():
    run = pyautogui.locateOnScreen('run.png')
    print(run)
    pyautogui.moveTo(run)
    pyautogui.click()
    express = None
    while express is None:
        time.sleep(30)
        express = pyautogui.locateOnScreen('express.png')
    print("launch express")
    pyautogui.moveTo(express)
    pyautogui.click()
    pyautogui.click()
    oklimit = None
    while oklimit is None:
        time.sleep(100)
        oklimit = pyautogui.locateOnScreen('oklimit.png')
    pyautogui.moveTo(oklimit)
    pyautogui.click()
    closesim = pyautogui.locateOnScreen('closesim.png')
    pyautogui.moveTo(closesim)
    pyautogui.hotkey("alt", "f4")
    pyautogui.click()

scenarios = {
    1:
    {
    # obszar sieci 
    "areaX" : 750,
    "areaY" : 750,
    # liczba bramek
    "numberOfGateways" : 1,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 2,
    },
    2:
    {
    # obszar sieci 
    "areaX" : 750,
    "areaY" : 750,
    # liczba bramek
    "numberOfGateways" : 2,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 2,
    },
    3:
    {
    # obszar sieci 
    "areaX" : 750,
    "areaY" : 750,
    # liczba bramek
    "numberOfGateways" : 1,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 5,
    },
    4:
    {
    # obszar sieci 
    "areaX" : 750,
    "areaY" : 750,
    # liczba bramek
    "numberOfGateways" : 2,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 5,
    },
    5:
    {
    # obszar sieci 
    "areaX" : 10000,
    "areaY" : 10000,
    # liczba bramek
    "numberOfGateways" : 1,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 2,
    },
    6:
    {
    # obszar sieci 
    "areaX" : 10000,
    "areaY" : 10000,
    # liczba bramek
    "numberOfGateways" : 2,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 2,
    },
    7:
    {
    # obszar sieci 
    "areaX" : 10000,
    "areaY" : 10000,
    # liczba bramek
    "numberOfGateways" : 1,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 5,
    },
    8:
    {
    # obszar sieci 
    "areaX" : 10000,
    "areaY" : 10000,
    # liczba bramek
    "numberOfGateways" : 2,
    # liczba węzłów
    "numberOfNodes" : [200, 600, 1000],
    # moment rozpoczęcia generowania wiadomości
    "timeToFirstPacket" : 600,
    # interwał z jakim są generowane kolejne pakiety
    "timeToNextPacket" : 100,
    # sigma  w  modelu  LoRaLogNormalShadowing
    "sigma" : 5,
    },
}

# numer seeda ( nr w dzienniku * 7)
seed = 5 * 7 
time.sleep(5)
sliced_scenarios = get_n_items(scenarios, 0, 1)
for scenario in sliced_scenarios:
    areaX = scenarios[scenario]["areaX"]
    areaY = scenarios[scenario]["areaY"]
    numbersOfNodes = scenarios[scenario]["numberOfNodes"]
    numberOfGateways = scenarios[scenario]["numberOfGateways"]
    timeToFirstPacket = scenarios[scenario]["timeToFirstPacket"]
    timeToNextPacket = scenarios[scenario]["timeToNextPacket"]
    sigma = scenarios[scenario]["sigma"]
    
    newGW = ""
    for numberOfNodes in numbersOfNodes[:2]:
        print(f"scenario {scenario} {numberOfNodes}")
        if scenarios[scenario]["numberOfGateways"] == 1:
            numberOfGW = 1
            posX = scenarios[scenario]["areaX"] / 2
            posY = scenarios[scenario]["areaY"] / 2 
        elif scenarios[scenario]["numberOfGateways"] == 2:
            numberOfGW = numberOfNodes / 200
            if numberOfGW == 1:
                posX = scenarios[scenario]["areaX"] / 2
                posY = scenarios[scenario]["areaY"] / 2
            elif numberOfGW == 3:
                posX = scenarios[scenario]["areaX"] / 6
                pos2X = 3 * scenarios[scenario]["areaX"] / 6
                pos3X = 5 * scenarios[scenario]["areaX"] / 6
                posY = scenarios[scenario]["areaY"] / 6
                pos2Y = 3 * scenarios[scenario]["areaY"] / 6
                pos3Y = 5 * scenarios[scenario]["areaY"] / 6
                newGW = f'\n**.loRaGW[2].numUdpApps = 1\n**.loRaGW[2].packetForwarder.localPort = 2000\n**.loRaGW[2].packetForwarder.destPort = 1000\n**.loRaGW[2].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[2].packetForwarder.indexNumber = 2\n**.loRaGW[1].**.initialX = {pos2X}m\n**.loRaGW[1].**.initialY = {pos2Y}m\n**.loRaGW[2].**.initialX = {pos3X}m\n**.loRaGW[2].**.initialY = {pos3Y}m\n'
            elif numberOfGW == 5:
                posX = scenarios[scenario]["areaX"] /10
                pos2X = 3 * scenarios[scenario]["areaX"] / 10
                pos3X = 5 * scenarios[scenario]["areaX"] / 10
                pos4X = 7 * scenarios[scenario]["areaX"] / 10
                pos5X = 9 * scenarios[scenario]["areaX"] / 10
                posY = scenarios[scenario]["areaY"] / 10
                pos2Y = 3 * scenarios[scenario]["areaY"] / 10
                pos3Y = 5 * scenarios[scenario]["areaY"] / 10
                pos4Y = 7 * scenarios[scenario]["areaY"] / 10
                pos5Y = 9 * scenarios[scenario]["areaY"] / 10

                newGW = f'\n**.loRaGW[2].numUdpApps = 1\n**.loRaGW[2].packetForwarder.localPort = 2000\n**.loRaGW[2].packetForwarder.destPort = 1000\n**.loRaGW[2].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[2].packetForwarder.indexNumber = 2\n\n**.loRaGW[3].numUdpApps = 1\n**.loRaGW[3].packetForwarder.localPort = 2000\n**.loRaGW[3].packetForwarder.destPort = 1000\n**.loRaGW[3].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[3].packetForwarder.indexNumber = 3\n**.loRaGW[4].numUdpApps = 1\n**.loRaGW[4].packetForwarder.localPort = 2000\n**.loRaGW[4].packetForwarder.destPort = 1000\n**.loRaGW[4].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[4].packetForwarder.indexNumber = 4\n**.loRaGW[1].**.initialX = {pos2X}m\n**.loRaGW[1].**.initialY = {pos2Y}m\n**.loRaGW[2].**.initialX = {pos3X}m\n**.loRaGW[2].**.initialY = {pos3Y}m\n\n**.loRaGW[3].**.initialX = {pos4X}m\n**.loRaGW[3].**.initialY = {pos4Y}m\n\n**.loRaGW[4].**.initialX = {pos5X}m\n**.loRaGW[4].**.initialY = {pos5Y}m\n'

        loraNetworkTest = f'[General]\nnetwork = LoRaNetworkTest\nrng-class = "cMersenneTwister"\n\n# network features\n**.numberOfGateways = {numberOfGW}\n**.loRaGW[0].numUdpApps = 1\n**.loRaGW[0].packetForwarder.localPort = 2000\n**.loRaGW[0].packetForwarder.destPort = 1000\n**.loRaGW[0].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[0].packetForwarder.indexNumber = 0\n\n**.loRaGW[1].numUdpApps = 1\n**.loRaGW[1].packetForwarder.localPort = 2000\n**.loRaGW[1].packetForwarder.destPort = 1000\n**.loRaGW[1].packetForwarder.destAddresses = "networkServer"\n**.loRaGW[1].packetForwarder.indexNumber = 1\n\n**.networkServer.numUdpApps = 1\n**.networkServer.**.evaluateADRinServer = true\n**.networkServer.udpApp[0].typename = "NetworkServerApp"\n**.networkServer.udpApp[0].destAddresses = "loRaGW[0]"\n**.networkServer.udpApp[0].destPort = 2000\n**.networkServer.udpApp[0].localPort = 1000\n**.networkServer.udpApp[0].adrMethod = ${{"avg"}}\n\n**.numberOfNodes = {numberOfNodes}\n**.numberOfPaketsToSend = 0 #0 means infinite number of packets\nsim-time-limit = 7d\nwarmup-period = 0.5d\nsimtime-resolution = -9\n\n**.timeToFirstPacket = exponential({timeToFirstPacket}s)\n**.timeToNextPacket = exponential({timeToNextPacket}s)\n**.alohaChannelModel = false\n\n#nodes features\n**.loRaNodes[*].**.initFromDisplayString = false\n**.loRaNodes[*].**.evaluateADRinNode = true\n**.loRaNodes[*].**initialLoRaSF = intuniform(7,12)\n**.loRaNodes[*].**initialLoRaBW = 125 kHz\n**.loRaNodes[*].**initialLoRaCR = 1\n**.loRaNodes[*].**initialLoRaTP = (2dBm + 4dBm*intuniform(0, 3))\n\n# deployment of nodes in a circle with radius=maxGatewayDistance and gateway at gatewayX,gatewayY\n#**.loRaNodes[*].deploymentType = "circle"\n#**.loRaNodes[*].maxGatewayDistance = 120.0\n#**.loRaNodes[*].gatewayX = 240\n#**.loRaNodes[*].gatewayY = 240\n\n# random deployment of nodes in a square square area\n**.loRaNodes[*].**.initialX = uniform(0m, {areaX}m)\n**.loRaNodes[*].**.initialY = uniform(0m, {areaY}m)\n\n#gateway features\n**.LoRaGWNic.radio.iAmGateway = true\n**.loRaGW[*].**.initFromDisplayString = false\n**.loRaGW[0].**.initialX = {posX}m\n**.loRaGW[0].**.initialY = {posY}m{newGW}\n\n\n#power consumption features\n**.loRaNodes[*].LoRaNic.radio.energyConsumerType = "LoRaEnergyConsumer"\n**.loRaNodes[*].**.energySourceModule = "IdealEpEnergyStorage"\n**.loRaNodes[*].LoRaNic.radio.energyConsumer.configFile = xmldoc("energyConsumptionParameters.xml")\n\n#general features\n**.sigma = {sigma}\n**.constraintAreaMinX = 0m\n**.constraintAreaMinY = 0m\n**.constraintAreaMinZ = 0m\n**.constraintAreaMaxX = {areaX}m\n**.constraintAreaMaxY = {areaY}m\n**.constraintAreaMaxZ = 0m\n\nLoRaNetworkTest.**.radio.separateTransmissionParts = false\nLoRaNetworkTest.**.radio.separateReceptionParts = false\n\n**.delayer.config = xmldoc("cloudDelays.xml")\n**.radio.radioMediumModule = "LoRaMedium"\n**.LoRaMedium.pathLossType = "LoRaLogNormalShadowing"\n**.minInterferenceTime = 0s\n**.displayAddresses = false\nseed-0-mt = {seed}'
        with open('C:/Users/Przemyslaw/omnet/omnetpp-5.2.1/samples/flora-0.8/simulations/loRaNetworkTest.ini', 'w') as file: 
            file.write(loraNetworkTest)
        
        gui_interaction()
        copy_results(RESULTS, scenario, numberOfNodes)

