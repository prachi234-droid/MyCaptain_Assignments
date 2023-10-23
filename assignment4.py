def most_frequent(str1):
  
  dict = {}
  for n in str1:
    keys = dict.keys()
    if n in keys:
      dict[n] += 1
    else:
      dict[n] = 1

  sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
  for key, value in sorted_dict:
    print(key, value)

str1 = "mississippi"
most_frequent(str1)
