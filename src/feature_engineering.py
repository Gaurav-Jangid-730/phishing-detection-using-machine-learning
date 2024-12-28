# import tldextract
# import pandas
# import socket

# def extract_url_features(url):
#     features = {}
    
#     # Count of specific characters in the URL
#     features['qty_dot_url'] = url.count('.')
#     features['qty_hyphen_url'] = url.count('-')
#     features['qty_underline_url'] = url.count('_')
#     features['qty_slash_url'] = url.count('/')
#     features['qty_questionmark_url'] = url.count('?')
#     features['qty_equal_url'] = url.count('=')
#     features['qty_at_url'] = url.count('@')
#     features['qty_and_url'] = url.count('&')
#     features['qty_exclamation_url'] = url.count('!')
#     features['qty_space_url'] = url.count(' ')
#     features['qty_tilde_url'] = url.count('~')
#     features['qty_comma_url'] = url.count(',')
#     features['qty_plus_url'] = url.count('+')
#     features['qty_asterisk_url'] = url.count('*')
#     features['qty_hashtag_url'] = url.count('#')
#     features['qty_dollar_url'] = url.count('$')
#     features['qty_percent_url'] = url.count('%')
#     features['qty_tld_url'] = len(tldextract.extract(url).suffix)  # Count of TLD

#     # Length of the URL
#     features['length_url'] = len(url)
    
#     return features

# def extract_domain_features(domain):
#     features = {}
    
#     # Count of specific characters in the domain
#     features['qty_dot_domain'] = domain.count('.')
#     features['qty_hyphen_domain'] = domain.count('-')
#     features['qty_underline_domain'] = domain.count('_')
#     features['qty_slash_domain'] = domain.count('/')
#     features['qty_questionmark_domain'] = domain.count('?')
#     features['qty_equal_domain'] = domain.count('=')
#     features['qty_at_domain'] = domain.count('@')
#     features['qty_and_domain'] = domain.count('&')
#     features['qty_exclamation_domain'] = domain.count('!')
#     features['qty_space_domain'] = domain.count(' ')
#     features['qty_tilde_domain'] = domain.count('~')
#     features['qty_comma_domain'] = domain.count(',')
#     features['qty_plus_domain'] = domain.count('+')
#     features['qty_asterisk_domain'] = domain.count('*')
#     features['qty_hashtag_domain'] = domain.count('#')
#     features['qty_dollar_domain'] = domain.count('$')
#     features['qty_percent_domain'] = domain.count('%')
#     features['qty_vowels_domain'] = domain.count('a','e','i','o','u','A','E','I','O','U')
#     # Length of the domain
#     features['domain_length'] = len(domain)

#     # Check if domain is an IP address (simplified check)
#     features['domain_in_ip'] = int(is_ip(domain))
#     features['server_client_domain'] = 0
#     return features

# def extract_directory_features(directory):
#     features = {}
    
#     # Count of specific characters in the directory path
#     features['qty_dot_directory'] = directory.count('.')
#     features['qty_hyphen_directory'] = directory.count('-')
#     features['qty_underline_directory'] = directory.count('_')
#     features['qty_slash_directory'] = directory.count('/')
#     features['qty_questionmark_directory'] = directory.count('?')
#     features['qty_equal_directory'] = directory.count('=')
#     features['qty_at_directory'] = directory.count('@')
#     features['qty_and_directory'] = directory.count('&')
#     features['qty_exclamation_directory'] = directory.count('!')
#     features['qty_space_directory'] = directory.count(' ')
#     features['qty_tilde_directory'] = directory.count('~')
#     features['qty_comma_directory'] = directory.count(',')
#     features['qty_plus_directory'] = directory.count('+')
#     features['qty_asterisk_directory'] = directory.count('*')
#     features['qty_hashtag_directory'] = directory.count('#')
#     features['qty_dollar_directory'] = directory.count('$')
#     features['qty_percent_directory'] = directory.count('%')

#     # Length of the directory path
#     features['directory_length'] = len(directory)

#     return features

# def extract_file_features(file):
#     features = {}

