def volumeKerucut(valueDiameter, valueTinggi):
    x = valueDiameter
    y = valueTinggi
    diameterToJarijari = x/2
    z = diameterToJarijari

    hasilVolume = 1/3*3.14*z**2*y

    return hasilVolume

print(volumeKerucut(5, 4))