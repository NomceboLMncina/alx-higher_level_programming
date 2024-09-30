#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    t_r = 0
    for x in range(0, list_length):
        try:
            t_r = my_list_1[x] / my_list_2[x]
        except TypeError:
            t_r = 0
            print("wrong type")
        except ZeroDivisionError:
            t_r = 0
            print("Division by 0")
        except IndexError:
            t_r = 0
            print("Out of range")
        finally:
            pass
        div.append(t_r)
    return div
