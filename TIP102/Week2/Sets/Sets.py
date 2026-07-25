students_A = {"Alice", "Bob", "Charlie"}
students_B = {"Bob", "Charlie", "David"}

union = students_A | students_B
intersect = students_A & students_B
diffA = students_A - students_B
diffB = students_B - students_A
symmDiff = students_A ^ students_B

# Lists in Python are O(N) lookup, while Sets are Constant Time (Hashing)

print(f"\n{union}\n{intersect}\n{diffA}\n{diffB}\n{symmDiff}")
