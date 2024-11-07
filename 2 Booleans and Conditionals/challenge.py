surface_type = input("Please enter the type for the surface*(example:- carpet, tile, grass):- ")
surface = surface_type.lower()
battery_level = int(input("Please enter the battery level between 0% to 100%:- "))


if surface in ["carpet", "tile", "grass"]:
    if 0 <= battery_level <= 100:
        if surface == "carpet":
            
            if battery_level > 50:
                print("🚨 Carpet detected with high battery. Increasing wheel torque for better traction.")
                
            else:
                print("Carpet detected with moderate or low battery. Maintaining normal wheel torque to conserve energy.")
                
        elif surface == "tile":
            
            if battery_level > 50:
                print("🟢 Tile detected with high battery. Maintaining normal wheel torque.")
                
            elif battery_level > 20:
                print("Tile detected with moderate battery. Maintaining normal wheel torque.")
            else:
                print("Tile detected with low battery. Conserving energy with normal wheel torque.")
        elif surface == "grass":
            if battery_level >= 50:
                print("🟢 Grass detected with sufficient battery. Maintaining normal wheel torque.")
            else:
                print("⚠️ Grass detected with low battery. Decreasing wheel torque to avoid getting stuck.")
    else:
        print("Invalid battery level. Please enter a value between 0 and 100.")
        exit()
else:
    print("Invalid surface type. Please enter carpet, tile, or grass.")
    exit()
