import pandas as pd
import streamlit as st

NAME = "Divyansh Gupta"
PROGRAMME = "PGDM"

st.set_page_config(page_title=f"{NAME} | e-Portfolio", page_icon="📁", layout="centered")

# ---------- Data (from the Meridian HCM business model; illustrative case assumptions) ----------
sbu = pd.DataFrame(
    {"Revenue (₹ Cr)": [45, 35, 20]},
    index=["Infrastructure & Platform", "Enterprise Apps", "Security & Data"],
)
growth = pd.DataFrame(
    {"Revenue (₹ Cr)": [100, 140, 190, 255, 350], "Employees": [250, 350, 475, 638, 875]},
    index=["FY27", "FY28", "FY29", "FY30", "FY31"],
)
rupee_100 = pd.DataFrame(
    {"₹ out of every ₹100": [62.5, 12, 8, 7, 4, 5, 1.5]},
    index=["People", "Tech & cloud", "Sales & marketing", "Delivery", "Office", "R&D / legal", "Profit"],
)

# ---------- Header ----------
st.title(NAME)
st.caption(f"{PROGRAMME}  |  Meridian Forward  |  Human Capital Management e-Portfolio")
st.write("A short look at the business I worked on, the budget behind it, and what I learned about hiring.")

tab1, tab2, tab3 = st.tabs(["🏢 The Business", "💰 Budget", "💡 My Reflection"])

# ---------- Tab 1: The business ----------
with tab1:
    st.subheader("Meridian Intelligence")
    st.write("A cloud computing software company. Customers pay annual subscriptions, and growth in revenue drives growth in people.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Revenue", "₹100 Cr")
    c2.metric("Employees", "250")
    c3.metric("Customers", "200")
    c4.metric("Revenue / person", "₹40 L")

    st.markdown("**Revenue by business unit (₹ Cr)**")
    st.bar_chart(sbu, horizontal=True)

    st.markdown("**Five-year plan**")
    metric = st.radio("Show", ["Revenue (₹ Cr)", "Employees"], horizontal=True, label_visibility="collapsed")
    st.line_chart(growth[[metric]])
    st.caption("All figures are illustrative case assumptions.")

# ---------- Tab 2: Budget ----------
with tab2:
    st.subheader("Where the money goes")
    c1, c2, c3 = st.columns(3)
    c1.metric("Operating cost", "₹98.5 Cr")
    c2.metric("People cost", "₹62.5 Cr")
    c3.metric("Operating profit", "₹1.5 Cr", "1.5% margin", delta_color="off")

    st.markdown("**Every ₹100 of revenue**")
    st.bar_chart(rupee_100)
    st.write("Most of the budget is people. That is why hiring the right person matters.")

    st.subheader("The cost of getting people wrong")
    c1, c2, c3 = st.columns(3)
    c1.metric("Yearly loss", "₹11.6 Cr", help="Exits ₹8 Cr + slow ramp-up ₹3.6 Cr")
    c2.metric("Possible saving", "₹6.1 Cr")
    c3.metric("Programme cost", "₹2.4 Cr")
    st.write(
        "Faster onboarding, keeping critical talent and growing our own managers could "
        "save about ₹3.7 Cr a year after costs. These are estimates, not guarantees."
    )

# ---------- Tab 3: Reflection ----------
with tab3:
    st.subheader("What I learned in AS3")

    with st.expander("1. Start with the work, not the vacancy", expanded=True):
        st.write(
            "Meridian earns when client work is completed and accepted. So each role needs "
            "clear **KRAs, KPIs and KSABs** that show what the person must know, do and be."
        )

    with st.expander("2. The numbers made me rethink my first decision", expanded=True):
        st.write(
            "My first idea was to fill specialist gaps with people already in the team, and I still "
            "think that is a good start. But the overall numbers looked fine while real gaps remained "
            "in data preparation, QA and legacy knowledge. Meridian also has about **40 critical roles** "
            "that the business depends on."
        )
        st.write("So I look at the **skills available**, not just total budget or headcount.")

    with st.expander("3. Hiring is only the beginning", expanded=True):
        st.write(
            "After hiring, people need support, learning and a reason to stay."
        )
        a, b, c = st.columns(3)
        a.info("**Perform**\n\nClear KPIs, check-ins, coaching")
        b.info("**Stay engaged**\n\nFair workload and rewards")
        c.info("**Keep knowledge**\n\nProper handovers when people leave")

    st.success("**Next step (AS4):** connect hiring, readiness, performance, learning and retention into one employee journey.")

st.divider()
st.caption(f"{NAME}  |  Meridian Forward  |  AS3 e-Portfolio")
