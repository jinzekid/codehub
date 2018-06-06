# Author: Jason Lu

quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a4 successful man is na exhausted woman',
          'Black holes really suck...', 'Facts are stubborn things.')

class QuoteMode:
    def get_guote(self, n):
        try:
            n = n - 1
            if n >= 0 and n < len(quotes):
                value = quotes[n]
            else:
                value = 'Not found!'

        except IndexError as e:
            value = 'Not found!'

        return value


class QuoteTerminalView:
    def show(self, quote):
        print('Add the quote is: {}'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see?')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteMode()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error('Incorrect index {}'.format(n))

        quote = self.model.get_guote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()