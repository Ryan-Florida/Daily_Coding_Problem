
def MeetsConstraint(list_of_numbers: list, k: int) -> bool:
    for i in list_of_numbers:
        for j in list_of_numbers:
            if i != j and i + j == k:
                return True
    return False

def main():
    list_of_numbers = [10, 15, 3, 7]
    k               = 17

    print(MeetsConstraint(list_of_numbers, k))

main()