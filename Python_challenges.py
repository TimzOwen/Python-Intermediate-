
def print_message(day):
    messages = {
        'monday': 'Let\'s Code Python',
        'tuesday': 'We start writing scripts',
        'wednesday': 'Time for Automation.',
        'thursday': 'Find ad fix errors',
        'friday': 'Read some novels',
        'saturday': 'Go for meet ups',
        'sunday': 'Go to church'
    }
    print(messages[day])

def print_friday_message():
    print_message('Friday')

print_friday_message()
