import streamlit as st

# ตั้งค่าหน้าเว็บ (แนะนำให้เลือกแบบ wide เพื่อให้จัดวางซ้าย-ขวาได้สวยงาม)
st.set_page_config(page_title="Visual Novel - Choose Character", layout="centered")

# --- CSS ตกแต่งเพิ่มเติมให้เข้ากับแนวเกม ---
st.markdown("""
    <style>
    .title-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .char-card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 2px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. ตรวจสอบสถานะว่าเลือกตัวละครหรือยัง ---
if 'gender' not in st.session_state:
    st.session_state.gender = None

# ถ้ายังไม่ได้เลือกตัวละคร ให้แสดงหน้าเลือก
if st.session_state.gender is None:
    st.markdown('<div class="title-text">CHOOSE YOUR CHARACTER</div>', unsafe_allow_html=True)
    
    # แบ่ง 2 คอลัมน์ (ซ้าย: Woman, ขวา: Male) ตามแบบร่าง
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="char-card">', unsafe_allow_html=True)
        st.subheader("Woman")
        
        # --- แทนที่ด้วย path รูปภาพตัวละครหญิงของคุณ ---
        # ตัวอย่าง: st.image("images/woman_sprite.png", use_container_width=True)
        # ตอนนี้ใส่ภาพ Placeholder ไว้ก่อนครับ
        st.image("https://placehold.co/300x400/png?text=Woman+Character", use_container_width=True)
        
        if st.button("เลือกตัวละครหญิง (Woman)", use_container_width=True, key="btn_woman"):
            st.session_state.gender = "Woman"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="char-card">', unsafe_allow_html=True)
        st.subheader("Male")
        
        # --- แทนที่ด้วย path รูปภาพตัวละครชายของคุณ ---
        # ตัวอย่าง: st.image("images/male_sprite.png", use_container_width=True)
        st.image("https://placehold.co/300x400/png?text=Male+Character", use_container_width=True)
        
        if st.button("เลือกตัวละครชาย (Male)", use_container_width=True, key="btn_male"):
            st.session_state.gender = "Male"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. หลังจากเลือกตัวละครแล้ว เข้าสู่เนื้อเรื่องบทปฐมบท (Chapter 1) ---
else:
    st.success(f"คุณได้เลือกเล่นตัวละคร: **{st.session_state.gender}** เรียบร้อยแล้ว!")
    st.write("---")
    
    # ตัวอย่างการพาเข้าเนื้อเรื่องบทที่ 1
    st.subheader("ปฐมบท (Chapter 1): จุดเริ่มต้นของปริศนา")
    
    if st.session_state.gender == "Woman":
        st.info("บทสนทนาพิเศษสำหรับตัวละครหญิง: 'ฉันก้าวเท้าเข้ามาในที่เกิดเหตุ... ทุกอย่างดูผิดปกติไปหมด'")
    else:
        st.info("บทสนทนาพิเศษสำหรับตัวละครชาย: 'ผมได้รับแจ้งเหตุฉุกเฉินและรีบมายังสถานที่แห่งนี้ทันที'")
        
    # ปุ่มสำหรับกดรีเซ็ตกลับไปหน้าเลือกตัวละคร (เผื่ออยากลองเปลี่ยน)
    if st.button("🔄 กลับไปหน้าเลือกตัวละครใหม่"):
        st.session_state.gender = None
        st.rerun()
