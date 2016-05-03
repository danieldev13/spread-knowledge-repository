import sys

compensation_factor = 1
max_tweet_length = 140
max_tweetstorm_length = 138


def main():
    text = sys.argv[1]
    length = len(text)
    result = divmod(length, max_tweet_length)
    total_of_tweets = result[0] + 1 if (result[1] > 0) else 0
    list_of_tweets = []
    start = 0
    end = max_tweetstorm_length
    counter = 1

    while total_of_tweets >= counter:
        result_text = cut_text(text, start, end)
        list_of_tweets.append(result_text)
        start += len(result_text) + compensation_factor
        end = start + max_tweetstorm_length
        counter += 1

    check_tweetstorm(list_of_tweets, text)
    print_result(list_of_tweets)


def cut_text(text, start, end):
    result = text[start:end]

    if len(result) >= max_tweetstorm_length:
            result = result[0: result.rindex(" ")]

    return result.lstrip()


def print_result(list_of_tweets):
    counter = 1
    for tweet in list_of_tweets:
        print("{}/{}".format(str(counter), tweet))
        counter += 1


def check_tweetstorm(list_of_tweets, original_text):
    joined_text = " ".join(list_of_tweets)
    list_length = len(joined_text)
    original_length = len(original_text)

    if list_length < original_length:
        final_index = list_length + (original_length - list_length)
        last_tweet = original_text[list_length:final_index]

        list_of_tweets.append(last_tweet.lstrip())

main()
