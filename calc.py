# Ask for your height and weight
# height = input("What is your height in inches?")
# weight = input("What is your weight in pounds?")
# gender = input("What is your gender?")

#height, weight : size
girls_shirt_size = {
    ("5'2", 53): "small",
    ("5'5", 69): "small",
    ("5'6", 70): "medium",
    ("5'9", 84): "medium",
    ("5'10", 85): "large",
    ("6'0", 99): "large"
}

def height_to_inches(height):
    return (int(height.split("'")[0])*6) + int(height.split("'")[1])

def size(height, weight, gender):
    height = height_to_inches(height)
    for i in girls_shirt_size:
        for j in girls_shirt_size:
            if (height_to_inches(i[0]) <= height) and (i[1] <= weight) and (height_to_inches(j[0]) > height) and (j[1] > weight):
                return girls_shirt_size[j]



print(size("5'3", 60, "female"))
