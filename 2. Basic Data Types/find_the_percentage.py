if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks:
        if i == query_name:
            sum= (sum(student_marks[query_name]))
            len=len(student_marks[query_name])
            avg=sum/len
            print('%.2f' %avg)