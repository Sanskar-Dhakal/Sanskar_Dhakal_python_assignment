earnings=float(input("enter the earnings: "))
exchange_rate=float(input("enter the exchange rate: "))
servicecharge=float(input("enter the service charge: "))
nrp=earnings*exchange_rate
nrp_received=nrp-servicecharge*nrp
print("The amount received in NRP is: ", nrp_received)
