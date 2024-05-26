from english_words import get_english_words_set
from random import choice
import wikipedia as wp
import textwrap

# Constants
web2lowerset = list(get_english_words_set(['web2'], lower=True))

def print_summary(query, summary):
    print(f'\n{query.capitalize()} Summary:')
    print('-' * 50)
    wrapped_summary = textwrap.fill(summary, width=80)
    print(wrapped_summary)
    print('-' * 50)

def random_query():
    while True:
        query = choice(web2lowerset)
        try:
            summary = wp.summary(query)
            print_summary(query, summary)
            break
        except wp.DisambiguationError as e:
            print(f'Ambiguous term: {query}. Trying another random query.')
        except wp.PageError as e:
            print(f'No Wikipedia page found for {query}. Trying another random query.')

def set_query(query):
    try:
        summary = wp.summary(query)
        print_summary(query, summary)
    except wp.DisambiguationError as e:
        print(f'Ambiguous term: {query}. Try a more specific query.')
    except wp.PageError as e:
        print(f'No Wikipedia page found for {query}.')

print("Wikipedia Summarizer")
while True:
    query = input("\n Pick an article to summarize, type 'random' to summarize a random article, or type 'e' to end: ")
    if query.lower() == "random": random_query() 
    elif query.lower() == "e": quit()
    else: set_query(query)