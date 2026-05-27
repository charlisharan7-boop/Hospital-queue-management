import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# --- DATABASE SETUP ---
# No installation needed for sqlite3 as it is built into Python
conn = sqlite3.connect('hospital_hackathon.db', check_same_thread=False)
cursor = conn.cursor()

def init_db():
    # Doctors Table with Education and Experience
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            specialty TEXT,
            education TEXT,
            experience INTEGER,
            working_hours TEXT,
            status TEXT DEFAULT 'Available',
            room_no TEXT
        )
    ''')

    # Queue Table (Priority: 1-Emergency, 2-Medium, 3-Low)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            phone TEXT,
            priority INTEGER, 
            doctor_id INTEGER,
            arrival_time TEXT,
            FOREIGN KEY(doctor_id) REFERENCES doctors(id)
        )
    ''')
    
    # Pre-fill Doctors for the Hackathon Demo
    cursor.execute("SELECT COUNT(*) FROM doctors")
    if cursor.fetchone()[0] == 0:
        docs = [
            (1, 'Dr. Arisya Sharma', 'Cardiologist', 'MBBS, MD (Cardiology) - AIIMS', 12, '09:00 - 17:00', 'Available', '302-A'),
            (2, 'Dr. Vikram Seth', 'Neurologist', 'MBBS, Ph.D. - Stanford Medical', 15, '10:00 - 18:00', 'Available', '405-B'),
            (3, 'Dr. Sneha Rao', 'Pediatrician', 'MBBS, DCH - CMC Vellore', 8, '08:00 - 14:00', 'Available', '102-C')
        ]
        cursor.executemany("INSERT INTO doctors VALUES (?,?,?,?,?,?,?,?)", docs)
    conn.commit()

init_db()

# --- UI DESIGN ---
st.set_page_config(page_title="Smart Care Hospital", layout="wide")
st.title("🏥 Smart Healthcare & Priority Management")

# --- SIDEBAR: PATIENT REGISTRATION ---
st.sidebar.header("📝 Patient Registration")
p_name = st.sidebar.text_input("Patient Full Name")
p_phone = st.sidebar.text_input("Mobile Number")
p_priority = st.sidebar.selectbox("Severity / Priority", [1, 2, 3], 
                                  format_func=lambda x: {1: "🚨 EMERGENCY (High)", 2: "⚠️ Urgent (Medium)", 3: "✅ Routine (Low)"}[x])

# Get doctor list for dropdown
cursor.execute("SELECT id, name FROM doctors")
doctor_options = {name: id for id, name in cursor.fetchall()}
selected_doc_name = st.sidebar.selectbox("Consulting Doctor", list(doctor_options.keys()))

if st.sidebar.button("Confirm Booking"):
    if p_name and p_phone:
        now = datetime.now().strftime("%I:%M %p")
        cursor.execute("INSERT INTO queue (patient_name, phone, priority, doctor_id, arrival_time) VALUES (?, ?, ?, ?, ?)",
                       (p_name, p_phone, p_priority, doctor_options[selected_doc_name], now))
        conn.commit()
        st.sidebar.success(f"Ticket generated for {p_name}!")
        st.rerun()
    else:
        st.sidebar.error("Please fill all details.")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📋 Public Queue Board", "👨‍⚕️ Find Your Doctor", "🛡️ Admin Portal"])

with tab1:
    st.header("Live Waiting List")
    st.info("Emergency cases (🚨) are automatically moved to the front of the queue.")
    
    # Priority Logic: Sort by Priority (1 is top) then by Arrival Time (ID)
    query = """
    SELECT q.patient_name, 
           CASE q.priority WHEN 1 THEN '🚨 EMERGENCY' WHEN 2 THEN '⚠️ Urgent' ELSE '✅ Routine' END as Status,
           d.name as Assigned_Doctor, 
           q.arrival_time 
    FROM queue q 
    JOIN doctors d ON q.doctor_id = d.id 
    ORDER BY q.priority ASC, q.id ASC
    """
    df_queue = pd.read_sql_query(query, conn)
    
    if not df_queue.empty:
        st.dataframe(df_queue, use_container_width=True, hide_index=True)
    else:
        st.write("No patients currently waiting.")

with tab2:
    st.header("Specialist Profiles & Availability")
    df_docs = pd.read_sql_query("SELECT * FROM doctors", conn)
    
    for _, row in df_docs.iterrows():
        status_color = "🟢" if row['status'] == 'Available' else "🔴"
        with st.expander(f"{status_color} {row['name']} - {row['specialty']}"):
            c1, c2 = st.columns(2)
            c1.markdown(f"**Education:** {row['education']}")
            c1.markdown(f"**Experience:** {row['experience']} Years")
            c2.markdown(f"**Room No:** {row['room_no']}")
            c2.markdown(f"**Hours:** {row['working_hours']}")

with tab3:
    st.header("Doctor's Desk")
    st.subheader("Next Patient Actions")
    
    # Fetch the very next patient based on priority
    cursor.execute("""
        SELECT q.id, q.patient_name, q.phone, d.name 
        FROM queue q 
        JOIN doctors d ON q.doctor_id = d.id 
        ORDER BY q.priority ASC, q.id ASC LIMIT 1
    """)
    next_up = cursor.fetchone()
    
    if next_up:
        st.write(f"**Current Next:** {next_up[1]} for {next_up[3]}")
        if st.button("Serve & Send SMS Notification", type="primary"):
            # SIMULATED SMS LOGIC
            st.toast(f"SMS Alert sent to {next_up[2]}", icon="📱")
            st.success(f"Now serving {next_up[1]}. Please clear the room.")
            
            # Remove from DB
            cursor.execute("DELETE FROM queue WHERE id = ?", (next_up[0],))
            conn.commit()
            st.rerun()
    else:
        st.write("The queue is currently clear.")

    st.divider()
    st.subheader("Update Doctor Status")
    doc_to_update = st.selectbox("Select Your Name", list(doctor_options.keys()), key="update_status")
    new_stat = st.radio("Current Status", ["Available", "Busy"], horizontal=True)
    if st.button("Update Availability"):
        cursor.execute("UPDATE doctors SET status = ? WHERE name = ?", (new_stat, doc_to_update))
        conn.commit()
        st.success("Status Updated.")
        st.rerun()