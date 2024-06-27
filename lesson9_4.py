from fuzzywuzzy import fuzz

res = fuzz.ratio('Лак ПФ-238', 'ПФ-238 (лак)')
res = fuzz.token_set_ratio('Лак ПФ-238', 'ПФ-238 (лак)')
res = fuzz.token_sort_ratio('Лак ПФ-238', 'ПФ-238 (лак)')
res = fuzz.WRatio('Лак ПФ-238', 'ПФ-238 (лак)')

print(res)
