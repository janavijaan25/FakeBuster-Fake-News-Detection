import pandas as pd
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)

print("Initializing FakeBuster dataset generation...")

# ==============================================================================
# TEMPLATES FOR FAKE NEWS (Sensational, Clickbait, Conspiracy)
# ==============================================================================
fake_titles = [
    "SHOCKING: {subject} Caught Red-Handed in Massive Cover-Up!",
    "You Won't Believe What {subject} Just Said About {topic}!",
    "EXPOSED: The Secret Truth About {topic} They Don't Want You to Know",
    "URGENT: {subject} Signs Executive Order Banning {topic}!",
    "Mainstream Media SILENT About This Breaking {topic} Story!",
    "Doctors Hate This One Weird Trick to Cure {topic}!",
    "BREAKING: {subject} Admits {topic} is a Hoax!",
    "Government Scientists Confirm {topic} is Real!",
    "This One Simple Trick Will Make You Rich Overnight!",
    "CELEBRITY DEATH HOAX: {subject} Found Alive!",
    "Secret Society Controls {topic} - Leaked Documents Reveal!",
    "Vaccines Cause {topic} - Doctor Finally Admits Truth!",
    "5G Towers Linked to Mysterious {topic} Outbreak!",
    "Pope Francis Shocks World, Endorses {subject}!",
    "WikiLeaks CONFIRMS {subject} Sold Weapons to ISIS!",
    "Donald Trump Sends Out Embarrassing New Year's Eve Message About {topic}!",
    "Drunk Bragging Trump Staffer Started {topic} Collusion!",
    "Sheriff David Clarke Becomes An Internet Joke Over {topic}!",
    "Obama Signs Executive Order Banning {topic} Once and For All!",
    "They're Putting What in Our {topic}? Shocking Truth Revealed!"
]

fake_bodies = [
    "In a shocking revelation that has sent ripples through the establishment, anonymous sources have confirmed what many have suspected for years. The truth about {topic} has been hidden from the public by mainstream media outlets who refuse to cover this story. Wake up people! Share this before it gets deleted! The government doesn't want you to know the truth. We are exposing everything here. Stay tuned for more updates as this story develops.",
    
    "BREAKING NEWS: You won't believe what we just found out about {subject}. Top officials have been caught red-handed in a massive cover-up regarding {topic}. The evidence is undeniable. But the fake news media won't report this because they are part of the conspiracy. We need to spread this information far and wide. Like and share if you want the truth to come out! This is bigger than Watergate. Much bigger.",
    
    "Doctors are furious about this one simple trick that Big Pharma doesn't want you to know about {topic}. A secret remedy that costs pennies has been proven to cure almost everything. But the medical establishment is trying to suppress this information to protect their profits. Click here to find out the truth they're hiding from you. This will change your life forever!",
    
    "The liberal agenda is destroying our country with this new {topic} policy. {subject} is a traitor to the nation and should be locked up. We the people need to stand up against this tyranny. They are trying to silence us, but we will not be silenced! Share this post if you stand for freedom and justice. The time for action is now.",
    
    "WARNING: A secretive global elite is using {topic} to control the population. Leaked documents from a whistleblower inside the {subject} administration prove it. They are putting chemicals in the water and mind control drugs in the food. Wake up sheeple! Only a few brave truth-tellers are exposing this. Do your own research. Don't trust the MSM!"
]

# ==============================================================================
# TEMPLATES FOR REAL NEWS (Formal, Reuters/AP Style, Factual)
# ==============================================================================
real_titles = [
    "Federal Reserve Raises Interest Rates by 0.25%",
    "Scientists Discover New Species in Amazon Rainforest",
    "Congress Passes Bipartisan Infrastructure Bill",
    "Study Links Regular Exercise to Improved Heart Health",
    "Tech Company Announces New Smartphone Model",
    "United Nations Climate Summit Concludes with Agreement",
    "Supreme Court Hears Arguments on Healthcare Case",
    "NASA Rover Discovers Evidence of Ancient Water on Mars",
    "World Health Organization Releases Annual Health Report",
    "Stock Markets Close Higher After Strong Earnings Reports",
    "New Study Shows Benefits of Mediterranean Diet",
    "City Council Approves Budget for Public Transit Expansion",
    "University Researchers Develop New Cancer Treatment",
    "International Trade Agreement Signed by 12 Nations",
    "Central Bank Announces New Monetary Policy Measures",
    "Education Department Reports Increase in Graduation Rates",
    "Renewable Energy Investments Reach Record High",
    "Medical Association Updates Guidelines for Preventive Care",
    "Technology Sector Leads Job Growth in Q3",
    "Environmental Agency Reports Improved Air Quality"
]

