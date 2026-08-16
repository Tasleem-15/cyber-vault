marks={"alice":80,"bob":70,"charlie":90}
highest=0
topper=""
total=0
for name in marks:
    if marks[name]>highest:
        highest=marks[name]
        topper=name
    total+=marks[name]
result=total/len(marks)
print("topper : ",topper,highest)
print("avg marks: ",result)