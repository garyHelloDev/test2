import uuid
# 这里获取UUId
def uuid_no():
    id1 = str(uuid.uuid1()).replace("-", '')
    val = int(id1, 16)
    return val

#str="[{"id":207,"key":"SixSecondRule"},{"id":208,"key":"DangerousPlay"},{"id":209,"key":"Hands"},{"id":210,"key":"Obstruction"},{"id":211,"key":"Protest"},{"id":212,"key":"Simulation"},{"id":213,"key":"TimeDelay"},{"id":198,"key":"DisallowedGoal"}]"


print(uuid_no())