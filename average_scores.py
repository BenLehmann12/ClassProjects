
def average():
    score1 = int(input("Enter first score:"))
    score2 = int(input("Enter second score:"))
    score3 = int(input("Enter third score:"))
    sum = score1 + score2 + score3
    avg = sum / 3
    return avg


if __name__ == '__main__':
    name = input("Enter your Name")
    average_scores = average()
    print(str(name) +": " + str(average_scores))