#     # Count of specific characters in the file name
#     features['qty_dot_file'] = file.count('.')
#     features['qty_hyphen_file'] = file.count('-')
#     features['qty_underline_file'] = file.count('_')
#     features['qty_slash_file'] = file.count('/')
#     features['qty_questionmark_file'] = file.count('?')
#     features['qty_equal_file'] = file.count('=')
#     features['qty_at_file'] = file.count('@')
#     features['qty_and_file'] = file.count('&')
#     features['qty_exclamation_file'] = file.count('!')
#     features['qty_space_file'] = file.count(' ')
#     features['qty_tilde_file'] = file.count('~')
#     features['qty_comma_file'] = file.count(',')
#     features['qty_plus_file'] = file.count('+')
#     features['qty_asterisk_file'] = file.count('*')
#     features['qty_hashtag_file'] = file.count('#')
#     features['qty_dollar_file'] = file.count('$')
#     features['qty_percent_file'] = file.count('%')

#     # Length of the file name
#     features['file_length'] = len(file)

#     return features

# def extract_param_features(params):
#     features = {}
    
#     # Count of specific characters in the parameters
#     features['qty_dot_params'] = params.count('.')
#     features['qty_hyphen_params'] = params.count('-')
#     features['qty_underline_params'] = params.count('_')
#     features['qty_slash_params'] = params.count('/')
#     features['qty_questionmark_params'] = params.count('?')
#     features['qty_equal_params'] = params.count('=')
#     features['qty_at_params'] = params.count('@')
#     features['qty_and_params'] = params.count('&')
#     features['qty_exclamation_params'] = params.count('!')
#     features['qty_space_params'] = params.count(' ')
#     features['qty_tilde_params'] = params.count('~')
#     features['qty_comma_params'] = params.count(',')
#     features['qty_plus_params'] = params.count('+')
#     features['qty_asterisk_params'] = params.count('*')
#     features['qty_hashtag_params'] = params.count('#')
#     features['qty_dollar_params'] = params.count('$')
#     features['qty_percent_params'] = params.count('%')

#     # Length of the parameters string
#     features['params_length'] = len(params)
    
#     # Check for TLD presence in parameters
#     features['tld_present_params'] = int('.' in params)
    
#     return features

# def extract_features(url_data):
#     features = {}
#     # Extracting features from URL, domain, directory, file, parameters
#     features.update(extract_url_features(url_data))
#     domain = tldextract.extract(url_data).domain
#     features.update(extract_domain_features(domain))
#     features.update(extract_directory_features(url_data))
#     features.update(extract_file_features(url_data))
#     features.update(extract_param_features(url_data))
    
#     return features

# # Utility to check if a domain is an IP address (simple check)
# def is_ip(domain):
#     try:
#         # Attempt to convert the domain to an IP address
#         socket.inet_aton(domain)
#         return True
#     except socket.error:
#         return False
import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse

