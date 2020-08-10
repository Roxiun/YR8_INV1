reference_numbers = {"1":{"Lighting":"Dusk","Iso":"50","Shutter":"1/4000","Aperture":"22"},"2":{"Lighting":"Sunset/Shade","Iso":"100","Shutter":"1/2000","Aperture":"16"},"3":{"Lighting":"Overcast","Iso":"200","Shutter":"1/1000","Aperture":"11"},"4":{"Lighting":"Cloudy","Iso":"400","Shutter":"1/500","Aperture":"8"},"5":{"Lighting":"Lightly Cloudy","Iso":"800","Shutter":"1/250","Aperture":"5.6"},"6":{"Lighting":"Sunny","Iso":"1600","Shutter":"1/125","Aperture":"4"},"7":{"Lighting":"Snow/Sand","Iso":"3200","Shutter":"1/60","Aperture":"2"},"8":{"Lighting":"-","Iso":"6400","Shutter":"1/30","Aperture":"2"}}
# Creates a dictionary that holds all the reference Numbers
all_inputs = ["lighting", "iso", "shutter", "aperture"]
# Creates a list with all the inputs the user can enter
def getResult(UserDict):
	A=UserDict;B={}
	for C in A:B[C]=getReferenceValue(A[C])
	return B
def getReferenceValue(UserInput):
    for number in reference_numbers: 
        for value in reference_numbers[number]:
            if reference_numbers[number][value] == UserInput:
                return int(number)
# Creates some functions to find the reference numbers
user_selected = input("Enter that setting you want the program to recommend: ")
while not user_selected.lower().replace("lighting condition", "lighting").replace("shutter speed", "shutter") in all_inputs:
    print("Thats not a valid condition")
    user_selected = input("Enter that setting you want the program to recommend: ") 
    # Makes sure the user inputs a valid input
inputs = {} # Creates a dictionary for the inputs
for item in all_inputs:
    if item == user_selected.lower().replace("lighting condition", "lighting").replace("shutter speed", "shutter"):
        pass # Dont ask for the setting the user is asking to recommend
    else:
        isValid = False
        while not isValid:
            user_in = input(f"Enter your selected setting for {item.title()}: ")
            user_in = user_in.title().replace("F/" ,"").replace(".0", "")
            isValid = any(user_in in d.values() for d in reference_numbers.values())
        inputs[item] = user_in
        # Keep looping until a valid input is provided
res = getResult(inputs)
# Gets refence numbers of the inputs
req_ref = 16 - sum(res.values())
# Subtracts the sum of the reference numbers from 16 (Sunny 16 Rule) to get the last reference number
if req_ref > 0 and req_ref <= 8: print(f"Required {user_selected} Value: {reference_numbers[str(req_ref)][user_selected.lower().replace('lighting condition', 'lighting').replace('shutter speed', 'shutter').title()]}")
elif req_ref < 0: print(f"Too Bright - Change of {(req_ref - 1)*(-1)} stops is required")
elif req_ref > 8: print(f"Too Dark - Change of {req_ref - 8} stops is required")
elif req_ref == 0: print(f"You need to change you settings by at least 1 stop")
