import streamlit as st

# Define a list of side hustle ideas with detailed descriptions
side_hustles = [
    {
        "name": "Freelance Writing",
        "description": "Write articles, blog posts, or content for websites and businesses. This can include various topics and industries, and you can work with multiple clients to build a freelance writing career."
    },
    {
        "name": "Online Tutoring",
        "description": "Teach subjects you're knowledgeable in to students online. You can offer one-on-one or group tutoring sessions and choose your preferred subjects and grade levels."
    },
    {
        "name": "Graphic Design",
        "description": "Create logos, banners, and other graphic materials for clients. Graphic designers often work on a project basis and can offer their services for branding, marketing, and more."
    },
    {
        "name": "Photography",
        "description": "Offer photography services for events, portraits, or stock photography. You can specialize in various photography niches, including weddings, family portraits, or selling your photos online."
    },
    {
        "name": "Social Media Management",
        "description": "Manage social media accounts for businesses and individuals. This involves creating content, scheduling posts, and engaging with followers to grow online presence."
    },
    {
        "name": "Dropshipping",
        "description": "Start an e-commerce store and sell products without holding inventory. Dropshippers partner with suppliers to fulfill orders, making it a low-risk way to start an online business."
    },
    {
        "name": "Freelance Web Development",
        "description": "Build websites or web applications for clients on a freelance basis. Web developers can specialize in frontend, backend, or full-stack development, working on various projects."
    },
    {
        "name": "Consulting",
        "description": "Provide expertise in a specific field such as business, marketing, or finance. Consultants offer guidance, analysis, and recommendations to clients seeking professional advice."
    },
    {
        "name": "Handmade Crafts",
        "description": "Create and sell handmade crafts or artwork on platforms like Etsy. This side hustle allows you to showcase your creativity and craft unique items for sale."
    },
    {
        "name": "Delivery Driver",
        "description": "Work for food delivery or courier services in your spare time. Delivery drivers pick up and drop off orders, earning money for each delivery completed."
    }
]

# Streamlit app
st.title("Side Hustle Ideas for Gavin")

st.write("Are you looking for a side hustle, Gavin? Here are some ideas to consider:")

# Display side hustle options with detailed descriptions in expanders
for hustle in side_hustles:
    with st.expander(hustle["name"]):
        st.write(hustle["description"])

st.write("Feel free to explore these options and choose the one that best suits your skills and interests!")
