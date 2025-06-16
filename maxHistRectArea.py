
def max_rect_area(arr):
    i = 0
    #top = -1
    maxarea = -1
    currentarea = 0
    stack = []
    for x in range(len(arr)):
        if i == 0 or arr[i] > arr[stack[-1]]:
            stack.append(i)
            #top = stack[-1]
            i = i + 1
            print(stack, stack[-1], i)
        else:
            print(i, arr[i], stack[-1])
            top = stack.pop()
            if len(stack) == 0:
                currentarea = arr[top] * i
                stack.append(i)
                i = i + 1
            else:
                currentarea = arr[top] * (i-stack[-1]-1)
            if currentarea > maxarea:
                maxarea = currentarea

    print(maxarea)


max_rect_area([2, 1, 2, 3, 1])
