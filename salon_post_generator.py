import random
from salon_data import salon_post_ideas, post_endings, basic_hashtags, location_hashtags


class SalonPostGenerator:
    def __init__(self):
        self.post_ideas = salon_post_ideas
        self.post_endings = post_endings
        self.basic_hashtags = basic_hashtags
        self.location_hashtags = location_hashtags

    def get_random_post(self):
        """Returns a random post from any category"""
        all_posts = []
        for category_posts in self.post_ideas.values():
            all_posts.extend(category_posts)
        return random.choice(all_posts)

    def generate_category_post(self, category):
        """Generates a nicely formatted post for a specific category"""
        post = self.generate_category_post(category)

        if "Sorry" in post:  # if category not found
            return post


        # Use the same varied endings as random posts
        ending = random.choice(self.post_endings)
        hashtags = self.get_hashtags()

        formatted_post = f"""
✨ {category.title()} Post Idea ✨

{post}

{ending}

{hashtags}
        """
        return formatted_post

    def get_hashtags(self):
        """Returns 5 random basic hashtags + all location hashtags"""
        # Pick 5 random basic hashtags
        random_basic = random.sample(self.basic_hashtags, 5)
        # Combine with location hashtags
        all_hashtags = random_basic + self.location_hashtags
        return " ".join(all_hashtags)

    def generate_daily_post(self):
        """Generates a nicely formatted post with varied endings"""
        post = self.get_random_post()
        ending = random.choice(self.post_endings)
        hashtags = self.get_hashtags()

        formatted_post = f"""
✨ Daily Salon Post Idea ✨

{post}

{ending}

{hashtags}
                                """
        return formatted_post