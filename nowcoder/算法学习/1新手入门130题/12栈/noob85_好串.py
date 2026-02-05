# https://www.nowcoder.com/practice/9b072237ebdd4dd99562f01cbf594fac
s = input()
st = []
for c in s:
    if c == 'a':
        st.append(c)
    elif c == 'b':
        if st:
            st.pop()
        else:
            print("Bad")
            exit()
if st:
    print("Bad")
else:
    print("Good")
