# 87390
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    
    """
    n^2 배열 자르기 :
    정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

    n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
    i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
    1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
    1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
    새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

    Args :
    - n : 1 이상 10^7 이하 
    - left, right : 0 <= left <= right < n^2, right - left < 10^5

    Returns : 만들어진 1차원 배열 

    """
    """
    # soluition 1 -> time out 
    # 2차원 배열 생성
    matrix = []
    for i in range(n):
        maxx = i+1
        inner_matrix = []
        for j in range(n):
            if j+1 > maxx : maxx= j+1
            # inner_matrix.append(maxx)
            matrix.append(maxx)
        # matrix.append(inner_matrix)

    
    # print(matrix)

    return matrix[left:right+1]
    """

    # solution 2
    # index의 몫과 나머지로 해당 위치의 값을 알 수 있음.
    
    answer = []
    for i in range(left, right+1):
        row, col = divmod(i, n)
        val = max(row, col) + 1
        answer.append(val)
    
    return answer


# test case 
print(solution(3,2,5))
print(solution(4,7,14))