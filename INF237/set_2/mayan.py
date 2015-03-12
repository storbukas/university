def main():
    lol = raw_input()
    word = raw_input()
    segment = raw_input()

    #segment = "AbrAcadAbRa"
    #word = "cAda"

    glyph_count = [0] * 65
    glyph_correct = [0] * 65

    for i in word:
        glyph_correct[ord(i)-65] += 1

    for i in range(len(word)):
        glyph_count[ord(segment[i])-65] += 1

    # iterate segment

    nr_of = 0
    if(glyph_count == glyph_correct):
        nr_of += 1

    current_start = 0
    current_end = len(word)-1

    #print(len(segment))

    for i in range(len(segment)-len(word)):
        old_char = segment[current_start]
        new_char = segment[current_end+1]

        current_start += 1
        current_end += 1

        glyph_count[ord(old_char)-65] -= 1
        glyph_count[ord(new_char)-65] += 1

        if(glyph_count == glyph_correct):
            nr_of += 1

    print(nr_of)

if __name__ == "__main__":
    main()
