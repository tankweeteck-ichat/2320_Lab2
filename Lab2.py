

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    print(strlist)
    floatlist = [float(x) for x in strlist]
    print(floatlist)
    return floatlist

def calc_average(floatlist):
    print("calc_average")
    average = sum(floatlist)/len(floatlist)
    print("Average = " + f"{average:.2f}")
    return average

def find_min_max(floatlist):
    print("find_min_max")
    mintemp = min(floatlist)
    maxtemp = max(floatlist)
    print("Min = " + str(mintemp))
    print("Max = " + str(maxtemp))
    resultlist = []
    resultlist.append(mintemp)
    resultlist.append(maxtemp)
    return resultlist


def sort_temperature(floatlist):
    print("sort_temperature")
    sortedlist = floatlist.copy()
    sortedlist=sorted(sortedlist)
    print(sortedlist)
    return sortedlist



def calc_median_temperature(floatlist):
    print("calc_media_temperature")
    sortedlist = floatlist.copy()
    sortedlist = sorted(sortedlist)
    num = len(sortedlist)
    print("num = ", num)
    if num % 2 == 0:
        index = int(num/2)
        median=(sortedlist[index - 1] + sortedlist[index])/2.0
    else:
        index = int(num - 1)
        index = int(index/2)
        median = sortedlist[index]

    print("Median = " + f"{median:.2f}")
    return median


def main():
    print("ET0735 (DevOps for AIoT) - lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sort_temperature(floatlist)
    calc_median_temperature(floatlist)



if __name__ == "__main__":
    main()