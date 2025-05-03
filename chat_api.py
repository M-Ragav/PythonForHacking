from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Flutter to access this backend

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower().strip()
    reply = get_bot_reply(user_message)
    return jsonify({"reply": reply})

@app.route("/suggestions", methods=["GET"])
def get_suggestions():
    suggestions = list(responses.keys())  # Use global responses dictionary
    return jsonify({"suggestions": suggestions})



def get_bot_reply(message):
    responses = {
        "hello": "Hello! Welcome to our food-saving app. How can i assist you?",
        "hi": "Hi there! How can i help you today?",
        "good morning": "Good morning! How's your day going?",
        "good evening": "Good evening! How can i assist you?",
        "what can you do": "Our app helps reduce food waste by connecting users with expired-food delivery services. We offer food expiry detection, trust verification for delivery persons, and a reward system.",
        "how does the app work": "Our app scans food expiry dates using Ai, connects users to delivery persons for food redistribution, and verifies trust levels to ensure safety. Would you like more details?",
        "how do you check expiry": "We use Ai-powered image recognition to analyze food labels and estimate expiry dates.",
        "is it safe to eat expired food": "Some expired food is still safe to eat depending on the type and storage conditions. Our app categorizes food based on safety levels before redistribution.",
        "how do you verify delivery persons": "We verify delivery persons through identity checks, past records, and user ratings. Only trusted personnel can handle food deliveries.",
        "how can i become a delivery person": "You can register as a delivery person in our app. We require iD verification and past experience details before approval.",
        "is delivery free": "Delivery is free for food donations. For other cases, a small service fee applies.",
        "do i get rewards": "Yes! Users earn rewards for reducing food waste. You can redeem points for discounts or donations to charities.",
        "how do rewards work": "You collect points when you donate or receive food through our platform. These points can be redeemed for discounts, vouchers, or charitable donations.",
        "i found a bug": "We’re sorry for the issue. Please describe the bug so we can fix it quickly.",
        "how can i contact support": "You can reach our support team via the app or email us at support@foodsaveapp.com.",
        "who created this app": "This app was created by a team dedicated to reducing food waste and helping communities.",
        "how do i report a problem": "You can report a problem in the app settings under 'Report an issue.'",
        "can i track my deliveries": "Yes! We provide real-time tracking so you can monitor your food delivery status.",
        "what areas do you serve": "We currently operate in major cities, but we're expanding. Check our app for updated service areas.",
        "is this service available 24/7": "Our app is available 24/7, but delivery hours may vary based on location.",
        "how can i donate food": "You can list your surplus food on our platform, and we will connect you with people in need.",
        "what types of food can i donate": "You can donate packaged, dry, and perishable foods that are still safe for consumption.",
        "do i need to pay for donating food": "No! Donating food is completely free, and you might even earn rewards.",
        "how long does verification take for delivery persons": "Verification usually takes 24-48 hours, depending on document approval.",
        "how do i reset my password": "Go to the login page and click 'Forgot Password' to reset it.",
        "how can i update my profile": "Navigate to the settings menu and select 'Edit Profile.'",
        "can i delete my account": "Yes, you can delete your account in the settings, but all your data will be lost.",
        "what happens if i receive bad food": "Please report it immediately, and we will investigate the issue.",
        "can i schedule a delivery": "Yes, you can schedule food pickups and deliveries at your convenience.",
        "how do i cancel a delivery": "You can cancel deliveries within the app under 'My Orders.'",
        "can businesses donate food": "Yes, we welcome donations from businesses, restaurants, and supermarkets.",
        "how do i know if my food is safe to donate": "Our app provides guidelines on what food is safe to donate and how to store it.",
        "is my data safe on this app": "Yes, we prioritize user security and do not share personal information without consent.",
        "does this app work internationally": "Currently, we operate in selected regions, but we are expanding globally.",
        "do you partner with charities": "Yes, we collaborate with local charities to distribute food to those in need.",
        "how can i become a partner": "Businesses and charities can apply to become partners through our website or app.",
        "can i volunteer for food distribution": "Yes! Volunteers are always welcome to help with food deliveries and distribution.",
        "how do i earn trust points as a delivery person": "Trust points are earned based on successful deliveries, user reviews, and verification levels.",
        "what if i miss a scheduled delivery": "if you miss a delivery, you can reschedule or contact support for assistance.",
        "can i donate money instead of food": "Yes, we accept monetary donations that go toward food distribution programs.",
        "does this app charge users": "The app is free, but some services may have a small fee to cover operational costs.",
        "how do i sign up": "Download the app, sign up with your email or phone number, and start using our services.",
        "do i need an iD to register as a delivery person": "Yes, we require iD verification for safety reasons.",
        "how do i report a suspicious user": "You can report users through their profile page or contact support.",
        "what happens if a delivery is delayed": "We notify users of any delays and provide updates through the app.",
        "can i choose the food i want to receive": "Yes, you can select from available food donations based on your preferences.",
        "how do i contact the food donor": "You can chat with the donor directly within the app.",
        "is there a limit to how much food i can donate": "There is no limit, but we encourage responsible donations based on demand.",
        "do i get a receipt for my donations": "Yes, you will receive a digital receipt in your account.",
        "how does the app match donors with recipients": "Our Ai system matches donors with nearby recipients based on food type and location.",
        "can i block a user": "Yes, you can block or report users if you experience any issues.",
        "how do i leave a review for a delivery": "After completing a delivery, you can rate and review the experience in the app."
    }
    return responses.get(message, "i'm not sure. Can you clarify?")

if __name__ == "__main__":
    app.run(debug=True)