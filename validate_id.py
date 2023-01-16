def get_input():
    try:
        id_number = int(input("Enter your ID number: "))
        # print(id_number)
        return validate_id_main(id_number)
    except ValueError:
        print("Must not contain letters or any special characters")
        return get_input()


def convert_list(list):
    result = int("".join(map(str, list)))
    return result
 

def get_number(list_numbers, str_id):
    tester = 0
    list_numbers = [x for x in str_id]
    i = 0
    while i < 13:
        if i%2!=0:
            total = int(list_numbers[i])*2
            # print("Total:", total)
            # print(list_numbers[i])
            if total > 9:
                print("Too big: ", total)
                total = (total//10) + (total%10)
            list_numbers[i] = total
            print("Index: ", list_numbers[i])
            tester += int(list_numbers[i])
        else:
            # tester += int(list_numbers[i])
            list_numbers[i] = int(list_numbers[i])
        # print("The List:", list_numbers)
        i+=1
    new_int = int(convert_list(list_numbers))//10
    print("Tester: ", tester)
    return tester


def validate_id_math(id_number, str_id):
    final_answer = (id_number%10)
    print(final_answer)
    check_this_num = get_number(id_number, str_id)
    print(((check_this_num*9)%10),final_answer)
    if ((check_this_num*9)%10) == final_answer:
        # print("***")
        return True
    else:
        # print("**")
        return False


def validate_id_main(id_num):
    id_num_str = str(id_num)
    while len(id_num_str) != 13:
        print("Check", id_num_str)
        id_num_str = "0" + str(id_num_str)
    print(id_num_str, "***")
    if id_num_str[12]=="0" or validate_id_math(id_num, id_num_str):
        print("PLease enter a valid ID number")
        return get_input()
    else:
        return id_num_str


if __name__ == "__main__":
    id_num = get_input()
    print("Valid ID: ", id_num)
