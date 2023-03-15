def kill_downNum(n:int, result:list) -> list:
    new_result = []
    for value in result:
        if value > 0:
            value_str = str(value)
            new_result.append(float(value_str[0:n+1]))
        else:
            value_str = str(value)
            new_result.append(float(value_str[0:n+2]))
    return new_result


prepared_value = [0.1234567, -0.12312]
main_value = [0.1234, 0.1243456]
prepared_value = kill_downNum(4, prepared_value)
main_value = kill_downNum(4, main_value)

print(main_value)
print(prepared_value)
matching_idx = {}
for idx, value in enumerate(main_value):
    if value in prepared_value:
        print(value)
        matching_idx[value] = idx
    else:
        matching_idx[value] = 'none'
print(matching_idx)
        
