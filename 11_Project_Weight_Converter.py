weight_lbs = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':                                 #case sensitive to 'L'
    converted = weight_lbs * 0.45
    print(f'You are {converted} kilograms')

else:
    converted = weight_lbs / 0.45                      # '//' returns int, '/' returns float
    print(f'You are {converted} pounds')



