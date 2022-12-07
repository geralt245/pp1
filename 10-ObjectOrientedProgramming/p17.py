from thermometer import Thermometer

thermo = Thermometer()
thermo.turn_on()
thermo.measure()
print(thermo.display_temp())
thermo.turn_off()
