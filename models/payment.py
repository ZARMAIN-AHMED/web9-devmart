import stripe
import streamlit as st

stripe.api_key = st.secrets["STRIPE_SECRET_KEY"]

class Payment:
    def __init__(self, user, amount):
        self.user = user
        self.amount = int(amount * 100)

    def process_payment(self):
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "DevMart Purchase",
                            "description": f"Order by {self.user.name}",
                        },
                        "unit_amount": self.amount,
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url="https://devmart-demo.streamlit.app/success",
                cancel_url="https://devmart-demo.streamlit.app/cancel",
                customer_email=self.user.email
            )
            return session.url
        except Exception as e:
            print("Stripe error:", e)
            return None

