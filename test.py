import streamlit as st

# 1. กำหนดหัวข้อเว็บ
st.title("ระบบคำนวณราคาสินค้าอัจฉริยะ 🛒")

# 2. สร้างฐานข้อมูลรายการสินค้าและราคา (Dictionary)
menu_items = {
    "ชานมไข่มุก (Bubble Tea)": 45,
    "ชาเขียวมัทฉะ (Matcha Latte)": 55,
    "กาแฟอเมริกาโน่ (Americano)": 50,
    "เค้กช็อกโกแลต (Chocolate Cake)": 85,
    "ครัวซองต์ (Croissant)": 60
}

# 3. สร้างช่องเลือกหลายตัวเลือก (Multiselect)
selected_items = st.multiselect(
    label="เลือกรายการสินค้าที่คุณต้องการซื้อ:",
    options=list(menu_items.keys()),
    default=None,
    placeholder="คลิกเพื่อเลือกสินค้า..."
)

# 4. ส่วนการคำนวณเงิน
if selected_items:
    st.write("---")
    st.subheader("📋 รายการที่คุณเลือก:")
    
    total_price = 0
    
    # วนลูปแสดงรายการที่เลือกพร้อมราคา และบวกราคารวม
    for item in selected_items:
        price = menu_items[item]
        total_price += price
        st.write(f"- {item}: *{price} บาท*")
        
    st.write("---")
    # แสดงราคารวมทั้งหมดด้วยตัวหนาและขนาดใหญ่
    st.markdown(f"### 💰 ราคารวมทั้งหมด: {total_price:,} บาท")
else:
    st.info("กรุณาเลือกสินค้าอย่างน้อย 1 รายการเพื่อคำนวณเงิน")
