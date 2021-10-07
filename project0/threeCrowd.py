crowd = ["jimmer", "jeffrey", "bill", "jah"]
print(crowd)
if len(crowd) > 3:
    print("the room is too crowded")
crowd.pop(2)
crowd.pop(1)
print(crowd)
if len(crowd) > 3:
    print("the room is too crowded")
