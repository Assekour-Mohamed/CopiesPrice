n = int(input("Enter the number of copies: "))

if n < 10:
  p = n * 10
elif n < 20:
  p = 10 * 0.3 + (n - 10) * 0.25
else:
  p = 10 * 0.3 + 10 * 0.25 + (n - 30) * n

return p
