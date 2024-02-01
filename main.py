def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()

    return file_contents


def get_words(content):
    return len(content.split())


def count_letters(content):
    count_result = {}

    words = content.split()

    for word in words:
        for i in range(0, len(word)):
            if not (word[i].isalpha()):
                continue

            if word[i].lower() in count_result:
                count_result[word[i].lower()] += 1
            else:
                count_result[word[i].lower()] = 1

    return sorted(list(count_result.items()), key=lambda x: x[1], reverse=True)


def main():
    books_path = "./books/frankenstein.txt"

    book_content = get_book_text(books_path)
    words_count = get_words(book_content)

    print(f"There are {words_count} words in the book")

    print("Frequency of letter appear in the book")
    letter_frequency = count_letters(book_content)
    print(f"{letter_frequency}")


main()
