def is_palindrome(s):
        # Remove spaces and convert to lowercase for uniformity
            s = s.replace(" ", "").lower()
                # Check if the string is equal to its reverse
                    return s == s[::-1]

                if __name__ == "__main__":
                        print("Hello, World!")
                            
                                # Test the is_palindrome function
                                    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
                                        for string in test_strings:
                                                    print(f'"{string}" is a palindrome: {is_palindrome(string)}')

