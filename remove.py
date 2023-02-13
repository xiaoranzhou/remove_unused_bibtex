def remove_unused_references(bib_file, bbl_file, aux_file):
    used_references = set()

    with open(bbl_file, "r") as bbl:
        for line in bbl:
            if line.startswith("\\bibitem{"):
                reference = line.strip().split("{")[1][:-1]
                used_references.add(reference)

    with open(aux_file, "r") as aux:
        for line in aux:
            if line.startswith("\\citation{"):
                reference = line.strip().split("{")[1][:-1]
                used_references.add(reference)

    with open(bib_file, "r") as bib:
        bib_lines = bib.readlines()

    with open(bib_file, "w") as bib:
        in_reference = False
        reference_name = ""

        for line in bib_lines:
            if line.startswith("@"):
                reference_name = line.strip().split("{")[1].split(",")[0]
                in_reference = reference_name in used_references
                if in_reference:
                    bib.write(line)
            elif in_reference:
                bib.write(line)

bib_file = "these.bib"
bbl_file = "output.bbl"
aux_file = "output.aux"

remove_unused_references(bib_file, bbl_file, aux_file)