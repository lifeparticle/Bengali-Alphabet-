def encode(list):
    b = [chr(number) for number in list]
    return print(b)

# Vowels (স্বরবর্ণ)
Vowels = [2437, 2438, 2439, 2440, 2441, 2442, 2443, 2447, 2448, 2451, 2452]

# Numbers (সংখ্যা)
Numbers = [2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543]

# Consonants (ব্যঞ্জনবর্ণ)
Consonants = [2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2482, 2486, 2487, 2488, 2489, 2524, 2525, 2527, 2510, 2433, 2434, 2435]

# Vowel Diacritics (কার)
Vowel_Diacritics = [2494, 2495, 2496, 2497, 2498, 2499, 2503, 2504, 2507, 2508]

# Vowels + Numbers + Consonants + Vowel Diacritics
All = [2437, 2438, 2439, 2440, 2441, 2442, 2443, 2447, 2448, 2451, 2452, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2482, 2486, 2487, 2488, 2489, 2524, 2525, 2527, 2510, 2433, 2434, 2435, 2494, 2495, 2496, 2497, 2498, 2499, 2503, 2504, 2507, 2508]

encode(Vowels)
encode(Numbers)
encode(Consonants)
encode(Vowel_Diacritics)
encode(All)
