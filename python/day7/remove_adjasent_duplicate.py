def remove_all_adjusent(s):
    st=[]
    for i in s:
        if st and i ==st[-1]:
            st.pop()
        else:
            st.append(i)
    return "".join(st)
print(remove_all_adjusent("abbaca"))