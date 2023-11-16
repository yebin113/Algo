# 옵션의 개수 N
N = int(input())
order_list = []
for _ in range(N):
    order = list(input().split())
    order2 = ''
    # 먼저 하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다.
    # 만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.
    for i in range(len(order)):
        # 한문장으로 만들어놓음(뒤에 사용)
        order2 += order[i]+' '
        # 만약 띄어쓰기 후 첫글자가 명령어에 없다면
        if order[i][0].lower() not in order_list and order[i][0].upper() not in order_list:
            # 단축키 등록 후 break
            order_list.append(order[i][0])
            order[i] = f'[{order[i][0]}]'+order[i][1:]

            print(*order)
            break
    # 앞글자들에 단축키에 할 것이 없으면...
    else:
        order2 = order2[:len(order2)-1]
        # 한문장으로 만든 문자열을 순회하며
        for j in range(len(order2)):
            # 없는 단축어를 발견하면...
            if order2[j] != ' ' and order2[j].lower() not in order_list and order2[j].upper() not in order_list:
                # 대문자로 넣어서 추가함
                order_list.append(order2[j].upper())
                for k in range(len(order2)):
                    if k == j:
                        print(f'[{order2[k]}]',end='')
                    elif order2[k]==' ':
                        print(f' ',end='')
                    else:
                        print(order2[k],end='')
                print()
                break
        else:
            print(*order)





