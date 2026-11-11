import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Visual Novel - Beta", layout="centered")

# --- 1. CSS ตกแต่งพื้นหลังและสไตล์เกม VN ---
st.markdown("""
    <style>
    /* เปลี่ยนสีพื้นหลังหลักของแอปให้ออกแนวโทนมืดลึกลับสไตล์เกมไขคดี */
    .stApp {
        background: linear-gradient(135deg, #121214 0%, #1a1a24 100%);
        color: #e0e0e0;
    }
    .title-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(138, 43, 226, 0.5);
    }
    .char-card {
        background-color: #1e1e24;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.5);
        border: 2px solid #33334d;
    }
    .profile-box {
        background-color: #262633;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #5d3fd3;
        box-shadow: 0 0 15px rgba(93, 63, 211, 0.3);
        margin-bottom: 20px;
    }
    .story-box {
        background-color: #1a1a22;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #5d3fd3;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. กำหนดค่าเริ่มต้นใน session_state ---
if 'step' not in st.session_state:
    st.session_state.step = 'choose_char'  # ขั้นตอน: 'choose_char' -> 'preview_char' -> 'playing'
if 'gender' not in st.session_state:
    st.session_state.gender = None
if 'char_data' not in st.session_state:
    st.session_state.char_data = {}
if 'choice_result' not in st.session_state:
    st.session_state.choice_result = None


# ==========================================
# PHASE 1: หน้าเลือกตัวละคร
# ==========================================
if st.session_state.step == 'choose_char':
    st.markdown('<div class="title-text">CHOOSE YOUR CHARACTER</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="char-card">', unsafe_allow_html=True)
        st.subheader("Woman")
        st.image("https://placehold.co/300x400/2a2a3b/fff?text=Woman+Character", use_container_width=True)
        
        if st.button("เลือกตัวละครหญิง", use_container_width=True, key="btn_w"):
            st.session_state.gender = "Woman"
            st.session_state.char_data = {
                "name": "ร้อยตำรวจตรีหญิง อลิส (Alice)",
                "gender": "หญิง (Female)",
                "age": 24,
                "bio": "ตำรวจมือใหม่ไฟแรง ผู้มีเซ้นส์ในการสังเกตรายละเอียดเล็กๆ น้อยๆ ในที่เกิดเหตุ"
            }
            st.session_state.step = 'preview_char'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="char-card">', unsafe_allow_html=True)
        st.subheader("Male")
        st.image("https://placehold.co/300x400/2a2a3b/fff?text=Male+Character", use_container_width=True)
        
        if st.button("เลือกตัวละครชาย", use_container_width=True, key="btn_m"):
            st.session_state.gender = "Male"
            st.session_state.char_data = {
                "name": "นักสืบ เลโอ (Leo)",
                "gender": "ชาย (Male)",
                "age": 27,
                "bio": "นักสืบเอกชนผู้ผ่านคดีปริศนาร้ายแรงมานับไม่ถ้วน เยือกเย็นและมีเหตุผล"
            }
            st.session_state.step = 'preview_char'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# PHASE 2: หน้าต่างเช็คข้อมูลก่อนยืนยัน (ล็อกตัวละคร)
# ==========================================
elif st.session_state.step == 'preview_char':
    st.markdown('<div class="title-text">CHARACTER PROFILE</div>', unsafe_allow_html=True)
    
    data = st.session_state.char_data
    
    col_prev1, col_prev2 = st.columns([1, 1], gap="large")
    with col_prev1:
        if st.session_state.gender == "Woman":
            st.image("https://placehold.co/300x400/2a2a3b/fff?text=Woman+Profile", use_container_width=True)
        else:
            st.image("https://placehold.co/300x400/2a2a3b/fff?text=Male+Profile", use_container_width=True)
            
    with col_prev2:
        st.markdown(f"""
        <div class="profile-box">
            <h3>📋 ข้อมูลตัวละคร</h3>
            <p><b>ชื่อ:</b> {data['name']}</p>
            <p><b>เพศ:</b> {data['gender']}</p>
            <p><b>อายุ:</b> {data['age']} ปี</p>
            <p><b>ประวัติย่อ:</b> {data['bio']}</p>
            <hr style="border-color: #444;">
            <p style="color: #ff9999; font-size: 0.9rem;">⚠️ เมื่อกดยืนยันแล้ว คุณจะไม่สามารถเปลี่ยนตัวละครนี้ได้อีกในรอบนี้</p>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("❌ กลับไปเลือกใหม่", use_container_width=True):
                st.session_state.step = 'choose_char'
                st.session_state.gender = None
                st.rerun()
        with c2:
            if st.button("✅ ยืนยันตัวละคร", use_container_width=True, type="primary"):
                st.session_state.step = 'playing'
                st.rerun()


# ==========================================
# PHASE 3: เริ่มเนื้อเรื่องแบบแยก 3 เส้นทาง
# ==========================================
elif st.session_state.step == 'playing':
    data = st.session_state.char_data
    
    # แถบแสดงข้อมูลย่อด้านบนสุด (ยันยันแล้ว ห้ามเปลี่ยน)
    st.markdown(f"""
    <div style="background: #1e1e24; padding: 10px 15px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #444; display: flex; justify-content: space-between;">
        <span>👤 <b>ผู้เล่น:</b> {data['name']}</span>
        <span>⚧ <b>เพศ:</b> {data['gender']}</span>
        <span>🎂 <b>อายุ:</b> {data['age']} ปี</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 ปฐมบท: คดีปริศนาในค่ำคืนฝนตก")
    
    # ถ้ายังไม่ได้เลือกช้อยส์เนื้อเรื่อง ให้แสดงสถานการณ์และตัวเลือก 3 ทาง
    if st.session_state.choice_result is None:
        st.markdown("""
        <div class="story-box">
            คุณได้รับแจ้งเหตุฉุกเฉินให้มาตรวจสอบคฤหาสน์เก่าหลังหนึ่งในยามวิกาล บรรยากาศภายในวังเวงและมีกลิ่นประหลาดลอยออกมาจากห้องโถงใหญ่ 
            เบื้องหน้าของคุณมีประตู 3 บานที่นำไปสู่จุดเริ่มต้นการไขคดีที่แตกต่างกัน คุณจะตัดสินใจอย่างไร?
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### กรุณาเลือกเส้นทางของคุณ:")
        
        # 3 เส้นทางเลือก
        if st.button("🚪 เส้นทางที่ 1: พังประตูห้องโถงหลักบุกเข้าไปตรงๆ (สายบู๊/เผชิญหน้า)", use_container_width=True):
            st.session_state.choice_result = "path_1"
            st.rerun()
            
        if st.button("🔍 เส้นทางที่ 2: เดินอ้อมไปสำรวจหน้าต่างด้านข้างเพื่อหาหลักฐานเงียบๆ (สายสืบสวน/รอบคอบ)", use_container_width=True):
            st.session_state.choice_result = "path_2"
            st.rerun()
            
        if st.button("📞 เส้นทางที่ 3: ถอยออกมาตั้งหลักและโทรเรียกกำลังเสริมข้างนอก (สายปลอดภัย/ระแวดระวัง)", use_container_width=True):
            st.session_state.choice_result = "path_3"
            st.rerun()
            
    # แสดงผลลัพธ์ตามเส้นทางที่ผู้เล่นเลือก (3 เส้นทางแยก)
    else:
        result = st.session_state.choice_result
        
        if result == "path_1":
            st.markdown("""
            <div class="story-box" style="border-left-color: #ff4d4d;">
                <h3>⚡ ผลลัพธ์: เส้นทางที่ 1 (บุกตะลุยเข้าห้องโถงหลัก)</h3>
                <p>คุณถีบประตูเปิดผางเข้าไป เสียงไม้หักดังสนั่น! ภายในห้องคุณพบเงวปริศนากำลังยืนอยู่หน้าโต๊ะทำงานที่มีรอยเลือดสาดกระจาย 
                คนร้ายหันมามองคุณด้วยแววตาเหี้ยมเกรียม การปะทะและไล่ล่าจึงเริ่มต้นขึ้นทันทีก่อนที่คุณจะทันได้ตั้งตัว...</p>
                <p><b>[คุณปลดล็อกสถานะ: เส้นทางสายปะทะ - ความเสี่ยงสูง]</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        elif result == "path_2":
            st.markdown("""
            <div class="story-box" style="border-left-color: #4dabf7;">
                <h3>🔎 ผลลัพธ์: เส้นทางที่ 2 (สืบสวนรอบคอบจากหน้าต่าง)</h3>
                <p>คุณย่องไปที่หน้าต่างกระจกสีข้างคฤหาสน์อย่างเงียบเชียบ ใช้ไฟฉายส่องลอดเข้าไปข้างใน 
                คุณพบรอยนิ้วมือปริศนาและ "จดหมายขู่" วางทิ้งไว้บนขอบโต๊ะโดยที่คนร้ายยังไม่รู้ตัวว่าคุณแอบดูอยู่ 
                คุณได้หลักฐานชิ้นแรกเข้ากระเป๋าอย่างปลอดภัย!</p>
                <p><b>[คุณปลดล็อกสถานะ: เส้นทางสายนักสืบ - ได้รับเบาะแสลับ]</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        elif result == "path_3":
            st.markdown("""
            <div class="story-box" style="border-left-color: #fab005;">
                <h3>🛡️ ผลลัพธ์: เส้นทางที่ 3 (ถอยมารอคอยกำลังเสริม)</h3>
                <p>คุณตัดสินใจถอยออกมาที่รั้วบ้านเพื่อรอตำรวจหน่วยอื่นมารสมทบ แม้จะปลอดภัยจากอันตรายเฉพาะหน้า 
                แต่เมื่อตำรวจมาถึง คุณกลับพบว่าหลักฐานสำคัญทั้งหมดในห้องโถงถูกเผาทำลายหายไปอย่างไร้ร่องรอยเสียแล้ว...</p>
                <p><b>[คุณปลดล็อกสถานะ: เส้นทางสายปลอดภัย - พลาดเบาะแสสำคัญ]</b></p>
            </div>
            """, unsafe_allow_html=True)
            
        # ปุ่มสำหรับรีเซ็ตกลับไปลองเล่นเส้นทางอื่น (สำหรับเทส)
        if st.button("🔄 ลองเลือกเส้นทางใหม่อีกครั้ง"):
            st.session_state.choice_result = None
            st.rerun()
