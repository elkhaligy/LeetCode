def getSmallestString(s: str) -> str:
  s_list = list(s)

  for i in range(0, len(s) - 1):
    if (int(s_list[i]) % 2 == int(s_list[i + 1]) % 2) and s_list[i] > s_list[i + 1]:
      s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
      break

  return ''.join(s_list)



print(getSmallestString(s = "45320"))