def swap_case(string):
  site_string = ''
  for s in string:
    if s.isupper():
      site_string += s.lower()
    else:
      site_string += s.upper()
  return site_string

print(swap_case("dAVIDsTARDUST"))
