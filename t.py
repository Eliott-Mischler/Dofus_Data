with open('resources.txt', 'r', encoding='utf-8') as clean_incomplete:
    with open('out2.txt', 'r', encoding='utf-8') as unclean_complete:
        ci = clean_incomplete.read()
        uc = unclean_complete.read()
        lines_ci = [line for i, line in enumerate(ci.splitlines()) if not i%2]
        lines_uc = [line for line in enumerate(uc.splitlines())]
        print(len(lines_uc))

        for i, line_ci in enumerate(lines_ci):
            if i % 50 == 1:
                print(line_ci, lines_uc[i])
