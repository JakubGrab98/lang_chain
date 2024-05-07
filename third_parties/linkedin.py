import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles

    Args:
        linkedin_profile_url (str): _description_
        mock (bool, optional): _description_. Defaults to False.
    """

    linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    response = requests.get(
        linkedin_profile_url,
        timeout=10,
    )
    
    data = response.json()

    data = {
        key: value
        for key, value in data.items()
        if value not in ([], "", "", None)
        and key not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
        )
    )