from sort_station import polish_notation

assert polish_notation("123 + 456") == "123 456 +",  "Wrong answer"
assert polish_notation("1 + (2 + (3 + (4 + 5)))") == "1 2 3 4 5 + + + +",  "Wrong answer"
assert polish_notation("-- (2 == 3) % 2") == "2 3 == -- 2 %",  "Wrong answer"
assert polish_notation("1 + ! (2 + 4) * 2 + 3") == "1 2 4 + ! 2 * + 3 +",  "Wrong answer"
assert polish_notation("! 1") == "1 !",  "Wrong answer"
assert polish_notation("2 + 4 = 2 * 2 + 3") == "2 4 2 2 * 3 + = +",  "Wrong answer"
assert polish_notation("++ 1 - 2 & 2") == "1 ++ 2 - 2 &",  "Wrong answer"
assert polish_notation("42 || 52") == "42 52 ||",  "Wrong answer"

print("ALL TESTS PASSED :D")
