previous=float(input("enter the previous meter reading: "))
Current=float(input("enter the current meter reading: "))
cost_perunit=float(input("enter the cost per unit: "))
service_charge=30
unit_consumed=Current-previous
payable_cost=unit_consumed*cost_perunit+service_charge
print("The total payable cost is: ", payable_cost)