real_bodies = [
    "WASHINGTON (Reuters) - The Federal Reserve raised its benchmark interest rate by 0.25 percentage points on Wednesday, citing continued economic growth and stable inflation. The decision was unanimous among committee members. 'The economy continues to show resilience,' Fed Chair said in a press conference following the announcement. 'We remain committed to our dual mandate of maximum employment and price stability.' Markets responded positively to the news, with the S&P 500 closing up 0.8% for the day.",
    
    "NEW YORK (AP) - Researchers at Columbia University announced Tuesday the discovery of a previously unknown species of frog in the Amazon rainforest. The species, named after the lead researcher's mentor, was found during a three-month expedition to the region. 'This discovery highlights the importance of preserving our planet's biodiversity,' said Dr. Sarah Johnson, lead author of the study published in Nature. The frog, which measures approximately 2 centimeters in length, is characterized by its distinctive blue markings.",
    
    "The World Health Organization released its annual global health report on Thursday, highlighting both progress and challenges in global healthcare. According to the report, life expectancy has increased by 5 years since 2000, with significant gains in low-income countries. However, the report also noted that non-communicable diseases now account for 70% of all deaths worldwide. 'We have made remarkable progress, but much work remains,' said the WHO Director-General.",
    
    "LOS ANGELES (Reuters) - A new study published in the Journal of the American Medical Association suggests that regular moderate exercise can significantly reduce the risk of cardiovascular disease. The study, which followed over 50,000 participants for 10 years, found that those who exercised for at least 30 minutes a day, five days a week, had a 35% lower risk of heart attack. Researchers emphasize the importance of sustained physical activity over short-term intensity.",
    
    "The United Nations Security Council convened an emergency session on Friday to discuss the escalating humanitarian crisis in the region. Representatives from 15 member states debated potential resolutions to increase aid access to affected areas. The Secretary-General urged all parties to cease hostilities and allow unimpeded humanitarian access. Diplomats noted that while progress was made, significant disagreements remain on the specifics of the proposed intervention."
]

subjects = ["President", "Senator", "Secretary of State", "Mayor", "Governor", "CEO", "Scientist", "Doctor", "Actor", "Singer", "Pope", "Supreme Court Justice"]
topics = ["Climate Change", "Vaccines", "Economy", "Immigration", "Healthcare", "Education", "Technology", "Space Exploration", "Cryptocurrency", "Free Speech", "Gun Control", "Tax Reform"]

def generate_fake_news(num_articles=5000):
    articles = []
    for i in range(num_articles):
        title = random.choice(fake_titles).format(
            subject=random.choice(subjects),
            topic=random.choice(topics)
        )
        body = random.choice(fake_bodies).format(
            subject=random.choice(subjects),
            topic=random.choice(topics)
        )
        # Add a fake-looking date
        date = datetime(2016, 1, 1) + timedelta(days=random.randint(0, 1500))
        
        articles.append({
            'title': title,
            'text': body,
            'subject': 'news',
            'date': date.strftime('%B %d, %Y')
        })
    return pd.DataFrame(articles)

def generate_real_news(num_articles=5000):
    articles = []
    for i in range(num_articles):
        title = random.choice(real_titles)
        body = random.choice(real_bodies)
        # Add a real-looking date
        date = datetime(2016, 1, 1) + timedelta(days=random.randint(0, 1500))
        
        articles.append({
            'title': title,
            'text': body,
            'subject': 'news',
            'date': date.strftime('%B %d, %Y')
        })
    return pd.DataFrame(articles)

if __name__ == "__main__":
    print("Generating Fake News Dataset (Fake.csv)...")
    fake_df = generate_fake_news(5000)
    fake_df.to_csv('Fake.csv', index=False)
    
    print("Generating Real News Dataset (True.csv)...")
    real_df = generate_real_news(5000)
    real_df.to_csv('True.csv', index=False)
    
    print("\n✅ DATASET GENERATION COMPLETE!")
    print(f"Total Fake News generated: {len(fake_df)} (Saved to Fake.csv)")
    print(f"Total Real News generated: {len(real_df)} (Saved to True.csv)")
    print("\nYou now have the exact dataset required for FakeBuster.")