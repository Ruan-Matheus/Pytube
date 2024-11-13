Pytube is necessary

In /pytube/cypher.py replace:

var_regex = re.compile(r"^[\w\$_]+\W")

And in get_throttling_function_name in function patterns:

r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)'

https://github.com/pytube/pytube/issues/1707
https://github.com/pytube/pytube/issues/1918
