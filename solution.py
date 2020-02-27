filenames = ["a_example", "b_read_on", "c_incunabula", "e_so_many_books", "f_libraries_of_the_world",  "d_tough_choices"]

for fn in filenames:
    print(fn)
    file = open(fn + ".txt", 'r')
    lines = [list(map(int, line.strip().split())) for line in file.readlines()]
    file.close()

    penalty = 3
    num_books = lines[0][0]
    num_lib = lines[0][1]
    time = num_days = lines[0][2]
    scores = lines[1]
    score = 0
    duplicates = set([])
    libraries_used = set([])
    schedule = []

    libraries = []
    N = len(lines)
    for i in range(2, len(lines), 2):
        if i==N-1 and lines[i]==[]:
            break
        #print(lines[i], i, len(lines))
        bidxs = sorted([(scores[lines[i+1][j]], lines[i+1][j]) for j in range(len(lines[i+1]))])[::-1]
        books_idxs = [x[1] for x in bidxs]
        libraries.append((lines[i][0], lines[i][1], lines[i][2], books_idxs, (i-2)//2))

    while time > 0:

        lib_scores = []

        for lib in libraries:
            if lib[-1] in libraries_used:
                continue

            books_scanned = (time-lib[1])*lib[2]
            books_remaining = books_scanned
            if books_scanned < 0:
                continue
            #print(lib)
            books = [(scores[lib[3][i]],lib[3][i]) for i in range(lib[0])]
            i = -1
            books_taken = []
            score = 0
            while books_remaining >0 and i < (lib[0]-1):
                i += 1

                if books[i][1] not in duplicates:
                    score+=books[i][0]
                    books_taken.append(books[i][1])
                    #books_taken.append()

                    books_remaining-=1
            value = score/((time-lib[1])+(penalty*lib[1]))
            lib_scores.append([value,books_taken, lib[1], lib[-1]])
        lib_scores.sort()
        if len(lib_scores) == 0:
            break
        books_taken = lib_scores[-1][1]
        for b in books_taken:
            duplicates.add(b)
        schedule.append(lib_scores[-1])
        libraries_used.add(lib_scores[-1][-1])
        time -= lib_scores[-1][-2]

    A = len(schedule)

    f = open(fn+'out.txt', 'w')

    f.write(str(A)+'\n')

    for i in range(A):
        lib = schedule[i]
        lib_idx = lib[-1]
        no_books = len(lib[1])
        books = ' '.join([str(x) for x in lib[1]])

        f.write(str(lib_idx)+' '+str(no_books)+'\n')
        f.write(books+'\n')










    # for line in lines:
    #     print(line)
    # print("scores", scores)
    # break


