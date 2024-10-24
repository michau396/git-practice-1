def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current   
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return "zielony"
    elif 60 <= efficiency < 80:
        return "pomaranczowy"
    elif 30 <= efficiency < 60:
        return "czerwony"
    else:
        return "czarny"
voltage = float(input("Podaj napiecie"))
current = float(input("Podaj natezenie"))
theoretical_max_power = float(input("Podaj maksymalna teoretyczna moc"))

wynik = reactor_efficiency(voltage, current, theoretical_max_power)
print(f"Stan reaktora to kolor: {wynik}")
