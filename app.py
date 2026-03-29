import streamlit as st
import random
from salon_data import salon_post_ideas, post_endings, basic_hashtags, location_hashtags

st.set_page_config(page_title="Escondido Salon Posts", page_icon="✨", layout="centered")

st.title("🌟 Salon Post Helper")
st.markdown("### Quick, ready-to-post ideas for the salon 💇‍♀️")


# Helper functions
def get_random_post():
    all_posts = []
    for posts in salon_post_ideas.values():
        all_posts.extend(posts)
    return random.choice(all_posts)


def get_post_by_category(category):
    if category in salon_post_ideas:
        return random.choice(salon_post_ideas[category])
    return "Sorry, that category isn't available."


def get_hashtags():
    random_basic = random.sample(basic_hashtags, 5)
    return " ".join(random_basic + location_hashtags)


def generate_formatted_post(post, category=None):
    ending = random.choice(post_endings)
    hashtags = get_hashtags()
    title = f"{category.title()} Post Idea" if category else "Daily Salon Post Idea"

    return f"""
✨ {title} ✨

{post}

{ending}

{hashtags}
    """


# Main UI
option = st.radio(
    "Choose post type:",
    ["🎲 Random Post", "📋 Category Post"],
    horizontal=True
)

if option == "🎲 Random Post":
    if st.button("Generate Random Post", type="primary", use_container_width=True):
        post = get_random_post()
        formatted = generate_formatted_post(post)
        st.success("✅ Here's your random post!")
        st.text_area("Long-press to copy 👇", formatted, height=340)

else:  # Category Post
    category = st.selectbox(
        "Select Category:",
        options=list(salon_post_ideas.keys()),
        format_func=lambda x: x.title()
    )

    if st.button("Generate Category Post", use_container_width=True):
        post = get_post_by_category(category)
        formatted = generate_formatted_post(post, category)
        st.success("✅ Here's your category post!")
        st.text_area("Long-press to copy 👇", formatted, height=340)

st.divider()
st.caption("Built for the Escondido salon • Long-press the text box to copy on your phone ❤️")