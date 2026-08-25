import time
import streamlit as st

# ====================================================
# 🎮 ชื่อเกม
# ====================================================
st.title("⏱️ เกมเติมศัพท์จับเวลา")
st.write("เติมตัวอักษรให้เป็นคำศัพท์ที่ถูกต้อง ภายในเวลา 30 วินาที")


# ====================================================
# 1. กำหนดค่าเริ่มต้นใน session_state
# ====================================================

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "result_shown" not in st.session_state:
    st.session_state.result_shown = False


# ====================================================
# 2. ฟังก์ชันเริ่มเกมใหม่
# ====================================================

def reset_game():

    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    # เริ่มจับเวลาใหม่
    st.session_state.start = time.time()

    # เกมยังไม่จบ
    st.session_state.is_ended = False

    # ยังไม่แสดงผลลัพธ์
    st.session_state.result_shown = False


# ====================================================
# 3. Dialog แสดงผลคะแนน
# ====================================================

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()

    score = 0

    # แปลงคำตอบเป็นตัวพิมพ์เล็ก
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()


    # ------------------------------------------------
    # ตรวจข้อ 1
    # ------------------------------------------------

    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 1: ไม่ถูกต้อง")
        st.write("คำตอบที่ถูกต้องคือ **apple**")


    # ------------------------------------------------
    # ตรวจข้อ 2
    # ------------------------------------------------

    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 2: ไม่ถูกต้อง")
        st.write("คำตอบที่ถูกต้องคือ **fish**")


    # ------------------------------------------------
    # ตรวจข้อ 3
    # ------------------------------------------------

    if u_ans3 == "lemon":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 3: ไม่ถูกต้อง")
        st.write("คำตอบที่ถูกต้องคือ **lemon**")


    # ------------------------------------------------
    # ตรวจข้อ 4
    # ------------------------------------------------

    if u_ans4 == "pen":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 4: ไม่ถูกต้อง")
        st.write("คำตอบที่ถูกต้องคือ **pen**")


    # ------------------------------------------------
    # แสดงคะแนน
    # ------------------------------------------------

    st.divider()

    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")


    # ------------------------------------------------
    # แสดงผลชนะ/แพ้
    # ------------------------------------------------

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ====================================================
# 4. ปุ่มเริ่มเกม
# ====================================================

st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ====================================================
# 5. แสดงเวลานับถอยหลัง
# ====================================================

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:

        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )

    else:

        # หมดเวลา
        st.session_state.is_ended = True

        st.rerun()


st.divider()


# ====================================================
# 6. ช่องกรอกคำตอบ
# ====================================================

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: A `L _ _ on` is very sour. 🍋",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: May I borrow your `P _ n`. 🖊️",
    value=st.session_state.ans4_val
)


# ====================================================
# 7. บันทึกคำตอบลง session_state
# ====================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ====================================================
# 8. ปุ่มส่งคำตอบ
# ====================================================

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):

        # จบเกม
        st.session_state.is_ended = True

        st.rerun()


    # ------------------------------------------------
    # ทำให้นาฬิกาเดินต่อทุก 1 วินาที
    # ------------------------------------------------

    time.sleep(1)

    st.rerun()


# ====================================================
# 9. แสดง Dialog ผลลัพธ์
# ====================================================

if (
    st.session_state.is_ended
    and not st.session_state.result_shown
):

    # ป้องกัน Dialog เปิดซ้ำ
    st.session_state.result_shown = True

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )
    
st.divider()
st.write("น.ส.ณัฏฐณิชชา สัจจ์ธัมม์ เลขที่ 23 ห้อง4/9")
