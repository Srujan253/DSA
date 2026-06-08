def reverse_paranthese(s):
    st=[]
    for ch in s:
        if ch==")":
            res=""

            while st[-1]!="(" :
                res+=st[-1]
                st.pop()
            st.pop()
            for i in res:
                st.append(i)
        else:
            st.append(ch)
    return "".join(st)
print(reverse_paranthese("(u(love)i)"))
