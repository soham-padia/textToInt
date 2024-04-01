import re

english={
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9, # also decimal till here
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'lac': 100000,
    'lakh': 100000,
    'crore': 10000000,
    'million': 1000000,
    'billion': 1000000000,
    'point': '.',
}


# INPUT:
# A researcher interviewed 2067 people and asked whether they were the primary decision makers in the household 
# when buying a new car last year. Two hundred seven were men and had bought a new car last year. Sixty-five were 
# women and had bought a new car last year. Eight hundred eleven of the responses were from men who did not buy 
# a car last year. Nine hundred eighty-four were from women who did not buy a car last year. Use these data to 
# determine whether gender is independent of being a major decision maker in purchasing a car last year. Let 
# a = .05.

# RETURN:
# A researcher interviewed 2067 people and asked whether they were the primary decision makers in the household 
# when buying a new car last year. 207 were men and had bought a new car last year. 65 were 
# women and had bought a new car last year. 811 of the responses were from men who did not buy 
# a car last year. 984 were from women who did not buy a car last year. Use these data to 
# determine whether gender is independent of being a major decision maker in purchasing a car last year. Let 
# a = .05.


def text_to_number(text):
    def convert_number_phrase_to_number(match):
        # Split the matched phrase into components, accounting for both spaces, hyphens, and the word "point" for decimals
        parts = re.split(r'[\s-]+', match.group(0).lower())
        
        num = 0
        current = 0
        decimal_mode = False  # Indicates if we're processing the decimal part
        decimal_fraction = 0.0
        decimal_place = 1
        
        for part in parts:
            if part == 'point':
                decimal_mode = True  # Switch to processing decimal part
                num += current  # Add what we've accumulated so far as the integer part
                current = 0  # Reset current for decimal processing
                continue
            
            value = english.get(part, None)
            
            if value is not None:
                if decimal_mode:
                    # For decimal parts, accumulate as a fraction
                    decimal_fraction += value * (10 ** (-decimal_place))
                    decimal_place += 1
                else:
                    # For integer parts, process normally
                    if value < 100:
                        current += value
                    else:
                        if current == 0:
                            current = 1
                        num += current * value
                        current = 0
                        
        num += current  # Add any remaining integer part
        num += decimal_fraction  # Add the decimal fraction part
        
        return str(int(num)) if decimal_fraction == 0 else str(num)


    # Enhance the pattern to potentially match decimal expressions
    pattern = r'\b(' + '|'.join(english.keys()) + r'|\bpoint\b)(?:[\s-]+(' + '|'.join(english.keys()) + r'|\bpoint\b))*\b'
    regex = re.compile(pattern, re.IGNORECASE)

    new_text = regex.sub(convert_number_phrase_to_number, text)
    return new_text

# text = """
# A researcher interviewed two thousand sixty-seven people and asked whether they were the primary decision makers in the household when buying a new car last year. Two hundred seven were men and had bought a new car last year. Sixty-five were women and had bought a new car last year. Eight hundred eleven of the responses were from men who did not buy a car last year. Nine hundred eighty-four were from women who did not buy a car last year. Use these data to determine whether gender is independent of being a major decision maker in purchasing a car last year. Let a = point zero five.
# """
# converted_text = text_to_int(text)
# print(text)
# print(converted_text)