# Ask for your height and weight
# height = input("What is your height in inches?")
# weight = input("What is your weight in pounds?")
# gender = input("What is your gender?")

# https://www.kohls.com/media/digital/ecom/size-charts/costumes/Costumes135.htm 
#height, weight : size
girls_shirt_size = {
    ("5'0", 100): "small",
    ("5'3", 120): "small",
    ("5'6", 135): "medium",
    ("5'8", 150): "medium",
    ("5'10", 160): "large",
    ("5'11", 170): "large"
}

def height_to_inches(height):
    return (int(height.split("'")[0])*12) + int(height.split("'")[1])

# def size(height, weight, gender):
#     height = height_to_inches(height)
#     for i in girls_shirt_size:
#         for j in girls_shirt_size:
#             if (height_to_inches(i[0]) <= height) and (i[1] <= weight) and (height_to_inches(j[0]) > height) and (j[1] > weight):
#                 return girls_shirt_size[j]

def size(height, weight, gender):
    height = height_to_inches(height)
    for i in girls_shirt_size:
        if (height_to_inches(i[0]) <= height) and (i[1] <= weight) and (height_to_inches(i[0]) + 3 > height) and (i[1] + 16 > weight):
            return girls_shirt_size[i]


print(size("5'7", 80, "female"))
