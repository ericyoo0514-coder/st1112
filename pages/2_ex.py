import streamlit as st

st.title("11/12 Practice Problems")

a, b, c = st.tabs( ["문제1" ,"문제2" ,"문제3"])
with a:
    st.write("문제1")
    st.subheader("1. 식 전개하기")
    st.latex(r"(x+y)^2")


    with st.form("forms1"):
        answer1 = st.radio("전개한 식을 선택해주세요.",
        [r"$x^2+2x+1$", r"$x^2-2xy+y^2$",
        r"$x^2+2xy+y^2$", r"$x^2+xy+y^2$"],
        index=None,)


        submit_button1 = st.form_submit_button("제출")


    if submit_button1:
        if answer1 == r"$x^2+2xy+y^2$":
            st.success("정답입니다!")
        elif answer1 == r"$x^2-2xy+y^2$":
            st.warning("앗! 부호를 다시 살펴볼까요?")
        elif answer1 == r"$x^2+xy+y^2$":
            st.warning("앗! 두번째 항을 다시 살펴볼까요!")
        else:
            st.warning("앗! y는 어디로 갔나요!!")








with b:




    st.subheader("2. 일차방정식 풀기")
    st.latex(r"2x+3=7")


    with st.form("forms2"):
        answer2 = st.radio("x의 값을 선택해주세요.",
        [r"x=2", r"x=5", r"x=-2", r"x=4"],
        index=None,)
        submit_button2 = st.form_submit_button("제출")


    if submit_button2:
        if answer2 == r"x=2":
            st.success("정답입니다! 양변에서 3을 빼고 2로 나누면 x=2입니다.")
        elif answer2 == r"x=5":
            st.warning("앗! 3을 빼야 하는데 더한 것 같아요.")
        elif answer2 == r"x=-2":
            st.warning("앗! 양변에서 3을 뺄 때 부호를 다시 확인해보세요.")
        elif answer2 == r"x=4":
            st.warning("앗! 2x=4에서 양변을 2로 나눠야 해요.")
        else:
            st.warning("답을 선택해주세요.")


with c:
    st.write("문제3")
