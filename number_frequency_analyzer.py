def number_frequency_analyzer():

  try:

    numbers = [int(num.strip()) for num in input("Enter numbers separated by commas: ").split(",")]
  except ValueError:
    print("Invalid input! Please enter only numbers separated by commas.")
    return


  dict_freq ={}
  for num in  numbers:
    if num in dict_freq:
      dict_freq[num] += 1
    else:
       dict_freq[num] = 1

  print("Frequency:")
 
  for num,count in sorted(dict_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{num} --> {count} time{'s' if count >1 else''}")

#for num,count in dict_freq.items():
    # print(num, "->", count, "time" if count==1 else "times")
        # or
#    if count==1:
#      print(f"{num} --> {count} time ")
#    else:
#      print(f"{num} --> {count} times ")

  max_freqency=max(dict_freq.values())
  min_frequency=min(dict_freq.values())

  most_frequent = []
  least_frequent = []

  for num, count in dict_freq.items():
     if count == max_freqency:
        most_frequent.append(str(num))
     if count == min_frequency:
        least_frequent.append(str(num))

  print("Most Frequent:", ', '.join(most_frequent))
  print("Least frquent: ", ','.join(least_frequent))
  print("Total Unique Numbers:", len(dict_freq))



while True:
 number_frequency_analyzer()
 choice = input("Do you want to continue(y/n):").lower()
 if choice != 'y':
    print("Program ended")
    break
  

