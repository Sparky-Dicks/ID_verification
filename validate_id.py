def get_input():
    try:
        id_number = int(input("Enter your ID number: "))
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
            if total > 9:
                total = (total//10) + (total%10)
            list_numbers[i] = total
            tester += int(list_numbers[i])
        else:
            tester += int(list_numbers[i])
            list_numbers[i] = int(list_numbers[i])
        # print("The List:", list_numbers)
        i+=1
    new_int = int(convert_list(list_numbers))//10
    print(tester)
    return tester


def validate_id_math(id_number, str_id):
    final_answer = (id_number%10)
    check_this_num = get_number(id_number, str_id)
    print(((check_this_num*9)%10),final_answer)
    if ((check_this_num*9)%10) != final_answer:
        return True
    else:
        return False


def validate_id_main(id_num):
    id_num_str = str(id_num)
    if len(id_num_str) != 13 or id_num_str[12]=="0" or validate_id_math(id_num, id_num_str):
        print("PLease enter a valid ID number")
        return get_input()
    else:
        return id_num


if __name__ == "__main__":
    id_num = get_input()
    print("Valid ID: ", id_num)