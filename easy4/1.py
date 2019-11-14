def short_long_short(string1, string2):
	short_str, long_str = sorted([string1, string2], key = len)
	return short_str + long_str + short_str

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")