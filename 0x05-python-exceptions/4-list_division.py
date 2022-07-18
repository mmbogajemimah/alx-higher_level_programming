#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp_result = 0
    div = []
    for items in range(0, list_length):
        try:
            temp_result = my_list_1[items] / my_list_2[items]
        except TypeError:
            temp_result = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_result = 0
            print("division by 0")
        except IndexError:
            temp_result = 0
            print("out of range")
        finally:
            pass
        div.append(temp_result)
    return 
