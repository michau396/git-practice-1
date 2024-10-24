def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    
    if value < 0.9 * threshold:
        return "LOW"
    elif 0.9 * threshold <= value <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "HIGH"

temperature = float(input("Podaj temperature w kelwinach"))
neutrons_produced_per_second = float(input("Podaj liczbe neutronow produkowanych na sekunde"))
threshold = float(input("Podaj prog krytycznosci"))

status = fail_safe(temperature, neutrons_produced_per_second, threshold)
print(f"Stan reaktora: {status}")
