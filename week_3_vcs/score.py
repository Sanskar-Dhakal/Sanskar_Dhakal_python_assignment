def average_score(*marks):
    if len(marks) == 0:
        return "No marks provided."

    average = sum(marks) / len(marks)
    return average

print(average_score(80, 90, 70))           
print(average_score(85, 95, 90, 100))      
print(average_score(75))                   
print(average_score())                     