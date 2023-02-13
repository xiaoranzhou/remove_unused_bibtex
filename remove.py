import shutil

bib_file = "these.bib"
bbl_file = "output.bbl"
aux_file = "output.aux"
new_bib_file = "new.bib"


def remove_unused_references(bib_file, bbl_file, aux_file, new_bib_file):
    used_references = set()
    shutil.copy(bib_file, new_bib_file)
    with open(bbl_file, "r") as bbl:
        for line in bbl:
            if line.startswith("\entry{"):
                reference = line.strip().split("{")[1][:-1]
                used_references.add(reference)
                print(reference)

    with open(aux_file, "r") as aux:
        for line in aux:
            if line.startswith("\\abx@aux@cite{0}{"):
                reference = line.strip().split("{")[2][:-1]
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



remove_unused_references(bib_file, bbl_file, aux_file, new_bib_file)