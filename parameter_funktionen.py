def Parameter(param1, param2, param3):
    
    if None == param1:
        param1 = "Standardwert ist param1"

    if None == param2:
        param2 = 100

    if None == param3:
        param3 = 1, 2, 3

    return param1,param2,param3

print(Parameter(None, None, None))
