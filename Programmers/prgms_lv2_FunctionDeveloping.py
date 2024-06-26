# 42586
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses:list, speeds:list) -> list:
    """
    기능 개발 : 

    Args :
    - progress : 배포되어야 할 순서대로 작업의 진도가 적힌 정수 배열 
    - speeds : 각 작업의 개발 속도가 적힌 정수 배열

    Retruns : 각 배포마다 몇 개의 기능이 배포되는지 담은 배열 

    각 기능의 개발 속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 될 수 있고,
    이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.
    배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정한다.

    """

    answer = []

    remaining_dates = [] # 각 작업별로 배포까지 필요한 기간 
    for progress, speed in zip(progresses, speeds):
        remaining_progress = 100 - progress
        necessary_dates = remaining_progress // speed
        if remaining_progress % speed != 0:
            necessary_dates += 1

        remaining_dates.append(necessary_dates)

    # print(remaining_dates)

    idx = 0
    next_idx = 1
    while next_idx < len(remaining_dates):
        if next_idx == len(remaining_dates)-1:
            if remaining_dates[idx] > remaining_dates[next_idx]:
                answer.append(len(remaining_dates[idx:]))
                break
            else : # remaining_dates[idx] <= remaining_dates[next_idx]
                answer.append(len(remaining_dates[idx:next_idx]))
                answer.append(1)
                break
        elif remaining_dates[idx] < remaining_dates[next_idx]:
            answer.append(len(remaining_dates[idx:next_idx]))
            idx = next_idx
            next_idx = idx + 1
        else : # remaining_dates[idx] >= remaining_dates[next_idx]
            next_idx += 1

        


            
    return answer



# test case 
print(solution([93, 30, 55], [1, 30, 5]))
print()
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))