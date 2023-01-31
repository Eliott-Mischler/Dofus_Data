with open('resources.txt', 'r', encoding='utf-8') as clean_incomplete:
    with open('out2.txt', 'r', encoding='utf-8') as unclean_complete:
        ci = clean_incomplete.read()
        uc = unclean_complete.read()
        lines_ci = [line for i, line in enumerate(ci.splitlines()) if not i%2]
        lines_uc = [line for i, line in enumerate(uc.splitlines()) if not i%2]
        print(len(lines_uc))

        for i, line_ci in enumerate(lines_ci):
            print(i)
            if line_ci == lines_uc[i+1]:
                print(lines_uc[i], i*2, 1)
                break
            if line_ci == lines_uc[i+2]:
                print(lines_uc[i:i+2], i*2, 2)
                break
            if line_ci == lines_uc[i+3]:
                print(lines_uc[i:i+3], i*2, 3)
                break
            if line_ci == lines_uc[i+4]:
                print(lines_uc[i:i+4], i*2, 4)
                break