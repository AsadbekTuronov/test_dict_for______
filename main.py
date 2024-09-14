dic = {"act up" : "ishlamay qolmoq",
    "add * up +" : "hisoblab chiqarmoq",
    "add up to + " : "tashkil qilmoq",
    "add up" : "haqiqatga o'xshamoq",
    "ask * out +" : "kelishini so'ramoq",
    "ask * over +" : "taklif qilmoq",
    "back down" : "vos kechmoq/qaroridan qaytmoq",
    "back out" : "vadasini ustida turolmaydi/og'zida saqlab turolmaydi",
    "back out of +" : "fikridan qaytmoq",
    "back * up +" : "orqaga qaytmoq"
}

eng = ['act up', 'add * up +', 'add up to + ', 'add up', 'ask * out +',
 'ask * over +', 'back down', 'back out', 'back out of +', 'back * up +']
uzb = ['ishlamay qolmoq', 'hisoblab chiqarmoq', 'tashkil qilmoq', 
"haqiqatga o'xshamoq", "kelishini so'ramoq", 'taklif qilmoq', 
'vos kechmoq/qaroridan qaytmoq', 
"vadasini ustida turolmaydi/og'zida saqlab turolmaydi",
 'fikridan qaytmoq', 'orqaga qaytmoq']

import streamlit as st
from random import choice

st.title("test app for ...")

for i in dic:
    st.sidebar.write(f"""
        `{i}` : `{dic[i]}`
    """)

# st.button("testni boshlash")


if 'count_corr' not in st.session_state:
    st.session_state.count_corr = 0
if 'count_err' not in st.session_state:
    st.session_state.count_err = 0
if 'choiced_word' not in st.session_state:
    st.session_state.choiced_word = choice(eng)




    




def check_opt():
    is_r = True
    if opt == dic[st.session_state.choiced_word]:
        st.session_state.count_corr += 1
        st.session_state.choiced_word = choice(eng)
        if st.session_state.count_corr==5:
            is_r = False
            with st.expander("extra savol"):
                st.write("jumlani davom ettir")
                st.text_input(label="i love you", value="1 4444 333 t__")
                st.button("topdim") 

    else:
        st.session_state.count_err += 1 

    if is_r: st.rerun()
    
    

    
opt = st.selectbox(
    label=st.session_state.choiced_word,
    options=uzb)

   

if st.button("click"):
    check_opt()
    
st.markdown('''***''')

st.write("to'g'ri", st.session_state.count_corr)
st.write("noto'g'ri", st.session_state.count_err)        



    