def extract_features(url):
    """
    Extracts features from a given URL for phishing detection.

    Parameters:
        url (str): The URL to analyze.

    Returns:
        dict: A dictionary of extracted features.
    """
    features = {}
    
    # Parse URL components
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    # URL-level features
    features['qty_dot_url'] = url.count('.')
    features['qty_hyphen_url'] = url.count('-')
    features['qty_underline_url'] = url.count('_')
    features['qty_slash_url'] = url.count('/')
    features['qty_questionmark_url'] = url.count('?')
    features['qty_equal_url'] = url.count('=')
    features['qty_at_url'] = url.count('@')
    features['qty_and_url'] = url.count('&')
    features['qty_exclamation_url'] = url.count('!')
    features['qty_space_url'] = url.count(' ')
    features['qty_tilde_url'] = url.count('~')
    features['qty_comma_url'] = url.count(',')
    features['qty_plus_url'] = url.count('+')
    features['qty_asterisk_url'] = url.count('*')
    features['qty_hashtag_url'] = url.count('#')
    features['qty_dollar_url'] = url.count('$')
    features['qty_percent_url'] = url.count('%')
    features['length_url'] = len(url)

    # Domain-level features
    features['qty_dot_domain'] = domain.count('.')
    features['qty_hyphen_domain'] = domain.count('-')
    features['qty_underline_domain'] = domain.count('_')
    features['qty_slash_domain'] = domain.count('/')
    features['qty_questionmark_domain'] = domain.count('?')
    features['qty_equal_domain'] = domain.count('=')
    features['qty_at_domain'] = domain.count('@')
    features['qty_and_domain'] = domain.count('&')
    features['qty_exclamation_domain'] = domain.count('!')
    features['qty_space_domain'] = domain.count(' ')
    features['qty_tilde_domain'] = domain.count('~')
    features['qty_comma_domain'] = domain.count(',')
    features['qty_plus_domain'] = domain.count('+')
    features['qty_asterisk_domain'] = domain.count('*')
    features['qty_hashtag_domain'] = domain.count('#')
    features['qty_dollar_domain'] = domain.count('$')
    features['qty_percent_domain'] = domain.count('%')
    features['qty_vowels_domain'] = sum(1 for char in domain if char.lower() in 'aeiou')
    features['domain_length'] = len(domain)
    features['domain_in_ip'] = 1 if re.match(r'^\d+\.\d+\.\d+\.\d+$', domain) else 0

    # Directory-level features
    features['qty_dot_directory'] = path.count('.')
    features['qty_hyphen_directory'] = path.count('-')
    features['qty_underline_directory'] = path.count('_')
    features['qty_slash_directory'] = path.count('/')
    features['qty_questionmark_directory'] = path.count('?')
    features['qty_equal_directory'] = path.count('=')
    features['qty_at_directory'] = path.count('@')
    features['qty_and_directory'] = path.count('&')
    features['qty_exclamation_directory'] = path.count('!')
    features['qty_space_directory'] = path.count(' ')
    features['qty_tilde_directory'] = path.count('~')
    features['qty_comma_directory'] = path.count(',')
    features['qty_plus_directory'] = path.count('+')
    features['qty_asterisk_directory'] = path.count('*')
    features['qty_hashtag_directory'] = path.count('#')
    features['qty_dollar_directory'] = path.count('$')
    features['qty_percent_directory'] = path.count('%')
    features['directory_length'] = len(path)

    # File-level features
    file = path.split('/')[-1] if '/' in path else ''
    features['qty_dot_file'] = file.count('.')
    features['qty_hyphen_file'] = file.count('-')
    features['qty_underline_file'] = file.count('_')
    features['qty_slash_file'] = file.count('/')
    features['qty_questionmark_file'] = file.count('?')
    features['qty_equal_file'] = file.count('=')
    features['qty_at_file'] = file.count('@')
    features['qty_and_file'] = file.count('&')
    features['qty_exclamation_file'] = file.count('!')
    features['qty_space_file'] = file.count(' ')
    features['qty_tilde_file'] = file.count('~')
    features['qty_comma_file'] = file.count(',')
    features['qty_plus_file'] = file.count('+')
    features['qty_asterisk_file'] = file.count('*')
    features['qty_hashtag_file'] = file.count('#')
    features['qty_dollar_file'] = file.count('$')
    features['qty_percent_file'] = file.count('%')
    features['file_length'] = len(file)

    # Query parameter-level features
    features['qty_dot_params'] = query.count('.')
    features['qty_hyphen_params'] = query.count('-')
    features['qty_underline_params'] = query.count('_')
    features['qty_slash_params'] = query.count('/')
    features['qty_questionmark_params'] = query.count('?')
    features['qty_equal_params'] = query.count('=')
    features['qty_at_params'] = query.count('@')
    features['qty_and_params'] = query.count('&')
    features['qty_exclamation_params'] = query.count('!')
    features['qty_space_params'] = query.count(' ')
    features['qty_tilde_params'] = query.count('~')
    features['qty_comma_params'] = query.count(',')
    features['qty_plus_params'] = query.count('+')
    features['qty_asterisk_params'] = query.count('*')
    features['qty_hashtag_params'] = query.count('#')
    features['qty_dollar_params'] = query.count('$')
    features['qty_percent_params'] = query.count('%')
    features['params_length'] = len(query)

    # Presence of specific attributes
    features['tld_present_params'] = 1 if re.search(r'\.[a-z]{2,}$', query) else 0
    features['qty_params'] = query.count('&') + 1 if query else 0

    # Additional features
    features['email_in_url'] = 1 if re.search(r'[\w.-]+@[\w.-]+', url) else 0

    return features

# Example usage
if __name__ == "__main__":
    url = input("Enter a URL: ")
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    print(features_df)
