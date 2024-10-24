def is_criticality_balanced(temperature, neutrons):
    if temperature < 800 and neutrons> 500 and (temperature * neutrons) < 500000:
        return True
    else:
        return False
temperature = float(input("Podaj temperature w kelwinach"))
neutrons = float(input("Podaj liczbe  emitowanych neutronow na sekunde"))

if is_criticality_balanced(temperature, neutrons):
    print("Reaktor w stanie krytycznym")
else:
    print("Reaktor nie jest w stanie krytycznym")
