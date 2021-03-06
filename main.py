from Tab import Tab

def main():
    # from Men on The Couch
    senso_comum()


def hedwig():
    tab = Tab(snaps_per_beat = 4)

    tab.add("G", "4")
    tab.add("B", "5")
    tab.add("e", "3")
    tab.add("e", "\\2", beat=3, snap=4)
    tab.add("e", "7")
    tab.add("e", "5")
    tab.add("e", "2")
    tab.add("e", "0", beat=6, snap=4)
    tab.add("e", "3")
    tab.add("e", "\\2")
    tab.add("B", "4")
    tab.add("B", "6")
    tab.add("B", "0")

    tab.add("G", "4")
    tab.add("B", "5")
    tab.add("e", "3")
    tab.add("e", "\\2")
    tab.add("e", "0")
    tab.add("e", "7")
    tab.add("e", "10")
    tab.add("e", "9")
    tab.add("e", "8")
    tab.add("B", "9")
    tab.add("e", "8")
    tab.add("e", "7")
    tab.add("e", "\\6")
    tab.add("D", "8")
    tab.add("B", "8")
    tab.add("e", "0")

    

    tab.add("B", "8")
    tab.add("e", "7")
    tab.add("B", "8")
    tab.add("e", "7")
    tab.add("B", "8")
    tab.add("e", "8")
    tab.add("e", "7")
    tab.add("e", "6")
    tab.add("B", "7")
    tab.add("B", "8")
    tab.add("e", "7")
    tab.add("e", "6")
    tab.add("D", "8")
    tab.add("B", "9")
    tab.add("e", "7")

    tab.add("B", "8")
    tab.add("e", "7")
    tab.add("B", "8")
    tab.add("e", "7")
    tab.add("B", "8")
    tab.add("e", "10")
    tab.add("e", "9")
    tab.add("e", "8")
    tab.add("B", "9")
    tab.add("e", "8")
    tab.add("e", "7")
    tab.add("e", "\\6")
    tab.add("D", "8")
    tab.add("B", "8")
    tab.add("e", "0")

    return tab


def senso_comum():
    intro = Tab()

    intro.add("e", "16")
    intro.add("e", "x")
    intro.add("e", "14")
    intro.add("e", "\\12")
    intro.add("B", "16")
    intro.add("G", "14")
    intro.add("G", "13")
    intro.add("B", "14")
    intro.add("G", "13")
    intro.add("G", "\\11")

    intro.add("D", "13")
    intro.add("D", "/14")
    intro.add("G", "11")
    intro.add("B", "12")
    intro.add("G", "13")
    intro.add("D", "14")
    intro.add("D", "13")

    intro.add("B", "14")
    intro.add("B", "12")
    intro.add("G", "14")
    intro.add("G", "13")
    intro.add("e", "12")
    intro.add("G", "13")
    intro.add("G", "11")
    intro.add("G", "14")
    
    intro.add("e", "16")
    intro.add("e", "x")
    intro.add("e", "14")
    intro.add("e", "\\12")
    intro.add("B", "16")
    intro.add("G", "14")
    intro.add("G", "13")
    intro.add("B", "14")
    intro.add("B", "16")
    intro.add("G", "13")
    intro.add("G", "14")
    intro.add("G", "16")
    intro.add("B", "14")
    intro.add("B", "17")
    intro.add("B", "16")
    intro.add("e", "16")
    intro.add("e", "19")
    intro.add("e", "17")

    
    chorus_1 = Tab()
    chorus_1.add("e", "16")
    chorus_1.add("e", "14")
    chorus_1.add("B", "17")
    chorus_1.add("B", "16")
    chorus_1.add("B", "14")
    chorus_1.add("G", "16")
    chorus_1.add("B", "14")
    chorus_1.add("G", "16")
    chorus_1.add("G", "13")
    chorus_1.add("G", "16")
    chorus_1.add("B", "14")
    chorus_1.add("e", "x7", beat=4, snap=1)
    chorus_1.add("B", "x7", beat=4, snap=1)
    chorus_1.add("G", "x7", beat=4, snap=1)

    
    chorus_1.add("e", "16", beat=5, snap=1)
    chorus_1.add("e", "14")
    chorus_1.add("B", "17")
    chorus_1.add("B", "16")
    chorus_1.add("B", "14")
    chorus_1.add("G", "16")
    chorus_1.add("B", "14")
    chorus_1.add("G", "16")
    chorus_1.add("G", "13")
    chorus_1.add("G", "16")
    chorus_1.add("G", "13")
    chorus_1.add("G", "16")
    chorus_1.add("G", "13")
    chorus_1.add("G", "16")

    chorus_2 = Tab()
    chorus_2.add("D", "11")
    chorus_2.add("G", "12")
    chorus_2.add("G", "/13")
    chorus_2.add("G", "11")
    chorus_2.add("G", "12")
    chorus_2.add("G", "/13")
    chorus_2.add("B", "12")
    chorus_2.add("G", "13")
    chorus_2.add("G", "11")
    chorus_2.add("G", "13")
    chorus_2.add("D", "11")
    chorus_2.add("B", "x7", beat=4, snap=1)
    chorus_2.add("G", "x7", beat=4, snap=1)
    chorus_2.add("D", "x7", beat=4, snap=1)
    chorus_2.add("D", "11", beat=5, snap=1)
    chorus_2.add("G", "12")
    chorus_2.add("G", "/13")
    chorus_2.add("G", "11")
    chorus_2.add("G", "12")
    chorus_2.add("G", "/13")
    chorus_2.add("B", "12")
    chorus_2.add("G", "13")
    chorus_2.add("B", "12")
    chorus_2.add("G", "13")
    chorus_2.add("G", "11")
    chorus_2.add("D", "11")
    
    print("Intro:")
    print(intro)

    print("Refrao 1:")
    print(chorus_1)

    print("Refrao 2:")
    print(chorus_2)

main()