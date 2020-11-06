from secrets import randbelow
def deel_kaarten():
    nog_beschikbare_kaarten = [["K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "KB", "KQ", "KK", "KA"],
                               ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SB", "SQ", "SK", "SA"],
                               ["R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "RB", "RQ", "RK", "RA"],
                               ["H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HB", "HQ", "HK", "HA"]]
    deling = [[], [], [], []]
    for i in range(13):
        for j in range(4):
            shape = randbelow(4)
            while len(nog_beschikbare_kaarten[shape]) == 0:
                shape = randbelow(4)
            level = randbelow(len(nog_beschikbare_kaarten[shape]))
            deling[j].append(nog_beschikbare_kaarten[shape].pop(level))
    return deling
deling = deel_kaarten()
