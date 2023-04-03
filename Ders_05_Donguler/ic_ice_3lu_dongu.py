# ABC harflerinin farklı permütasyonu:
for ilk in "ABC":
    for ikinci in "ABC":
        if ikinci != ilk:
            for ucuncu in "ABC":
                if ucuncu != ilk and ucuncu != ikinci:
                    for dorduncu in "ABC":
                        if dorduncu != ilk and ikinci !=ucuncu:
                          print(ilk + ikinci + ucuncu + dorduncu)