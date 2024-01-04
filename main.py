import webbrowser
import colorama
from colorama import Fore, Style
import wikipedia

colorama.init(autoreset=True)

def main():

    print(colorama.ansi.clear_screen())
    while True:
        try:
            random_article_title = wikipedia.random() #Fetch random article title using Wikipedia library
            random_article_summary = wikipedia.summary(random_article_title)

            print("\nRandom Wikipedia Article:")
            print(Fore.YELLOW + f"Title: {random_article_title}")
            print(Style.RESET_ALL + f"Summary: {random_article_summary[:200]}") #Displaying the first 200 characters of the summary

            open_browser = input("\nDo you want to open this article in your web browser? (yes/no): ").lower()

            if open_browser == "yes":
                article_url = f"https://en.wikipedia.org/wiki/{random_article_title.replace(' ', '_')}"
                webbrowser.open(article_url)

            elif open_browser == "no":
                next_summary = input("Would you like another summary? (yes/no): ").lower()

                if next_summary == "yes":
                    continue
                elif next_summary == "no":
                    break
            break
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"DisambiguationError: {e.options}. Please try again.")
        except wikipedia.exceptions.PageError:
            print("Error: Unable to fetch article information. Please try again.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

main()
