# Problem Set 4B
# Name: Deniz Sert
# Collaborators: May Huang
# Time Spent: 5:00
# Late Days Used: 0

#NOTE: My computer's OS got wiped -> no Python Interpreter -> I WAS NOT ABLE TO RUN THE TESTS
#I wrote the code "blindly" using online IDEs

import string

### HELPER CODE ###
def load_words(file_name):
    '''
        file_name (string): the name of the file containing
        all the words to load
        
        Returns: a set of valid words. Words are strings of lowercase letters.
        
        Depending on the number of words to load, this function may
        take a while to finish.
        '''
    print("Loading word set from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # word_set: set of strings
    word_set = set()
    for line in inFile:
        word_set.update([word.lower() for word in line.split(' ')])
    print("  ", len(word_set), "words loaded.")
    inFile.close()
    return word_set

def is_word(word_set, word):
    '''
        Determines if word is a valid word, ignoring
        capitalization and punctuation
        
        word_set (set): set of words in the dictionary.
        word (string): a possible word.
        
        Returns: True if word is in word_set, False otherwise
        
        Example:
        >>> is_word(word_set, 'bat') returns
        True
        >>> is_word(word_set, 'asdf') returns
        False
        '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_set

def get_story_string():
    """
        Returns: a story in encrypted text.
        """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDSET_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
            Initializes a Message object
            
            input_text (string): the message's text
            
            a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (set, determined using helper function load_words)
            '''
        self.message_text = input_text
        self.valid_words = load_words("words.txt")
    
    
    def get_message_text(self):
        '''
            Used to safely access self.message_text outside of the class
            
            Returns: self.message_text
            '''
        return self.message_text
    
    def make_shift_dict(self, lowercase_shift, uppercase_shift):
        '''
            Creates a dictionary that can be used to apply a cipher to a letter.
            
            The dictionary maps every uppercase and lowercase letter to a
            character shifted down the alphabet by the corresponding shift. The
            shift values for uppercase and lowercase letters are distinct. If
            lowercase_shift is 2 and uppercase_shift is 4, then 'a' is mapped to 'c'
            but 'A' is mapped to 'E'.
            
            The dictionary should contain 52 keys of all the uppercase letters
            and all the lowercase letters only, mapped to their shifted values.
            
            lowercase_shift: the amount by which to shift every lowercase letter of the
            alphabet. 0 <= lowercase_shift < 26
            uppercase_shift: the amount by which to shift every lowercase letter of the
            alphabet. 0 <= uppercase_shift < 26
            
            Returns: a dictionary mapping letter (string) to
            another letter (string).
            '''
        #loops through number of letters in alphabet and indexes them to shift
        # mod to account for wraparound
        dict = {}
        for i in range(26):
            
            dict[string.ascii_lowercase[i] = string.ascii_lowercase[(i+lowercase_shift)%26]
                 dict[string.ascii_uppercase[i] = string.ascii_uppercase[(i+uppercase_shift)%26]
                      
                      return dict
                      
                      
                      def apply_shift(self, shift_dict):
                      '''
                          Applies the Caesar Cipher to self.message_text with letter shift
                          specified in shift_dict. Creates a new string that is self.message_text,
                          shifted down the alphabet by some number of characters, determined by
                          the shift value that shift_dict was built with.
                          
                          shift_dict: a dictionary with 52 keys, mapping
                          lowercase and uppercase letters to their new letters
                          (as built by make_shift_dict)
                          
                          Returns: the message text (string) with every letter shifted using the
                          input shift_dict
                          
                          '''
                      
                      
                      encrypted_mess = ''
                      
                      #loops through the encrypted text
                      for letter in self.message_text:
                      if letter in shift_dict:
                      encrypted_mess += shift_dict[letter]
                      else:
                      encrypted_mess += letter
                      #returns text with every letter shifted
                      return encrypted_mess
                      
                      
                      class PlaintextMessage(Message):
                      def __init__(self, input_text, lowercase_shift, uppercase_shift):
                      '''
                          Initializes a PlaintextMessage object.
                          
                          input_text (string): the message's text
                          lowercase_shift: the lowercase shift associated with this message
                          uppercase_shift: the uppercase shift associated with this message
                          
                          A PlaintextMessage object inherits from Message. It has five attributes:
                          self.message_text (string, determined by input text)
                          self.valid_words (set, determined using helper function load_words)
                          self.lowercase_shift (integer, determined by input lowercase_shift)
                          self.uppercase_shift (integer, determined by input uppercase_shift)
                          self.encryption_dict (dictionary, built using both shift values)
                          self.encrypted_message_text (string, encrypted using self.encryption_dict)
                          
                          '''
                      #initializes variable from superclass
                      super().__init__(input_text)
                      
                      
                      self.lowercase_shift = lowercase_shift
                      self.encryption_dict = make_shift_dict(lowercase_shift, uppercase_shift)
                      self.encrypted_message_text = apply_shift(self.encryption_dict)
                      
                      
                      def get_lowercase_shift(self):
                      '''
                          Used to safely access self.lowercase_shift outside of the class
                          
                          Returns: self.lowercase_shift
                          '''
                      return self.lowercase_shift
                      
                      def get_uppercase_shift(self):
                      '''
                          Used to safely access self.uppercase_shift outside of the class
                          
                          Returns: self.uppercase_shift
                          '''
                      return get_uppercase_shift
                      
                      def get_encryption_dict(self):
                      '''
                          Used to safely access a copy of self.encryption_dict outside of the class
                          
                          Returns: a COPY of self.encryption_dict
                          '''
                      return self.encryption_dict.copy()
                      
                      def get_encrypted_message_text(self):
                      '''
                          Used to safely access self.encrypted_message_text outside of the class
                          
                          Returns: self.encrypted_message_text
                          '''
                      self.encrypted_message_text
                      
                      def modify_shift(self, lowercase_shift, uppercase_shift):
                      '''
                          Changes self.lowercase_shift and self.uppercase_shift of the PlaintextMessage,
                          and updates any other attributes that are determined by the shift values.
                          
                          lowercase_shift: the new lowercase shift that should be associated with this message.
                          [0 <= lowercase_shift < 26]
                          uppercase_shift: the new uppercase shift that should be associated with this message.
                          [0 <= uppercase_shift < 26]
                          
                          Returns: nothing
                          '''
                      self.lowercase_shift = lowercase_shift
                      self.uppercase_shift = uppercase_shift
                      self.encryption_dict = make_shift_dict(lowercase_shift, uppercase_shift)
                      self.encrypted_message_text = apply_shift(self.encryption_dict)
                      
                      
                      class EncryptedMessage(Message):
                      def __init__(self, input_text):
                      '''
                          Initializes an EncryptedMessage object
                          
                          input_text (string): the message's text
                          
                          an EncryptedMessage object inherits from Message. It has two attributes:
                          self.message_text (string, determined by input text)
                          self.valid_words (set, determined using helper function load_words)
                          '''
                      
                      super().__init__(input_text)
                      
                      
                      def decrypt_message(self):
                      '''
                          Decrypts self.message_text by trying every possible pair of lowercase and uppercase
                          shift values, and finding the "best" pair.
                          
                          We will define "best" as the shift pair that creates the max number of
                          valid English words when we use apply_shift(shift_dict) on the message text, using the
                          shift_dict created by this pair. For either shift, if a is the original shift value used
                          to encrypt the message, then we would expect (26 - a) to be the value found for decrypting it.
                          
                          Note: if shift pairs are equally good, such that they all create the
                          max number of valid words, you may choose any of those shift pairs
                          (and their corresponding decrypted messages) to return.
                          
                          Returns a tuple of:
                          - the best shift value pair used to originally encrypt the message, as a tuple itself
                          - the decrypted message text using that shift pair
                          -> ((best_lowercase_shift, best_uppercase_shift), decrypted_message)
                          '''
                      
                      
                      max_of = 0
                      shift_max = ()
                      #double loop to account for lower and upper cases
                      for lower_shift in range(26):
                      for upper_shift in range(26):
                      #reset counter to find max word
                      counter = 0
                      shift_dict = make_shift_dict(26-lower_shift, 26-upper_shift)
                      message = apply_shift(message, shift_dict)
                      words = message.split()
                      #loops through words in message
                      for word in words:
                      #checks if each word is an actual word
                      if is_word(self.valid_words, word):
                      counter+=1
                      
                      #checks to see if this is the largest number of actual words
                      #record the lower and upper shift that had largest num of actual words
                      if counter>max_of:
                      max_of = counter
                      shift_max = ((lower_shift, upper_shift), message)
                      
                      return shift_max
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      def test_plaintext_message():
                      '''
                          Write two test cases for the PlaintextMessage class here.
                          Each one should handle different cases (see handout for
                          more details.) Write a comment above each test explaining what
                          case(s) it is testing.
                          '''
                      
                      #### Example test case (PlaintextMessage) #####
                      
                      # This test is checking encoding a lowercase string with punctuation in it.
                      plaintext = PlaintextMessage('hello!', 2, 0)
                      print('Expected Output: jgnnq!')
                      print('Actual Output:', plaintext.get_encrypted_message_text())
                      
                      pass # delete this line and replace with your code here
                      
                      def test_encrypted_message():
                      '''
                          Write two test cases for the EncryptedMessage class here.
                          Each one should handle different cases (see handout for
                          more details.) Write a comment above each test explaining what
                          case(s) it is testing.
                          '''
                      
                      #### Example test case (EncryptedMessage) #####
                      
                      # This test is checking decoding a lowercase string with punctuation in it.
                      encrypted = EncryptedMessage('jgnnq!')
                      print('Expected Output:', (2, 'hello!'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      # This test is checking decoding a lowercase string with punctuation in it.
                      encrypted = EncryptedMessage('jgnnq!')
                      print('Expected Output:', (2, 'hello!'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      #This test is checking decoding a lowercase string.
                      encrypted = EncryptedMessage('fuuqj')
                      print('Expected Output:', (5, 'apple'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      #This test is checking decoding a combination of lowercase and uppercase chars with a punctuation.
                      encrypted = EncryptedMessage('Xuckx!')
                      print('Expected Output:', (6, 'Rower!'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      encrypted = EncryptedMessage('Xuckx!')
                      print('Expected Output:', (6, 'Rower!'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      #This test is checking decoding an all uppercase string.
                      encrypted = EncryptedMessage('EAIWSQI')
                      print('Expected Output:', (4, 'AWESOME'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      
                      #This test is checking decoding an all uppercase string.
                      encrypted = EncryptedMessage('LOKX')
                      print('Expected Output:', (10, 'BEAN'))
                      print('Actual Output:', encrypted.decrypt_message())
                      
                      
                      
                      def decode_story():
                      '''
                          Write your code here to decode the story contained in the file story.txt.
                          Hint: use the helper function get_story_string and your EncryptedMessage class.
                          
                          Returns: a tuple containing ((best_lowercase_shift, best_uppercase_shift), decoded_story)
                          
                          '''
                      encrypted = EncryptedMessage(get_story_string())
                      return encrypted.decrypt_message()
                      
                      
                      if __name__ == '__main__':
                      
                      # Uncomment these lines to try running your test cases
                      # test_plaintext_message()
                      # test_encrypted_message()
                      
                      # Uncomment these lines to try running decode_story_string()
                      # best_shift, story = decode_story()
                      # print("Best shift:", best_shift)
                      # print("Decoded story: ", story)
                      pass
