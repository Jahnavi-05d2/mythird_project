import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍔",
    layout="centered"
)

# Restaurant title
st.title("🍔 Restaurant Bill Generator")
st.write("Select your food items and generate your bill.")

# Menu with prices
menu = {
    "🍕 Pizza": 250,
    "🍔 Burger": 150,
    "🍝 Pasta": 180,
    "🍟 French Fries": 100,
    "🥤 Cold Drink": 60,
    "🍨 Ice Cream": 90
}

st.subheader("🍽️ Select Food Items")

bill_items = []
subtotal = 0

# Food selection
for item, price in menu.items():

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"**{item}** - ₹{price}")

    with col2:
        quantity = st.number_input(
            "Qty",
            min_value=0,
            max_value=10,
            value=0,
            key=item
        )

    if quantity > 0:
        item_total = price * quantity

        bill_items.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "total": item_total
        })

        subtotal += item_total


# Discount
st.subheader("💸 Discount")

discount_percent = st.number_input(
    "Enter discount (%)",
    min_value=0.0,
    max_value=50.0,
    value=0.0,
    step=1.0
)

discount = subtotal * discount_percent / 100

# Tax
st.subheader("🧾 Tax")

tax_percent = st.number_input(
    "GST (%)",
    min_value=0.0,
    max_value=30.0,
    value=5.0,
    step=1.0
)

taxable_amount = subtotal - discount
tax = taxable_amount * tax_percent / 100

# Grand total
grand_total = taxable_amount + tax


# Generate bill
if st.button("🧾 Generate Bill", use_container_width=True):

    if len(bill_items) == 0:
        st.warning("Please select at least one food item.")

    else:
        st.divider()

        st.subheader("🍽️ FINAL BILL")

        # Bill table
        st.write("| Item | Price | Qty | Total |")
        st.write("|---|---:|---:|---:|")

        for item in bill_items:
            st.write(
                f"| {item['item']} | "
                f"₹{item['price']:.2f} | "
                f"{item['quantity']} | "
                f"₹{item['total']:.2f} |"
            )

        st.divider()

        # Bill summary
        st.write(f"**Subtotal:** ₹{subtotal:.2f}")
        st.write(
            f"**Discount ({discount_percent:.0f}%):** "
            f"- ₹{discount:.2f}"
        )
        st.write(
            f"**GST ({tax_percent:.0f}%):** "
            f"₹{tax:.2f}"
        )

        st.success(
            f"## 💰 Grand Total: ₹{grand_total:.2f}"
        )

        st.balloons()

        st.write("### 🙏 Thank you for visiting!")

