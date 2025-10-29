def find_max_number(num1, num2, num3):
  max_num = 0
  if num1 >= num2:
    max_num
  else:
    max_num = num2
  if num3 >= max_num:
    max_num = num3
  
  return max_num

def find_mean(num1, num2, num3):
  sum = num1 + num2 + num3

  return sum/3

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    data = [num1, num2, num3]
    mean = find_mean(num1, num2, num3)

    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = variance ** 0.5

    return mean, std

