status = 0

# tax for single
if status == 0:
    print("single")
elif status == 1:
    print("married filling Jointly or Qualified Widow(er)")
elif status == 2:
    print("Married Filling Separately")
else:
    print("Head of HouseHold")