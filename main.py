def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # добавляем 0, чтобы гарантированно обработать всё в конце
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

if __name__ == "__main__":
    data = list(map(int, input().split()))
    n = data[0]
    heights = data[1:]
    print(largest_rectangle_area(heights))
