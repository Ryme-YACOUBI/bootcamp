print("Print a text :")

ch1 = input()
ch = ch1.lower()

count = 0

ecarts = {
    "french": 0,
    "english": 0,
    "spanish": 0,
    "german": 0
}

french = {
    'a': 7.6368, 'b': 0.9015, 'c': 3.2601, 'd': 3.6690, 'e': 14.7157,
    'f': 1.0667, 'g': 0.8665, 'h': 0.7370, 'i': 7.5297, 'j': 0.6132,
    'k': 0.0490, 'l': 5.4560, 'm': 2.9680, 'n': 7.0952, 'o': 5.7961,
    'p': 2.5211, 'q': 1.3620, 'r': 6.6938, 's': 7.9480, 't': 7.2440,
    'u': 6.3110, 'v': 1.8380, 'w': 0.0490, 'x': 0.4270, 'y': 0.1280,
    'z': 0.3260
}

english = {
    'a': 8.1670, 'b': 1.4920, 'c': 2.7820, 'd': 4.2530, 'e': 12.7020,
    'f': 2.2280, 'g': 2.0150, 'h': 6.0940, 'i': 6.9660, 'j': 0.1530,
    'k': 0.7720, 'l': 4.0250, 'm': 2.4060, 'n': 6.7490, 'o': 7.5070,
    'p': 1.9290, 'q': 0.0950, 'r': 5.9870, 's': 6.3270, 't': 9.0560,
    'u': 2.7580, 'v': 0.9780, 'w': 2.3600, 'x': 0.1500, 'y': 1.9740,
    'z': 0.0740
}

spanish = {
    'a': 12.5250, 'b': 1.4220, 'c': 4.3870, 'd': 5.4110, 'e': 13.6800,
    'f': 0.6920, 'g': 1.0290, 'h': 0.7030, 'i': 6.2470, 'j': 0.4930,
    'k': 0.0110, 'l': 4.9670, 'm': 3.1570, 'n': 6.7120, 'o': 8.6830,
    'p': 2.5100, 'q': 0.8770, 'r': 6.8710, 's': 7.9770, 't': 4.6320,
    'u': 3.9270, 'v': 1.1130, 'w': 0.0170, 'x': 0.2150, 'y': 1.0080,
    'z': 0.4670
}

german = {
    'a': 6.5160, 'b': 1.8860, 'c': 2.7320, 'd': 5.0760, 'e': 17.3960,
    'f': 1.6560, 'g': 3.0090, 'h': 4.5770, 'i': 7.5500, 'j': 0.2680,
    'k': 1.4170, 'l': 3.4370, 'm': 2.5340, 'n': 9.7760, 'o': 2.5940,
    'p': 0.6700, 'q': 0.0180, 'r': 7.0030, 's': 7.2700, 't': 6.1540,
    'u': 4.3460, 'v': 0.8460, 'w': 1.9210, 'x': 0.0340, 'y': 0.0390,
    'z': 1.1340
}

mon_dic = {}

for i in range(0, len(ch)):

    if ch[i] >= 'a' and ch[i] <= 'z' and ch[i] not in mon_dic:
        mon_dic[ch[i]] = 0

    if ch[i] in mon_dic:
        mon_dic[ch[i]] += 1

    if ch[i] >= 'a' and ch[i] <= 'z':
        count += 1

for couple in mon_dic:
    mon_dic[couple] = mon_dic[couple] / count * 100

for couple in mon_dic:

    if couple in french:
        ecarts["french"] += abs(mon_dic[couple] - french[couple])

    if couple in english:
        ecarts["english"] += abs(mon_dic[couple] - english[couple])

    if couple in spanish:
        ecarts["spanish"] += abs(mon_dic[couple] - spanish[couple])

    if couple in german:
        ecarts["german"] += abs(mon_dic[couple] - german[couple])

min_ecart = min(ecarts.values())

for valeurs in ecarts:

    if ecarts[valeurs] == min_ecart:
        print(valeurs)
