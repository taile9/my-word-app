import sys

def get_day_words_full(filepath, day):
    """Returns list of (word, meaning, line_num) for specified day"""
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        parts = line.rstrip('\r\n').split('\t')
        if len(parts) >= 3 and parts[0] == day and parts[1].strip() and parts[2].strip():
            words.append((parts[1].strip(), parts[2].strip(), i+1))
    return words

# Compare day1
d1_full = get_day_words_full('public/data.csv', 'day1')
d2_full = get_day_words_full('public/data2.csv', 'day1')

d1_words = [w[0] for w in d1_full]
d2_words = [w[0] for w in d2_full]

with open('scripts/compare_result.txt', 'w', encoding='utf-8') as f:
    f.write(f'=== data.csv day1 ({len(d1_full)} words) ===\n')
    for word, meaning, linenum in d1_full:
        marker = ' <<MISSING from data2>>' if word not in d2_words else ''
        f.write(f'L{linenum}: {word} | {meaning}{marker}\n')
    
    f.write(f'\n=== data2.csv day1 ({len(d2_full)} words) ===\n')
    for word, meaning, linenum in d2_full:
        marker = ' <<EXTRA not in data1>>' if word not in d1_words else ''
        f.write(f'L{linenum}: {word} | {meaning}{marker}\n')
    
    missing = [(w, m, l) for w, m, l in d1_full if w not in d2_words]
    extra = [(w, m, l) for w, m, l in d2_full if w not in d1_words]
    
    f.write(f'\n=== MISSING in data2.csv ({len(missing)}) ===\n')
    for word, meaning, linenum in missing:
        f.write(f'  - {word} | {meaning} (data.csv L{linenum})\n')
    
    f.write(f'\n=== EXTRA in data2.csv ({len(extra)}) ===\n')
    for word, meaning, linenum in extra:
        f.write(f'  - {word} | {meaning} (data2.csv L{linenum})\n')

print("Done! Check scripts/compare_result.txt")
