#encryption code
# Jordan Adriano
# jan 9 2020

orginal= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"," "]
rot_15 = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "1", "2", "3", "4", "5", "6", "7", "8", "9"," "]



info="this is information that need to be encrypted use any means but do not show anybody"
new_info=""


for x in (range(len(info))): #range of the array orginal
   position = x
   letter = info[x]

   letter_position_in_orginal= (orginal.index(letter))

   
