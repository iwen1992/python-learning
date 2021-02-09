def isbn_or_key(word):
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "");
    if "-" in word and len(short_word)==10 and short_word.isdigit:  # 多个and条件，把最可能为假的放在前面
        isbn_or_key = 'isbn'
    return  isbn_or_key