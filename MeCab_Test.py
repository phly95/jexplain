import MeCab
import re
import random

def katakana_to_hiragana(katakana):
    """Convert katakana to hiragana."""
    hiragana = ''
    for char in katakana:
        code = ord(char)
        if 0x30A1 <= code <= 0x30F6:
            hiragana += chr(code - 0x60)
        else:
            hiragana += char
    return hiragana

def get_furigana(sentence):
    # Remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Initialize MeCab
    mecab = MeCab.Tagger()

    # Parse the sentence
    parsed = mecab.parse(sentence)

    # Split the parsed output into lines
    lines = parsed.split('\n')

    # Initialize a list to store the results
    results = []

    # Iterate through the lines
    for line in lines:
        if line == 'EOS' or line == '':
            continue

        # Split the line into components
        components = line.split('\t')
        if len(components) < 2:
            continue

        word = components[0]
        features = components[1].split(',')

        if len(features) < 8:
            continue

        # Extract the furigana
        furigana = features[7]

        # Convert furigana from katakana to hiragana
        furigana = katakana_to_hiragana(furigana)

        # Append the result to the list
        results.append((word, furigana))

    return results

def print_furigana(results):
    # Shuffle the results
    random.shuffle(results)

    for word, furigana in results:
        print(f"Word: {word}")
        print(f"- {word}【{furigana}】\n")

if __name__ == "__main__":
    sentence = "この存在は太古の昔に葬られており、今は知る者もほとんどいません。"
    results = get_furigana(sentence)
    print_furigana(results)



### This is an example of a prompt that can be used with this which will allow smaller llms like Gemma 2 2b to handle this types of task:

# <dictionary_lookup>
# Word: ほとんど
# - ほとんど【ほとんど】

# Word: 知る
# - 知る【しる】

# Word: 者
# - 者【もの】

# Word: も
# - も【も】

# Word: て
# - て【て】

# Word: の
# - の【の】

# Word: に
# - に【に】

# Word: 存在
# - 存在【そんざい】

# Word: は
# - は【は】

# Word: 葬ら
# - 葬ら【ほうむら】

# Word: は
# - は【は】

# Word: 太古
# - 太古【たいこ】

# Word: おり
# - おり【おり】

# Word: 今
# - 今【いま】

# Word: この
# - この【この】

# Word: ん
# - ん【ん】

# Word: 昔
# - 昔【むかし】

# Word: れ
# - れ【れ】

# Word: ませ
# - ませ【ませ】

# Word: い
# - い【い】
# </dictionary_lookup>

# Translate and break down this Japanese sentence:
# <japanese_sentence>
# この存在は太古の昔に葬られており、今は知る者もほとんどいません。
# </japanese_sentence>

# Format:
# 1. English Translation: [Full sentence translation]

# 2. <segmented_sentence>
#    [Your segmented sentence here. Separate each word with a comma, with no furigana.]
#    </segmented_sentence>

# 3. Breakdown:
#    - [Word]【ふりがな】: Context-specific definition

# Rules:
# 1. Include particles
# 2. Use original word forms
# 3. Always use 【ふりがな】, even for hiragana
# 4. Only hiragana in 【】
# 5. One 【】 per word
# 6. No explanations outside format
# 7. Use the furigana from the dictionary lookup
# 8. Include the entire sentence (excluding punctuation) in the breakdown.
# 9. Do not add any words that are not in the original sentence.

# Example:
# English Translation: This is an example sentence.

# <segmented_sentence>
# これ, は, 例, の, 文, です
# </segmented_sentence>

# Breakdown:
# - これ【これ】: this
# - は【は】: is
# - 例【れい】: example
# - の【の】: of
# - 文【ぶん】: sentence
# - です【です】: is

# Another Example:
# English Translation: I am eating an apple.

# <segmented_sentence>
# 私, は, りんご, を, 食べて, います
# </segmented_sentence>

# Breakdown:
# - 私【わたし】: I
# - は【は】: (This word is used as a particle to indicate the subject of the sentence)
# - りんご【りんご】: apple
# - を【を】: (This word is used as a particle to indicate the object of the sentence)
# - 食べて【たべて】: eating
# - います【います】: am