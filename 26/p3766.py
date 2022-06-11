file = open('p3766.txt')
n = int(file.readline())

nums = [int(i) for i in file.readlines() if i]

nums_sorted = sorted(nums)

# Среднее арифметическое пары должно быть больше этого числа чтобы удовлетворять первому условию
median = nums_sorted[len(nums)//2 - 1]

# Среднее арифметическое пары должно быть меньше этого числа чтобы удовлетворять второму условию
quarter = nums_sorted[len(nums)//4*3]

counter = 0
min_sr_ar = 10000000000000000
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        s = nums[i] + nums[j]
        if s % 2 != 0:
            continue
        sr_ar = (nums[i] + nums[j]) / 2
        if sr_ar > median and sr_ar < quarter:
            counter += 1
            min_sr_ar = min(min_sr_ar, sr_ar)

print(counter, min_sr_ar)