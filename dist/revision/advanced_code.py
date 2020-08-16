reference_numbers = {"1":{"Lighting":"Dusk","Iso":"50","Shutter":"1/4000","Aperture":"22"},"2":{"Lighting":"Sunset/Shade","Iso":"100","Shutter":"1/2000","Aperture":"16"},"3":{"Lighting":"Overcast","Iso":"200","Shutter":"1/1000","Aperture":"11"},"4":{"Lighting":"Cloudy","Iso":"400","Shutter":"1/500","Aperture":"8"},"5":{"Lighting":"Lightly Cloudy","Iso":"800","Shutter":"1/250","Aperture":"5.6"},"6":{"Lighting":"Sunny","Iso":"1600","Shutter":"1/125","Aperture":"4"},"7":{"Lighting":"Snow/Sand","Iso":"3200","Shutter":"1/60","Aperture":"2.8"},"8":{"Lighting":"-","Iso":"6400","Shutter":"1/30","Aperture":"2"}}; all_inputs = ["lighting", "iso", "shutter", "aperture"]; inputs = {}; inputs_aliases = {"lighting":"Lighting Condtion" ,"iso":"ISO", "aperture":"Aperture", "shutter":"Shutter Speed"}; modes = ["regular", "automatic", 'semi', "semi-automatic", "semi automatic", "auto"]; modes_aliases = {"regular":"regular","automatic":"automatic", "auto":'automatic', "semi-automatic":"semi", "semi automatic": "semi", "semi":"semi"}; selected_mode = ""; semi_modes = ["portrait", "landscape"]; semi_select = "" # Creates a dictionary for the inputs ## Creates a dictionary that holds all the reference Numbers & Creates a list with all the inputs the user can enter
def getResult(UserDict):
	A=UserDict;B={}
	for C in A:B[C]=getReferenceValue(A[C])
	return B
def getReferenceValue(UserInput):
    for number in reference_numbers: 
        for value in reference_numbers[number]:
            if reference_numbers[number][value] == UserInput: return int(number) # Creates some functions to find the reference numbers
while not selected_mode.lower() in modes: selected_mode = input("What mode would you like? Regular, Automatic or Semi-Automatic: ").lower()
if modes_aliases[selected_mode.lower()] == "regular" or modes_aliases[selected_mode.lower()] == "automatic":
    user_selected = input("Enter that setting you want the program to recommend: ")
    while not user_selected.lower().replace("lighting condition", "lighting").replace("shutter speed", "shutter") in all_inputs: print("Thats not a valid condition"); user_selected = input("Enter that setting you want the program to recommend: ")  # Makes sure the user inputs a valid input
    for item in all_inputs:
        if item == user_selected.lower().replace("lighting condition", "lighting").replace("shutter speed", "shutter"): pass # Dont ask for the setting the user is asking to recommend
        else:
            isValid = False
            while not isValid:
                user_in = input(f"Enter your selected setting for {inputs_aliases[item.lower()]}: "); user_in = user_in.title().replace("F/" ,"").replace(".0", ""); isValid = any(user_in in d.values() for d in reference_numbers.values())
            inputs[item] = user_in # Keep looping until a valid input is provided
    res = getResult(inputs); req_ref = 16 - sum(res.values())  ## Subtracts the sum of the reference numbers from 16 (Sunny 16 Rule) to get the last reference number Gets refence numbers of the inputs
    if modes_aliases[selected_mode.lower()] == "regular" :
        if req_ref > 0 and req_ref <= 8: print(f"Required {inputs_aliases[user_selected.lower()]} Value: {reference_numbers[str(req_ref)][user_selected.lower().replace('lighting condition', 'lighting').replace('shutter speed', 'shutter').title()]}")
        elif req_ref < 0: print(f"Too Bright - Change of {(req_ref - 1)*(-1)} stops is required")
        elif req_ref > 8: print(f"Too Dark - Change of {req_ref - 8} stops is required")
        elif req_ref == 0: print(f"You need to change you settings by at least 1 stop")
    else:
        res[user_selected.lower().replace("lighting condition", "lighting").replace("shutter speed", "shutter")] = req_ref
        while not semi_select in semi_modes: semi_select = input("Which Automatic Mode do you want (Portrait or Sports): ").lower()
        if semi_select == "portrait": res['iso'] = res['iso']-4; res['aperture'] = res['aperture']+4
        else: res['iso'] = res['iso']+1; res['aperture'] = res['aperture']+1; res['shutter'] = res['shutter']-1
        exec("""\ntry:\n    for result in res: print(f"Required {inputs_aliases[result.lower()]} value of: {reference_numbers[str(res[result])][result.title()]}")\nexcept:\n    print(f"Invalid Setting for {inputs_aliases[result.lower()]} was entered")\n""")
else: print("Semi-Automatic not dont yet sorry! :(")