#   17. 1부터 1000까지 영어로 썼을 때 사용된 글자의 개수는?
one_nine = "one two three four five six seven eight nine".split()
eleven_nineteen = "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
twenty_ninety = "twenty thirty forty fifty sixty seventy eighty ninety".split()
before_hundred_list = one_nine + ["ten"] + eleven_nineteen + [i+j for i in twenty_ninety for j in [""]+one_nine]
after_hundred_list = [i+"hundred" for i in one_nine] + [i+"hundredand"+j for i in one_nine for j in before_hundred_list]
print(sum(len(i) for i in before_hundred_list+after_hundred_list)+len("onethousand"))
# 1000(one thousand)을 추가 안해줘서 무한 삽질...
