import decimal
# import the library "decimal"
# display 2 decimal precision

print (round(3.1415, 2)) # result 3.14
print (round(9.995, 2)) # result 9.99

# call function "Decimal" from lib "Decimal"
print (decimal.Decimal(9.995)) # The last "print" returns the exact number which is exactly how 9.995 is stored in the hardware
