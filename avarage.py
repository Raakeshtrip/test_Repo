def avarage(numbers):
   total=  len(numbers)
   numinator=0.0
   for number in numbers:
        numinator +=number
   return numinator/total

print(avarage([10,11,12,13]))