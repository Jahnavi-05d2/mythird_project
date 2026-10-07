import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# Title
st.title("🎬 Movie Ticket Booking System")
st.write("Book your movie tickets easily!")

# Movie selection
st.subheader("🎥 Select Movie")

movie = st.selectbox(
    "Choose a movie:",
    [
        "Pushpa 2",
        "RRR",
        "Baahubali",
        "Kalki 2898 AD",
        "Avatar"
    ]
)

# Ticket category
st.subheader("🎟️ Select Ticket Type")

ticket_type = st.selectbox(
    "Choose ticket category:",
    [
        "Regular",
        "Premium",
        "VIP"
    ]
)

# Ticket prices
ticket_prices = {
    "Regular": 150,
    "Premium": 250,
    "VIP": 400
}

price = ticket_prices[ticket_type]

# Number of tickets
st.subheader("👥 Number of Tickets")

tickets = st.number_input(
    "Enter number of tickets:",
    min_value=1,
    max_value=10,
    value=1
)

# Calculate total
total_price = price * tickets

# Book button
if st.button("🎟️ Book Tickets", use_container_width=True):

    st.divider()

    st.subheader("📋 Booking Summary")

    st.write(f"**🎬 Movie:** {movie}")
    st.write(f"**🎟️ Ticket Type:** {ticket_type}")
    st.write(f"**👥 Number of Tickets:** {tickets}")
    st.write(f"**💵 Price per Ticket:** ₹{price}")
    
    st.divider()

    st.success(
        f"### 💰 Total Price: ₹{total_price}"
    )

    st.info(
        "🎉 Your tickets have been successfully booked!"
    )

