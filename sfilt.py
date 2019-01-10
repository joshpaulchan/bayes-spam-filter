#! /usr/bin/env python3
# Joshua Paul A. Chan
# This is an exercise in understanding and implementing the Bayes Theorem as a spam filter.

import string

class Message(object):
    
    def __init__(self, email_to, email_from, body):
        self.email_to = email_to
        self.email_from = email_from
        self.body = body
    
    def get_recipients(self):
        return self.email_to
    
    def get_sender(self):
        return self.email_from
    
    def get_body(self):
        return self.body
    
    def __str__(self):
        # 40 is about less than half an average sentence
        # 5.1 + 1 avg char length per word + whitespace
        # 14 words per sentence on avg
        return "<Message '{}..'>".format(self.body[:40])
        
    def __repr__(self):
        return str(self)

class SpamFilter(object):
    
    # Build a SpamFilter from a model
    @classmethod
    def load_model(cls, fname):
        sf = cls()
        f = open(fname, 'r')
        for line in f:
            w, p_s, p_n = line.split(',')
            sf.set_word(w, float(p_s), float(p_n))
        return sf
    
    def save_model(self, fname):
        f = open(fname, 'w+')
        for word, p in self.words:
            f.write('{},{},{}\n'.format(word, p[0], p[1]))
    
    def __init__(self):
        self.words = {
            # 'i': [0.5, 0.5],
            'rolex': [ 0.0125, 0.005],
            'stock': [ 0.2, 0.06],
            'undervalued': [0.1, 0.025]
        }
    
    def set_word(self, w, p_spam, p_not):
        self.words[w] = [p_spam, p_not]
    
    def tokenize_words(self, text):
        return map(lambda w: w.strip(' ').strip(string.punctuation).lower(), text.split(' '))
    
    def train(self, message, result):
        # TODO
        pass
    
    # determines if given message is spam
    # @param:   message:<Message>
    # @returns  boolean
    def is_spam(self, msg):
        print(msg)
        # tokenize body
        words = self.tokenize_words(msg.body)
        # print(words)
        
        P_spam = 0
        P_notspam = 0
        for word in words:
            probs = self.words.get(word)
            # print(probs)
            
            if probs != None:
                P_spam = P_spam*probs[0]
                P_notspam = P_notspam*probs[1]
                
                if P_spam == 0:
                    P_spam = probs[0]
                if P_notspam == 0:
                    P_notspam = probs[1]
                
                # print(P_spam)
                # print(P_notspam)
        if (P_spam + P_notspam) == 0:
            return 0     
        return (P_spam)/(P_spam + P_notspam)
    
    
# TRAINING SETS
# non-spam

B = [
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL'),
    Message('me', 'you', 'LOLOLOLOL')
]

G = [
    Message('me', 'you', 'Hey I have this rolex that you might like.'),
    Message('me', 'you', 'What are you doing for lunch tmm?'),
    Message('me', 'you', 'Hello')
]

# Parses CLI flags and commands
# @param filename
# @returns <Tuple(<Float>,<String>)>
def main():
    f = SpamFilter.load_model('model.txt')
    
    # Train model
    
    # Parse filename
    
    # Read file
    
    # Predict
    for message in G:
        confidence = f.is_spam(message)
        print("{:.2%} probability that this is spam.\n".format(confidence))
    
    # Report 

if __name__ == '__main__':
    main()


    
